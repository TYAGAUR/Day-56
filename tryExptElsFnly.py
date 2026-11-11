try:
    tokens = int(input("Enter token count: "))

except ValueError:
    print("Please enter a valid integer.")

else:
    print("Token count:", tokens)

finally:
    print("Program execution completed.")