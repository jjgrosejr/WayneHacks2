import openai
from instagrapi import Client

openai.api_key = ("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")

engineeredPrompt = ""

def FuckBot(Client, thread_id):
    messages = [
        {"role": "system", "content": engineeredPrompt}
    ]

    while True:
        message = Client.direct_messages(thread_id, 20)[0].text # add instagram dms

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

recipient = [cl.user_id_from_username(input("enter recipient: "))]

thread_id = cl.direct_send("hello", recipient).thread_id

FuckBot(cl, thread_id)