# =============================================================================
# task6_visualizer.py — Task 6: Fetch data from Alpha Vantage and generate chart
# =============================================================================
# This module handles two responsibilities:
#   1. Querying the Alpha Vantage API for stock data
#   2. Filtering by date range, building the chart, and opening it in the browser
# =============================================================================

import os
import sys
import webbrowser
from datetime import datetime

import requests
import plotly.graph_objects as go

from config import API_KEY, BASE_URL


# --------------------------------------------------------------------------- #
#  API Data Fetching
# --------------------------------------------------------------------------- #

def fetch_stock_data(symbol: str, function: str) -> dict:
    """
    Calls the Alpha Vantage API and returns the full JSON response.

    Args:
        symbol   (str): The stock ticker symbol (e.g. 'AAPL').
        function (str): The Alpha Vantage function name
                        (e.g. 'TIME_SERIES_DAILY').

    Returns:
        dict: The raw JSON response from the API.

    Raises:
        SystemExit: If the API returns an error or the symbol is not found.
    """
    params = {
        "function":   function,
        "symbol":     symbol,
        "outputsize": "full",   # return up to 20 years of data
        "apikey":     API_KEY,
        "datatype":   "json",
    }

    print(f"\n  Querying Alpha Vantage for '{symbol}' ({function})...")

    try:
        response = requests.get(BASE_URL, params=params, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"  [!] Network error: {err}")
        sys.exit(1)

    data = response.json()

    # Alpha Vantage returns error info inside the JSON body (not HTTP status)
    if "Error Message" in data:
        print(f"  [!] API Error: {data['Error Message']}")
        sys.exit(1)

    if "Information" in data:
        # This usually means the free-tier rate limit was hit
        print(f"  [!] API Notice: {data['Information']}")
        sys.exit(1)

    return data


# --------------------------------------------------------------------------- #
#  Data Filtering
# --------------------------------------------------------------------------- #

def filter_by_date_range(
    raw_data:   dict,
    json_key:   str,
    begin_date: datetime,
    end_date:   datetime,
) -> tuple[list[str], list[float]]:
    """
    Extracts closing prices from the API response and filters them to the
    requested date range.

    Args:
        raw_data   (dict):     Full API JSON response.
        json_key   (str):      The key that holds the time series data
                               (e.g. 'Time Series (Daily)').
        begin_date (datetime): Start of the date range.
        end_date   (datetime): End of the date range.

    Returns:
        tuple[list[str], list[float]]:
            - Sorted list of date strings (YYYY-MM-DD)
            - Corresponding list of closing prices (float)

    Raises:
        SystemExit: If the expected JSON key is missing.
    """
    if json_key not in raw_data:
        available = list(raw_data.keys())
        print(f"  [!] Expected key '{json_key}' not found in API response.")
        print(f"      Available keys: {available}")
        sys.exit(1)

    time_series = raw_data[json_key]

    begin_str = begin_date.strftime("%Y-%m-%d")
    end_str   = end_date.strftime("%Y-%m-%d")

    filtered = {
        date: values
        for date, values in time_series.items()
        if begin_str <= date <= end_str
    }

    if not filtered:
        print(
            f"\n  [!] No data found between {begin_str} and {end_str}.\n"
            "      Try a wider date range, or check that the stock was active during that period."
        )
        sys.exit(1)

    dates  = sorted(filtered.keys())
    closes = [float(filtered[d]["4. close"]) for d in dates]

    return dates, closes


# --------------------------------------------------------------------------- #
#  Chart Generation
# --------------------------------------------------------------------------- #

def generate_chart(
    symbol:     str,
    chart_type: str,
    json_key:   str,
    raw_data:   dict,
    begin_date: datetime,
    end_date:   datetime,
) -> None:
    """
    Filters the stock data, builds a Plotly chart, saves it as an HTML file,
    and opens it in the user's default web browser.

    Args:
        symbol     (str):      Stock ticker (used for chart title and filename).
        chart_type (str):      'bar' or 'line'.
        json_key   (str):      Key to locate the time series in raw_data.
        raw_data   (dict):     Full API JSON response from fetch_stock_data().
        begin_date (datetime): Start of the date range.
        end_date   (datetime): End of the date range.
    """
    dates, closes = filter_by_date_range(raw_data, json_key, begin_date, end_date)

    begin_str = begin_date.strftime("%Y-%m-%d")
    end_str   = end_date.strftime("%Y-%m-%d")
    title     = f"{symbol} — Closing Price  ({begin_str} to {end_str})"

    # Build the Plotly trace based on the chosen chart type
    if chart_type == "bar":
        trace = go.Bar(
            x=dates,
            y=closes,
            name=symbol,
            marker_color="steelblue",
        )
    else:  # line
        trace = go.Scatter(
            x=dates,
            y=closes,
            mode="lines+markers",
            name=symbol,
            line=dict(color="steelblue", width=2),
        )

    fig = go.Figure(data=[trace])
    fig.update_layout(
        title=dict(text=title, font=dict(size=18)),
        xaxis_title="Date",
        yaxis_title="Closing Price (USD)",
        hovermode="x unified",
        template="plotly_white",
    )

    # Save the chart as a self-contained HTML file in the current directory
    output_file = f"{symbol}_chart.html"
    fig.write_html(output_file)

    abs_path = os.path.abspath(output_file)
    print(f"\n  Chart saved to: {abs_path}")
    print("  Opening chart in your default browser...\n")
    webbrowser.open(f"file://{abs_path}")
