from __future__ import annotations

import json
from urllib import request


class Response:
    """Simplified HTTP response."""

    def __init__(self, resp: request.addinfourl) -> None:
        self.status_code = resp.getcode()
        self._data = resp.read()

    def json(self) -> dict:
        return json.loads(self._data.decode())

    @property
    def text(self) -> str:
        return self._data.decode()


class Session:
    """Lightweight HTTP session built on :mod:`urllib`."""

    def __init__(self) -> None:
        self.headers: dict[str, str] = {}

    def _request(
        self,
        method: str,
        url: str,
        data: bytes | None = None,
        files: dict | None = None,
    ) -> Response:
        if files:
            # simple multipart form-data for single file
            key, fp = next(iter(files.items()))
            boundary = "----WXDIBoundary"
            body = (
                (
                    f"--{boundary}\r\n"
                    f'Content-Disposition: form-data; name="{key}"; filename="{getattr(fp, "name", "file")}"\r\n\r\n'
                ).encode()
                + fp.read()
                + f"\r\n--{boundary}--\r\n".encode()
            )
            headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
            req = request.Request(
                url, data=body, method=method, headers={**self.headers, **headers}
            )
        else:
            req = request.Request(url, data=data, method=method, headers=self.headers)
        resp = request.urlopen(req)
        return Response(resp)

    def get(self, url: str) -> Response:
        return self._request("GET", url)

    def post(
        self, url: str, json: dict | None = None, files: dict | None = None
    ) -> Response:
        if json is not None:
            body = json.dumps(json).encode()
            headers = {"Content-Type": "application/json"}
            req = request.Request(
                url, data=body, method="POST", headers={**self.headers, **headers}
            )
            resp = request.urlopen(req)
            return Response(resp)
        return self._request("POST", url, files=files)

    def patch(self, url: str, json: dict | None = None) -> Response:
        data = None
        headers = {}
        if json is not None:
            data = json.dumps(json).encode()
            headers["Content-Type"] = "application/json"
        req = request.Request(
            url, data=data, method="PATCH", headers={**self.headers, **headers}
        )
        resp = request.urlopen(req)
        return Response(resp)
