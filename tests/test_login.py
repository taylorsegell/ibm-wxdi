from ibm_wxdi.auth.login import login
from ibm_wxdi.utils.session import Session


def test_login_returns_session(monkeypatch):
    class DummyTokenManager:
        def __init__(self, api_key):
            pass

        def get_token(self):
            return "TOKEN"

    monkeypatch.setattr("ibm_wxdi.auth.login.TokenManager", DummyTokenManager)
    session = login(api_key="dummy")
    assert isinstance(session, Session)
    assert session.headers.get("Authorization") == "Bearer TOKEN"
