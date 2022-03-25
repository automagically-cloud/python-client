import json
from typing import Optional

from requests.structures import CaseInsensitiveDict

from automagically.automagically_exceptions import DeserializeException


class AutomagicallyResponse(object):
    def __init__(
        self,
        content: str,
        status_code: int,
        url: str,
        method: Optional[str],
        headers: CaseInsensitiveDict,
    ):
        self.content = content
        self.status_code = status_code
        self.headers = headers
        self.url = url
        self.method = method
        self._json = None

    @property
    def ok(self) -> bool:
        return not (self.status_code < 200 or self.status_code >= 400)

    @property
    def json(self) -> Optional[dict]:
        if self._json is not None:
            return self._json

        try:
            json_content = json.loads(self.content)
        except ValueError as error:
            raise DeserializeException(self.content) from error
        self._json = json_content

        return self._json


class PageResponse(AutomagicallyResponse):
    def __init__(
        self,
        content: str,
        status_code: int,
        url: str,
        method: Optional[str],
        headers: CaseInsensitiveDict,
    ):
        super().__init__(content, status_code, url, method, headers)

    @property
    def next(self):
        return self._json.get("next")

    @property
    def previous(self):
        return self._json.get("previous")

    @property
    def count(self):
        return self._json.get("count")

    @property
    def results(self):
        return self._json.get("results")
