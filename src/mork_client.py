import httpx
from httpx import URL
from typing import Optional
import os
from urllib.parse import quote

class MorkClient:
    def __init__(self, url: Optional[str| URL] = os.environ.get("MORK_URL")):
        if url is None:
            raise ValueError(
                "MORK_URL environment variable is not set. Please set it using \
                `export MORK_URL=http://localhost:8000/`."
            )

        if isinstance(url, URL):
            self.url = url
            return

        if isinstance(url, str):
            url = url.strip()

        self.url: URL = URL(url)

    async def _request(self, method: str = "GET", path: str = "", **kwargs):
        """request mork api, *args and **kwargs are valid httpx.request arguments"""

        assert path.startswith("/"), "Path must start with /"

        url = self.url.copy_with(path=path)

        async with httpx.AsyncClient() as client:
            return await client.request(method, url, **kwargs)

    async def _mork_to_path(self, mork_path: str):
        """changes mork code to valid path parameters"""

        lines = mork_path.split('\n')
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line != ""]  # remove empty lines
        path = "/".join(lines)

        return path

    async def busywait(self, timeout: int = 2000):
        await self._request(method="GET", path=f"/busywait/{timeout}")

    async def clear(self, expr: str):
        path = quote(expr.strip())

        return await self._request(
            method="GET",
            path=f"/clear/{path}"
        )

    async def count(self):
        pass

    async def export(self):
        pass

    async def import_(self):
        pass

    async def status(self):
        pass

    async def stop(self):
        return await self._request(
            method="GET",
            path="/stop/",
            params={"wait_for_idle": ""}
        )

    async def upload(self):
        pass

    async def transform(self):
        pass

    async def metta_thread(self):
        pass

    async def metta_thread_suspend(self):
        pass

    async def transform_multi_multi(self):
        pass

