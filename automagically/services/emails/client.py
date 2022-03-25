from automagically.services.utils import AutomagicallyServiceAPI


class EmailsServiceAPI(AutomagicallyServiceAPI):
    def __init__(self, client, relative_url="emails/"):
        super().__init__(client, relative_url)
