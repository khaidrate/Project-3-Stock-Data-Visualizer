# =============================================================================
# task1_stock_symbol.py — Task 1: Ask the user for a stock symbol
# =============================================================================

def get_stock_symbol() -> str:
    """
    Prompts the user to enter a stock ticker symbol (e.g. AAPL, TSLA).
    Keeps asking until a non-empty, letters-only value is provided.

    Returns:
        str: The validated stock symbol in uppercase.
    """
    while True:
        symbol = input("Enter the stock symbol for the company (e.g. AAPL): ").strip().upper()

        if not symbol:
            print("  [!] Symbol cannot be empty. Please try again.\n")
            continue

        if not symbol.isalpha():
            print("  [!] Symbol should contain letters only (no spaces or numbers). Please try again.\n")
            continue

        return symbol
