import json
from enum import Enum
from typing import Optional, Union

import requests
from exceptions import (
    AutomagicallyAuthenticationError,
    AutomagicallyError,
    AutomagicallyPermissionError,
    AutomagicallyServicesTransactionLimitError,
    DeserializeException,
)
from response import AutomagicallyResponse
from services.emails import Email, EmailsServiceAPI
from services.sms import Sms, SMSServiceAPI


class AppEnvironmentTypes(Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    LOCAL = "local"


AUTOMAGICALLY_STATUS_CODE_EXCEPTION = {
    429: AutomagicallyServicesTransactionLimitError,
    401: AutomagicallyAuthenticationError,
    403: AutomagicallyPermissionError,
}


class Client:
    def __init__(
        self,
        api_key: str,
        environment_type: str = AppEnvironmentTypes.PRODUCTION.value,
    ):
        self.api_key = api_key
        self._environment_type = environment_type
        # Services
        self._emails = EmailsServiceAPI(client=self)
        self._sms = SMSServiceAPI(client=self)

    @property
    def sms(self) -> SMSServiceAPI:
        return self._sms

    @property
    def emails(self) -> EmailsServiceAPI:
        return self._emails

    @property
    def environment_type(self) -> str:
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        if environment_type not in list(map(str, AppEnvironmentTypes)):
            raise ValueError
        self._environment_type = environment_type

    @property
    def api_url(self) -> str:
        # staging url for now
        return "https://api.automagically.dev/api"

    @property
    def api_version(self) -> str:
        return "v0"

    def request(
        self,
        method: str,
        url: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
    ) -> requests.Response:

        headers = headers or {}

        headers["api-key"] = self.api_key
        headers["Automagically-Environment"] = self.environment_type

        return requests.request(
            method=method, url=url, json=data, params=params, headers=headers
        )

    def do_service_request(
        self,
        method: str,
        service_url: Optional[str] = None,
        data: Optional[Union[dict, Email, Sms]] = None,
        params: Optional[dict] = None,
        url_for_request: Optional[str] = None,
    ) -> AutomagicallyResponse:
        if isinstance(data, (Email, Sms)):
            data = data.get()

        url = url_for_request or f"{self.api_url}/{self.api_version}/{service_url}"
        raw_response = self.request(method=method, url=url, data=data, params=params)
        automagically_response = AutomagicallyResponse(
            content=raw_response.text,
            status_code=raw_response.status_code,
            headers=raw_response.headers,
            url=raw_response.url,
            method=raw_response.request.method,
        )

        if not automagically_response.ok:
            self.raise_automagically_exception(automagically_response)
        return automagically_response

    def raise_automagically_exception(
        self, automagically_response: AutomagicallyResponse
    ) -> None:
        try:
            error_content = json.loads(automagically_response.content)
        except ValueError as error:
            raise DeserializeException(automagically_response.content) from error
        messages = error_content.get("messages")
        error_code = error_content.get("error_code")
        status_code = error_content.get("status_code")
        support_id = error_content.get("support_id")
        self.specify_error(
            messages,
            error_code,
            status_code,
            support_id,
            automagically_response.method,
            automagically_response.url,
        )

    def specify_error(
        self,
        message: str,
        error_code: str,
        status_code: int,
        support_id: str,
        method: Optional[str],
        url: str,
    ) -> None:
        exception = AUTOMAGICALLY_STATUS_CODE_EXCEPTION.get(
            status_code, AutomagicallyError
        )
        raise exception(message, error_code, status_code, support_id, method, url)

    def send_email(self, data: Union[Email, dict]) -> requests.Response:
        if isinstance(data, Email):
            data = data.get()
        return self._emails.send(data)

    def send_sms(self, data: Union[Sms, dict]) -> requests.Response:
        if isinstance(data, Sms):
            data = data.get()
        return self._sms.send(data)
