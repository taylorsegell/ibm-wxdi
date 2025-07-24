from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class Assets:
    """Operations related to catalog assets."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/catalogs"

    def get_catalogs(self) -> dict:
        response = self.session.get(self.url)
        return response.json()

    def get_catalog_id_by_name(self, name: str) -> str:
        catalogs = self.get_catalogs()
        for catalog in catalogs.get("catalogs", []):
            if catalog.get("name") == name:
                return catalog.get("id")
        raise ValueError(f"Catalog '{name}' not found")
