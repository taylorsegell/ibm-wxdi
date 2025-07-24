from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class Metadata:
    """Metadata import operations."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/metadata_imports"

    def create_metadata_import(
        self, connection_id: str, paths_scope: list[str]
    ) -> dict:
        payload = {"connection_id": connection_id, "paths": paths_scope}
        response = self.session.post(self.url, json=payload)
        return response.json()

    def run_metadata_import_job(self, mdi_id: str) -> dict:
        response = self.session.post(f"{self.url}/{mdi_id}/jobs")
        return response.json()

    def get_metadata_import_details(self, mdi_id: str) -> dict:
        response = self.session.get(f"{self.url}/{mdi_id}")
        return response.json()
