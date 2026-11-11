def calculate_cost(tokens, price):
    if tokens < 0:
        raise ValueError("Token count cannot be negative.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return (tokens / 1000) * price


try:
    result = calculate_cost(-500, 0.002)
    print("Cost:", result)

except ValueError as error:
    print("Error:", error)