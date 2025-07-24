from __future__ import annotations

from ibm_wxdi.utils.session import Session

from ibm_wxdi.config import BASE_URL


class Tags:
    """Manage catalog categories and tags."""

    def __init__(self, session: Session):
        self.session = session
        self.url = f"{BASE_URL}/categories"

    def get_categories(self) -> dict:
        response = self.session.get(self.url)
        return response.json()

    def get_category_ids(self, limit: int = 5) -> list[str]:
        categories = self.get_categories()
        ids = [c.get("id") for c in categories.get("categories", [])]
        return ids[:limit]
