import modules
import modules.tests.test_thesaurus as test_thesaurus
import modules.src.thesaurus as thesaurus
"""
import json
import os

# import requests
# from flask import Flask, request

import config
import modules

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', config.VERIFY_TOKEN)

app = Flask(__name__)


@app.route('/')
def about():
    return 'Just A Rather Very Intelligent System, now on Messenger!'


@app.route('/process/')
def process():
    return json.dumps(modules.process_query(request.args.get('q')))


@app.route('/search/')
def search():
    return json.dumps(modules.search(request.args.get('q')))


@app.route('/webhook/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True)
        messaging_events = data['entry'][0]['messaging']
        for event in messaging_events:
            sender = event['sender']['id']
            message = None
            if 'message' in event and 'text' in event['message']:
                if 'quick_reply' in event['message'] and 'payload' in event['message']['quick_reply']:
                    quick_reply_payload = event['message']['quick_reply']['payload']
                    message = modules.search(quick_reply_payload, sender=sender, postback=True)
                else:
                    text = event['message']['text']
                    message = modules.search(text, sender=sender)
            if 'postback' in event and 'payload' in event['postback']:
                postback_payload = event['postback']['payload']
                message = modules.search(postback_payload, sender=sender, postback=True)
            if message is not None:
                payload = {
                    'recipient': {
                        'id': sender
                    },
                    'message': message
                }
                r = requests.post('https://graph.facebook.com/v2.6/me/messages', params={'access_token': ACCESS_TOKEN},
                                  json=payload)
        return ''  # 200 OK
    elif request.method == 'GET':  # Verification
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Error, wrong validation token'
"""
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
"""
if __name__ == '__main__':
    print("Hello world!")
    test_thesaurus.test_thesaurus()

    user_input = input("Hello, I'm JARVIS, Just A Rather Very Intelligent System! How can I help you?\n")
    while(True):
        if(user_input == "Hello"):
            print("Hello")
        elif(user_input == "Goodbye" or user_input == "goodbye" or user_input == "bye" or user_input == "exit"):
            break
        else:
            output = thesaurus.process(user_input)
            if(output['success'] == False):
                print(output['error_msg'])
            else:
                print(output['output'])
        user_input = input("Is there anything else you would like?\n")



