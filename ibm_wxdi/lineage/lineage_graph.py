from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class LineageGraph:
    """Retrieve lineage information for assets."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/lineage"

    def get_lineage(self, asset_id: str) -> dict:
        response = self.session.get(f"{self.url}/{asset_id}")
        return response.json()
