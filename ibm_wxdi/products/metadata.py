from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class MetadataEnrichment:
    """Operations for metadata enrichment."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/metadata_enrichments"

    def create_metadata_enrichment(
        self,
        name: str,
        mdi_id: str,
        job_name: str,
        publish_job_name: str,
    ) -> dict:
        payload = {
            "name": name,
            "metadata_import_id": mdi_id,
            "job_name": job_name,
            "publish_job_name": publish_job_name,
        }
        response = self.session.post(self.url, json=payload)
        return response.json()

    def publish_metadata_enrichment_assets(self, enrichment_id: str) -> dict:
        response = self.session.post(f"{self.url}/{enrichment_id}/publish")
        return response.json()

    def update_metadata_enrichment_settings(
        self, enrichment_id: str, settings: dict
    ) -> dict:
        response = self.session.patch(f"{self.url}/{enrichment_id}", json=settings)
        return response.json()
