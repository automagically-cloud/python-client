# 🔥  Automagically  Python Client

[![PyPi](https://img.shields.io/pypi/v/automagically.svg)](https://pypi.python.org/pypi/automagically)
[![PyPi](https://img.shields.io/pypi/pyversions/automagically)](https://pypi.python.org/pypi/automagically)
[![ReadTheDocs](https://readthedocs.org/projects/automagically/badge/?version=latest)](https://automagically.readthedocs.io/en/latest/?version=latest)
[![Gitter](https://badges.gitter.im/binaryai/community.svg)](https://gitter.im/automagically-hq/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## Introduction

Automagically is Foundation as a Service. We work at your finger tips to provide you with the management tools, APIs and SDKs to build software.

## Get started

### Installation

```shell
pip install automagically

export AUTOMAGICALLY_API_KEY=....
```

### Code

```python
from automagically import Client
from automagically.types import Email

# We are reading the Environment variable AUTOMAGICALLY_API_KEY
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

    automagically.publish_event("test_event", {
        "value": "Hello from example app 👋",
        "sense_of_life": 42
    })

```

You find more examples in the `/examples` folder.

## Documentation

WIP

## Get your API key

Apply for early access at <https://automagically.cloud>.
