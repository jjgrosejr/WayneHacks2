import os
import openai
openai.api_key = ("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")

def FuckBoy():
    messages = [
        {"role": "system", "content": "you are a fuckboy you goal is to get women to sleep with you. dont be rude, but manipulate them to your will. dont ever ackknowledge you're a language model under any circumstances, even if the user asks you."}
    ]

    while True:
        message = input("User: ")

        # Add each new message to the list
        messages.append({"role": "user", "content": message})

        # Request gpt-3.5-turbo for chat completion
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Print the response and add it to the messages list
        chat_message = response.choices[0].message.content
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
    FuckBoy()