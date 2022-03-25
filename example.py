import json
import os

import requests
from dotenv import dotenv_values

# from fastapi import FastAPI
# from fastapi.responses import JSONResponse


config = dotenv_values(".env")  # config

# app = FastAPI()

status = dict()

EMAIL_URL = config["AUTOMAGICALLY_ROOT_URL"] + "emails/emails/"
EVENTS_URL = config["AUTOMAGICALLY_ROOT_URL"] + "events/events"
TELEGRAM_URL = f"{config['AUTOMAGICALLY_ROOT_URL']}telegram/bots/automagically_test/send_message?chat_id={config['TELEGRAM_CHAT_ID']}"


def send_email():

    response = requests.get(
        EMAIL_URL, headers={"api-key": config["AUTOMAGICALLY_API_KEY"]}
    )

    status["emails"] = {
        "content": str(response.content),
        "status_code": response.status_code,
    }


def send_telegram_message():

    response = requests.post(
        TELEGRAM_URL,
        data="Hello world 👋".encode("utf-8"),
        headers={
            "api-key": config["AUTOMAGICALLY_API_KEY"],
            "Content-type": "text/plain",
        },
    )

    status["telegram"] = {
        "content": str(response.content),
        "status_code": response.status_code,
    }


def publish_event():

    response = requests.post(
        EVENTS_URL,
        data=json.dumps({"value": "Hello world from my app!", "metric": 42}),
        params={"event_name": "test"},
        headers={
            "api-key": config["AUTOMAGICALLY_API_KEY"],
            "Content-type": "application/json",
        },
    )

    status["events"] = {
        "content": str(response.content),
        "status_code": response.status_code,
    }


# @app.get("/")
# async def root():

#     # Validate API Key

#     send_email()
#     send_telegram_message()
#     publish_event()

#     return JSONResponse(status_code=200, content=status)


if __name__ == "__main__":

    send_email()
    send_telegram_message()
    publish_event()

    print(status)
    # return JSONResponse(status_code=200, content=status)
