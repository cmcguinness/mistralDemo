# Simple Mistral.ai Demo

This Python app implements a simple chatbot using Mistral's hosted models.

Mistral obviously also allows you to download their models and run them locally.
This is not intended for that.

You will need an API key from Mistral to run the demo.  You can
get one [here](https://mistral.ai/).

You'll note that this does not use the Mistral Python library.  There are a couple of reasons for that:

1. The library doesn't really do that much, and
2. I think it's beneficial to see exactly what's going over the wire

For that reason, I used the generic Requests library to make calls to Mistral.