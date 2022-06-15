from flask import Flask, request, jsonify
from os import getenv
from heyoo import WhatsApp
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

messenger = WhatsApp('EAAUuI61kKewBADnNtmZCEc3SfDyh074JJbEo3JErXFrxniGwDgW1DscXuM0oIR3YhBtAc64ZBzxh75ZAHSMGA0JTNz1WO90XWoMW8ehksEURCZAg7cDOJzRBQtWxZBOYfdIta3Ox6ZBrnMUGs7KyzAnASvI3LZBxLM83WMtzhKSS1BdOC86V1rttXOt1MosOmfNoOgYhsxdNRczlIlbdBo2ErUvzgNCxMEZD', phone_number_id='101780209235905')
VERIFY_TOKEN = "Wesley13"
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
                    recipient_id="263785564315",
                )
        
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"
    return jsonify({"status": "success"}, 200)
    


if __name__ == "__main__":
    app.run(debug=True)