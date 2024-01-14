import openai
from instagrapi import Client

engineeredPrompt = ""

def FuckBot(Client):
    messages = [
        {"role": "system", "content": engineeredPrompt}
    ]

    while True:
        message = 0 # TODO add instagram dms

        messages.append({"role": "user", "content": message})

        # Request gpt-3.5-turbo for chat completion
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Print the response and add it to the messages list
        chat_message = response.choices[0].message.content
        Client.direct_send(chat_message)
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

username = input("enter username: ")
password = input("enter password: ")

cl = Client()

cl.login(username, password)

recipient = [input("Enter recipient")]

FuckBot(cl)