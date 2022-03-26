# Usage

To use Automagically in a project

## Passing the API Key

### Via .env file

```text
AUTOMAGICALLY_API_KEY=123
```

### Via environment

```shell
export AUTOMAGICALLY_API_KEY=123
```

### As Argument to client

```python
from automagically import Client
from automagically.types import Email


automagically = Client(logging=True)


if __name__ == "__main__":

    email = Email(
        from_email= "hey@automagically.cloud",
        to= ["hey@automagically.cloud"],
        subject="Hello world",
        body="Hello from example app 👋"
    )

    automagically.send_email(email)
    automagically.send_telegram_message("Hello from example app 👋")
    automagically.publish_event("test", {"value": "Hello from example app 👋", "sense_of_life": 42})



```
