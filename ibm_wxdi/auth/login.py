from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.auth.token_manager import TokenManager
from ibm_wxdi.utils.exceptions import AuthenticationError


def login(api_key: str) -> Session:
    """Authenticate and return a session with auth headers."""
    manager = TokenManager(api_key)
    token = manager.get_token()
    if not token:
        raise AuthenticationError("Unable to acquire token")

    session = Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session
