import logging

logger = logging.getLogger(__name__)


class AIRequestService:

    def __init__(self, model_name, price_per_1000_tokens):
        self.model_name = model_name
        self.price_per_1000_tokens = price_per_1000_tokens

    def validate_request(self, tokens):

        if not isinstance(tokens, int):
            raise TypeError("Token count must be an integer.")

        if tokens <= 0:
            raise ValueError("Token count must be greater than zero.")

        if not self.model_name:
            raise ValueError("Model name is required.")

        return True

    def calculate_cost(self, tokens):

        self.validate_request(tokens)

        cost = (
            tokens / 1000
        ) * self.price_per_1000_tokens

        logger.info(
            "Request processed for model %s with %s tokens",
            self.model_name,
            tokens
        )

        return cost

    def process_request(self, tokens):

        try:
            cost = self.calculate_cost(tokens)

            return {
                "status": "success",
                "model": self.model_name,
                "tokens": tokens,
                "estimated_cost": round(cost, 5)
            }

        except (TypeError, ValueError):
            logger.exception("AI request validation failed")
            raise