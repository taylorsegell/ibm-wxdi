from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class Connections:
    """Manage datasource connections."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/connections"

    def define_connection(self, connection_type: str, config: dict) -> dict:
        payload = {"type": connection_type, "config": config}
        response = self.session.post(self.url, json=payload)
        return response.json()

    def get_connections(self) -> dict:
        response = self.session.get(self.url)
        return response.json()
