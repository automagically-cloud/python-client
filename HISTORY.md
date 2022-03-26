# History

## 0.1.1 (2022-03-25)

* First release on PyPI.

## 0.1.2 (2022-03-26)

* Usage of `api_key` possible via `.env File` or existing environment variable set as `AUTOMAGICALLY_API_KEY`
* Usage of `api_key` possible via `Client(<api_key>)`
* Sending email: `client.send_email(Email object)` can send an email
* Sending to a Telegram chat: `client.send_telegram_message(message)` can send a Telegram message
* Publishing an event: `client.publish_event(event_name, dict)` can publish an event

## 0.1.3 (2022-03-31)

*
