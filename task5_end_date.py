# =============================================================================
# task5_end_date.py — Task 5: Ask the user for the end date
# =============================================================================
# Rule: The end date must NOT be before the begin date.
# =============================================================================

from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"


def get_end_date(begin_date: datetime) -> datetime:
    """
    Prompts the user to enter an end date in YYYY-MM-DD format.
    Validates that the end date is not before the begin date.
    Keeps asking until a valid date is entered.

    Args:
        begin_date (datetime): The start date returned by task4_begin_date.

    Returns:
        datetime: The validated end date as a datetime object.
    """
    while True:
        date_str = input("Enter the end date     (YYYY-MM-DD): ").strip()

        try:
            date = datetime.strptime(date_str, DATE_FORMAT)
        except ValueError:
            print("  [!] Invalid date or format. Please use YYYY-MM-DD (e.g. 2023-12-31).\n")
            continue

        if date < begin_date:
            print(
                f"  [!] End date ({date.strftime(DATE_FORMAT)}) cannot be before "
                f"begin date ({begin_date.strftime(DATE_FORMAT)}). Please try again.\n"
            )
            continue

        print(f"  -> End date set:   {date.strftime(DATE_FORMAT)}")
        return date
