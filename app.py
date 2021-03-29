import json
import requests
import pymysql
import os
#import logging
import logging.config
import sys
import yaml
import re
from itertools import cycle
#from email_validator import validate_email, EmailNotValidError
from flask import Flask, request, jsonify
from send_sms import sendsms
from update_list_picker_payload import set_up_payload

app = Flask(__name__)

@app.route("/sendsms", methods=["POST"])
def test_functions():
    try:
        request_body = json.loads(request.data)
        print("REQ: "+str(request_body))
        result = {
                    "option": "SMS",
                    "visibleContext":request_body["visibleContext"],
                    "openContext":request_body["openContext"],
                    "hiddenContext":request_body["hiddenContext"]        
        }
        print("REQ: "+str(request_body))
        info = request_body["info"]

        data = {
            'sessionCode': info["sessionCode"],
            'name': request_body["text"]
        }

        print("DATA: "+str(data))

        #asunto = request.json['asunto']
        #body = request.json['body']
        destinatario = request.json['text']
        body = "body de prueba"

        requestService = sendsms(body, destinatario)

        print("BODY: "+body+"; DEST: "+destinatario)
        print(requestService)

    except: 
        logging.exception("Unexpected error parsing payload: %s ", sys.exc_info()[0])
        result = "Error..."

    print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True, port=8002)
