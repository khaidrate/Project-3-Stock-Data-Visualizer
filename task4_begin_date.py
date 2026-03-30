# =============================================================================
# task4_begin_date.py — Task 4: Ask the user for the beginning date
# =============================================================================

from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"


def get_begin_date() -> datetime:
    """
    Prompts the user to enter a start date in YYYY-MM-DD format.
    Keeps asking until a valid date is entered.

    Returns:
        datetime: The validated beginning date as a datetime object.
    """
    print()
    while True:
        date_str = input("Enter the beginning date (YYYY-MM-DD): ").strip()

        try:
            date = datetime.strptime(date_str, DATE_FORMAT)
            print(f"  -> Begin date set: {date.strftime(DATE_FORMAT)}")
            return date
        except ValueError:
            print("  [!] Invalid date or format. Please use YYYY-MM-DD (e.g. 2022-01-15).\n")
