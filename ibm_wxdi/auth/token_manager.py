from __future__ import annotations

from urllib import request, parse
import json

from ibm_wxdi.config import BASE_URL
from ibm_wxdi.utils.exceptions import AuthenticationError


class TokenManager:
    """Handle IAM token generation and refresh."""

    def __init__(self, api_key: str, url: str | None = None) -> None:
        self.api_key = api_key
        self.url = url or f"{BASE_URL}/authorize"
        self._token: str | None = None

    def refresh_token(self) -> None:
        data = parse.urlencode(
            {
                "apikey": self.api_key,
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            }
        ).encode()
        req = request.Request(self.url, data=data, method="POST")
        try:
            with request.urlopen(req) as resp:
                payload = json.loads(resp.read().decode())
        except Exception as exc:  # pragma: no cover - network failure
            raise AuthenticationError("Failed to retrieve token") from exc
        self._token = payload.get("access_token")

    def get_token(self) -> str:
        if not self._token:
            self.refresh_token()
        assert self._token is not None
        return self._token
