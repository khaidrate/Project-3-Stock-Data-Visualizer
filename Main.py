# =============================================================================
# main.py — Entry Point
# =============================================================================
# Ties all 6 task modules together into one cohesive application.
# Nothing needs to be changed about this because this doesn't really do anything by itself
# Run with:
#   python main.py
# =============================================================================

from task1_stock_symbol import get_stock_symbol
from task2_chart_type    import get_chart_type
from task3_time_series   import get_time_series
from task4_begin_date    import get_begin_date
from task5_end_date      import get_end_date
from task6_visualizer    import fetch_stock_data, generate_chart


def main() -> None:
    print("=" * 50)
    print("   Stock Data Visualization — Alpha Vantage")
    print("=" * 50)

    # Task 1 — Stock symbol
    symbol = get_stock_symbol()

    # Task 2 — Chart type
    chart_type = get_chart_type()

    # Task 3 — Time series function
    function, json_key = get_time_series()

    # Task 4 — Beginning date
    begin_date = get_begin_date()

    # Task 5 — End date (validated against begin date)
    end_date = get_end_date(begin_date)

    # Task 6 — Fetch data and generate chart
    raw_data = fetch_stock_data(symbol, function)
    generate_chart(symbol, chart_type, json_key, raw_data, begin_date, end_date)


if __name__ == "__main__":
    main()
