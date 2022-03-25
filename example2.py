from fastapi import FastAPI, Response, status

from automagically.client import Client
from automagically.services.emails.helpers.email import Email

app = FastAPI()

automagically = Client(api_key="8ARkhpC6EVv7zeETmJnAZOuxBwJaB1HYt9sYUbZ_aZ4")


@app.get("/", status_code=status.HTTP_200_OK)
async def basic_test(response: Response):

    email = Email(
        from_email="me@jensneuhaus.de",
        to=["me@jensneuhaus.de"],
        text="Hello world",
        subject="Hello world",
    )

    email = automagically.send_email(email)

    return {"hello": "world", "email": email}

    # automagically.automagically_exceptions.AutomagicallyAuthenticationError:
    # (['User is inactive'], ['user_inactive'], 401, '0afbb99bfe', 'POST',
    # 'http://api.automagically.dev/api/v0/emails/')
    # automagically.automagically_exceptions.AutomagicallyError:
    # (None, None, None, None, 'POST', 'http://api.automagically.dev/api/v0/emails/')
    # automagically.automagically_exceptions.AutomagicallyAuthenticationError:
    # (['The provided api_key is incorrect'], ['authentication_failed'], 401, '308cb5da20', 'POST',
    # 'http://api.automagically.dev/api/v0/emails/')
