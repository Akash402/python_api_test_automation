import os

# Active environment: dev | staging | prod
# Override at runtime: ENV=staging robot -d results api/tests/
ENV = os.environ.get("ENV", "dev")

ENVIRONMENTS = {
    "dev":     os.environ.get("DEV_URL",     "https://restful-booker.herokuapp.com/"),
    "staging": os.environ.get("STAGING_URL", ""),
    "prod":    os.environ.get("PROD_URL",    ""),
}

if ENV not in ENVIRONMENTS:
    raise EnvironmentError(
        f"Invalid ENV '{ENV}'. Must be one of: {', '.join(ENVIRONMENTS.keys())}."
    )

if not ENVIRONMENTS[ENV]:
    raise EnvironmentError(
        f"No URL configured for ENV='{ENV}'. Set {ENV.upper()}_URL in your .env file."
    )

BASE_URL = ENVIRONMENTS[ENV]

# Auth strategy: "basic", "oauth", "api_key", "none"
AUTH_TYPE = os.environ.get("AUTH_TYPE", "basic")

# Basic auth
USERNAME = os.environ.get("API_USERNAME", "")
PASSWORD = os.environ.get("API_PASSWORD", "")

# OAuth (client credentials)
TOKEN_URL = os.environ.get("TOKEN_URL", "")
CLIENT_ID = os.environ.get("CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "")

# API Key
API_KEY = os.environ.get("API_KEY", "")
API_KEY_HEADER = os.environ.get("API_KEY_HEADER", "x-api-key")

ENDPOINTS = {
    "ping": "ping",
    "all_bookings": "booking",
    "authentication": "auth",
    "get_booking": "booking/"
}

# Validate required env vars based on AUTH_TYPE
_missing = []

if AUTH_TYPE == "basic":
    if not USERNAME:
        _missing.append("API_USERNAME")
    if not PASSWORD:
        _missing.append("API_PASSWORD")

elif AUTH_TYPE == "oauth":
    if not TOKEN_URL:
        _missing.append("TOKEN_URL")
    if not CLIENT_ID:
        _missing.append("CLIENT_ID")
    if not CLIENT_SECRET:
        _missing.append("CLIENT_SECRET")

elif AUTH_TYPE == "api_key":
    if not API_KEY:
        _missing.append("API_KEY")

elif AUTH_TYPE == "none":
    pass

else:
    raise EnvironmentError(
        f"Invalid AUTH_TYPE '{AUTH_TYPE}'. Must be one of: basic, oauth, api_key, none."
    )

if _missing:
    raise EnvironmentError(
        f"Missing required environment variables for AUTH_TYPE='{AUTH_TYPE}': {', '.join(_missing)}.\n"
        f"Copy .env.example to .env and fill in the required values."
    )
