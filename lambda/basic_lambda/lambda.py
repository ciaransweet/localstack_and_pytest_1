import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info("I've been called!")
    return {
        "message": "Hello pytest!"
    }
