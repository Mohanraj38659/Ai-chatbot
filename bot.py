import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?"]
}

def chatbot_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return random.choice(responses["default"])
