# =============================================================================
# config.py — Project Configuration
# this is where the API key goes
# the base_url basically acts as the front door for the API. so intead of typing a long url into the code we can just store it in config and reference it when it's needed
# =============================================================================

API_KEY = "7INVJN5YRPL01XX2"

BASE_URL = "https://www.alphavantage.co/query"

# Maps the user-facing time series names to the Alpha Vantage function names
# and the corresponding JSON key returned by the API.
# as long as it works you don't really need to do anything with this
TIME_SERIES_OPTIONS = {
    "1": {
        "label":    "Daily",
        "function": "TIME_SERIES_DAILY",
        "json_key": "Time Series (Daily)",
    },
    "2": {
        "label":    "Weekly",
        "function": "TIME_SERIES_WEEKLY",
        "json_key": "Weekly Time Series",
    },
    "3": {
        "label":    "Monthly",
        "function": "TIME_SERIES_MONTHLY",
        "json_key": "Monthly Time Series",
    },
}

# Maps chart type choices to Plotly trace types
CHART_TYPE_OPTIONS = {
    "1": {"label": "Bar",  "type": "bar"},
    "2": {"label": "Line", "type": "line"},
}
