import logging

logging.basicConfig(level=logging.INFO)

try:
    tokens = int("invalid")

except ValueError:
    logging.exception("Token conversion failed")