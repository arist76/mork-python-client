import httpx
from httpx import URL
from typing import Optional
import os


class MorkClient:
    def __init__(self, url: Optional[str| URL] = os.environ.get("MORK_URL")):
        if url is None:
            raise ValueError(
                "MORK_URL environment variable is not set. Please set it using \
                `export MORK_URL=http://localhost:8000`."
            )

        if isinstance(url, URL):
            self.url = url
            return

        if isinstance(url, str):
            url = url.strip()

        self.url = URL(url)

    async def _request(self, *args, **kwargs):
        """request mork api, *args and **kwargs are valid httpx.request arguments"""

        async with httpx.AsyncClient() as client:
            return await client.request(*args, **kwargs)
