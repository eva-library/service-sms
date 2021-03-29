import os
from twilio.rest import Client
from flask import Flask, request

def sendsms(cuerpo, destinatario):
    try:
        account_sid = "aaaaaaaaaaaaaaaaaaaaaaaa"    #api key
        auth_token = "aaaaaaaaaaaaaaaaaaaaaaaa"     #token

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=cuerpo,
                from_='+99999999',  #sender number
                to=destinatario
            )
        print("MSJ: "+message.sid)
        print("success")
        return ("success")
    except:
        print("fail")
        return ("fail")



