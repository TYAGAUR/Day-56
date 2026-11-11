model = {
    "name": "GPT",
    "provider": "OpenAI"
}

try:
    print(model["version"])

except KeyError:
    print("Version information is unavailable.")