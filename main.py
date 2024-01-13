import openai
from instagrapi import Client

# openai.my_api_key = 'org-tIGaYoDJjUPeawEvfqE0QUmD'

username = input("enter username: ")
password = input("enter password: ")

while True:
    relogin = input("would you like to save login (1 for yes, 0 for no): ")
    relogin = int(relogin)
    if (relogin >= 0) and (relogin <= 1):
        break
    else:
        print("invalid response, please try again")

cl = Client()
cl.login(username, password)

message = input("Please enter message: ")
recipient = input("Please enter recipient usernaeme: ")

recipid = cl.user_id_from_username(recipient)
 
cl.direct_send(message, recipid)