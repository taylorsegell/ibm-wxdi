from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class Governance:
    """Import and manage governance artifacts."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/governance/artifacts"

    def import_governance_artifacts(self, zip_file_path: str) -> dict:
        with open(zip_file_path, "rb") as file:
            files = {"file": file}
            response = self.session.post(self.url, files=files)
        return response.json()

    def check_import_status(self, process_id: str) -> dict:
        response = self.session.get(f"{self.url}/{process_id}")
        return response.json()
