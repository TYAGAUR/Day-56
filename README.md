# AI Request Cost Estimator

## What is this project?

This is a small Python project that estimates the cost of an AI request from
the number of tokens it uses. A **token** is a small piece of text that an AI
model reads or writes. It might be a whole word, part of a word, or punctuation.

This project is for learning: it does **not** connect to an AI model or send
anything over the internet. It uses a sample model name and price to practise
calculating costs, checking input, and handling errors.

## How to run it

You need Python installed. Open a terminal in this folder and run:

```bash
python main.py
```

When asked, enter a positive whole number for the token count. For example:

```text
Enter token count: 1500

AI Request Response
-------------------
status: success
model: GPT
tokens: 1500
estimated_cost: 0.003
```

The example uses a price of `0.002` per 1,000 tokens, so 1,500 tokens cost
`1.5 * 0.002 = 0.003` in the project's chosen price units. This is only an
example estimate, not a live price quote.

## How the code works

### `main.py`

This is the program's starting point. It:

1. Sets up a log file called `app.log` to record useful information and errors.
2. Creates an `AIRequestService` with a sample model name and price.
3. Asks you to enter a token count and turns your answer into an integer
   (a whole number).
4. Asks the service to process the count and prints the result.
5. Shows friendly messages for common input errors. Unexpected errors are
   written to the log.

### `ai_service.py`

This file contains the `AIRequestService` class, which groups related work
together:

- `validate_request` checks that the token count is a whole number greater
  than zero and that a model name was provided.
- `calculate_cost` applies the price formula:

  ```text
  cost = (tokens / 1000) * price per 1000 tokens
  ```

- `process_request` calls the calculation and returns the result as a
  dictionary (a collection of named values). If the input is invalid, it logs
  the validation error and passes the error back to `main.py`.

## A few Python ideas used here

- **Imports** let one file use code defined in another file.
- A **class** is a template for an object; here it keeps the model and price
  together with the actions that use them.
- **Exceptions** are errors that the program can catch and handle.
- **Logging** records events in `app.log`, which can help explain what happened
  if something goes wrong.

## Project files

- `main.py` — asks for input and displays the result.
- `ai_service.py` — validates the input and estimates the cost.
- `log_examples.py` — a separate example showing logging levels.
- `app.log` — created when the program runs; stores log messages.
