import logging

from ai_service import AIRequestService


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


service = AIRequestService(
    model_name="GPT",
    price_per_1000_tokens=0.002
)


try:

    tokens = int(input("Enter token count: "))

    response = service.process_request(tokens)

    print("\nAI Request Response")
    print("-------------------")

    for key, value in response.items():
        print(f"{key}: {value}")


except ValueError as error:

    print("Validation Error:", error)

except TypeError as error:

    print("Type Error:", error)

except Exception:

    logging.exception("Unexpected application error")
    print("An unexpected error occurred.")