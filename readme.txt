Stock Data Visualization
IT4320 Software Engineering — Project 3
Scrum Team 8

What It Does
This Python application lets a user look up historical stock data for any publicly traded company using the Alpha Vantage API. The user selects a stock symbol, a chart type, a time series interval, and a custom date range. The app then fetches the data and automatically opens an interactive chart in the user's default web browser.

Setup
1. Install dependencies (one time only)
      Open a terminal inside the project folder and run:
pip install -r requirements.txt
2. Run the application
      python main.py

How to Use It
Once running, the app will walk you through five prompts in order:
PromptExample InputStock symbolAAPL, TSLA, GOOGLChart type1 for Bar, 2 for LineTime series1 Daily, 2 Weekly, 3 MonthlyBeginning date2022-01-01End date2023-01-01
After the last prompt, the app fetches the data and opens your chart in the browser. The chart is also saved as SYMBOL_chart.html in the project folder so you can reopen it anytime.

File Structure
Stock Visualizer/
├── main.py                  ← Entry point — run this to start the app
├── config.py                ← API key and shared settings
├── task1_stock_symbol.py    ← Handles stock symbol input
├── task2_chart_type.py      ← Handles chart type selection
├── task3_time_series.py     ← Handles time series function selection
├── task4_begin_date.py      ← Handles beginning date input
├── task5_end_date.py        ← Handles end date input and validation
├── task6_visualizer.py      ← Fetches API data and generates the chart

How Each Module Fulfills a Project Task
Task 1 — task1_stock_symbol.py
Asks the user to enter a stock ticker symbol (e.g. AAPL). Validates that the input is non-empty and contains only letters before passing it along.
Task 2 — task2_chart_type.py
Presents the user with a numbered menu of chart types (Bar or Line) and returns their selection. Keeps prompting if an invalid option is entered.
Task 3 — task3_time_series.py
Presents the user with a numbered menu of Alpha Vantage time series functions (Daily, Weekly, Monthly). Returns both the API function name and the corresponding JSON key needed to parse the response.
Task 4 — task4_begin_date.py
Asks the user for a beginning date in YYYY-MM-DD format. Validates the format using Python's datetime module and keeps prompting until a valid date is entered.
Task 5 — task5_end_date.py
Asks the user for an end date in YYYY-MM-DD format. In addition to format validation, it checks that the end date is not before the beginning date, re-prompting the user if it is.
Task 6 — task6_visualizer.py
Handles two things: first, it calls the Alpha Vantage API using the requests library and retrieves up to 20 years of stock data. Then it filters that data to the user's selected date range, builds an interactive chart using plotly, saves it as an HTML file, and opens it automatically in the user's default web browser.


Notes

You can only use the API key 25 times a day unless you have a paid key, which we don't
The generated chart file (SYMBOL_chart.html) is saved in the same folder as main.py and will be overwritten each time you run the app with the same symbol.
