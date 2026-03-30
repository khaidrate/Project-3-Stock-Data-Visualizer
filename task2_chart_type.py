# =============================================================================
# task2_chart_type.py — Task 2: Ask the user for the chart type
# =============================================================================

from config import CHART_TYPE_OPTIONS


def get_chart_type() -> str:
    """
    Displays the available chart types and prompts the user to choose one.
    Keeps asking until a valid option is entered.

    Returns:
        str: The chart type string, either 'bar' or 'line'.
    """
    print("\nAvailable chart types:")
    for key, option in CHART_TYPE_OPTIONS.items():
        print(f"  {key}. {option['label']}")

    while True:
        choice = input("Enter the number for the chart type you want: ").strip()

        if choice in CHART_TYPE_OPTIONS:
            selected = CHART_TYPE_OPTIONS[choice]
            print(f"  -> Chart type selected: {selected['label']}")
            return selected["type"]

        print(f"  [!] Invalid choice. Please enter a number between 1 and {len(CHART_TYPE_OPTIONS)}.\n")
