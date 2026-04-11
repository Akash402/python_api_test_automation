import base64
import time
import requests
import config

_oauth_cache = {
    "token": None,
    "expires_at": 0
}


def get_auth_headers():
    if config.AUTH_TYPE == "none":
        return {}

    elif config.AUTH_TYPE == "basic":
        return _basic_auth_headers()

    elif config.AUTH_TYPE == "oauth":
        return _oauth_headers()

    elif config.AUTH_TYPE == "api_key":
        return {config.API_KEY_HEADER: config.API_KEY}


def _basic_auth_headers():
    credentials = f"{config.USERNAME}:{config.PASSWORD}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}


def _oauth_headers():
    token = _get_valid_oauth_token()
    return {"Authorization": f"Bearer {token}"}


def _get_valid_oauth_token():
    now = time.time()
    if _oauth_cache["token"] and now < _oauth_cache["expires_at"]:
        return _oauth_cache["token"]

    response = requests.post(
        config.TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": config.CLIENT_ID,
            "client_secret": config.CLIENT_SECRET
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"OAuth token request failed ({response.status_code}): {response.text}"
        )

    data = response.json()
    _oauth_cache["token"] = data["access_token"]
    # Refresh 30 seconds before actual expiry to avoid edge cases
    _oauth_cache["expires_at"] = now + data.get("expires_in", 3600) - 30

    return _oauth_cache["token"]
