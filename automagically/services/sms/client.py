from automagically.services.utils import AutomagicallyServiceAPI


class SMSServiceAPI(AutomagicallyServiceAPI):
    def __init__(self, client, relative_url="sms/"):
        super().__init__(client, relative_url)
