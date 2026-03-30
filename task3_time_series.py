# =============================================================================
# task3_time_series.py — Task 3: Ask the user for the time series function
# =============================================================================

from config import TIME_SERIES_OPTIONS


def get_time_series() -> tuple[str, str]:
    """
    Displays the available Alpha Vantage time series functions and prompts
    the user to choose one.

    Returns:
        tuple[str, str]: A tuple of (function_name, json_key) where
            - function_name is the Alpha Vantage API function string
              (e.g. 'TIME_SERIES_DAILY')
            - json_key is the key used to extract data from the API response
              (e.g. 'Time Series (Daily)')
    """
    print("\nAvailable time series functions:")
    for key, option in TIME_SERIES_OPTIONS.items():
        print(f"  {key}. {option['label']}")

    while True:
        choice = input("Enter the number for the time series function you want: ").strip()

        if choice in TIME_SERIES_OPTIONS:
            selected = TIME_SERIES_OPTIONS[choice]
            print(f"  -> Time series selected: {selected['label']}")
            return selected["function"], selected["json_key"]

        print(f"  [!] Invalid choice. Please enter a number between 1 and {len(TIME_SERIES_OPTIONS)}.\n")
