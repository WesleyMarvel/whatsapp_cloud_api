from flask import Flask, request, jsonify
from os import getenv
from heyoo import WhatsApp
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

messenger = WhatsApp('', phone_number_id='')
VERIFY_TOKEN = ""
load_dotenv()
@app.route('/hook', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        enter = request.get_json()
        trimmed = enter['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        print(trimmed)

        if "hi" == trimmed.lower():
            messenger.send_message(
                    message="Hello Wesley",
                    recipient_id="263XXXXXXX5",
                )
        
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"
    return jsonify({"status": "success"}, 200)
    


if __name__ == "__main__":
    app.run(debug=True)
