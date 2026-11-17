import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("AI application started")
logging.warning("API response is taking longer than expected")
logging.error("Model request failed")