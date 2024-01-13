import openai
import tkinter as tk
from instagrapi import Client
from instagrapi import DirectMixin

openai.my_api_key = 'org-tIGaYoDJjUPeawEvfqE0QUmD'

#username = input("enter username: ")
#password = input("enter password: ")

username = "hoebottest"
password = "Homie-144"

cl = Client()
cl.login(username, password)

message = input("please enter message: ")

numRecipients = input("how many recipients would you like to message: ")

list = []
for i in range(int(numRecipients)):
    recipient = input("Please enter recipient username: ")
    list.append(cl.user_id_from_username(recipient))

cl.direct_send(message, list)

""" messageList = cl.direct_messages(cl.direct_thread_by_participants(list))

print(messageList[0])
 """