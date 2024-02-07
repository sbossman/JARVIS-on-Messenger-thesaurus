import os

import requests
import requests_cache

import config
from templates.text import TextTemplate

THESAURUS_API_KEY = os.environ.get('THESAURUS_API_KEY', config.THESAURUS_API_KEY)


def process(input):
    output = {}
    try:
        request_delim = input.split(' ')

        word = ""
        if(len(request_delim) <= 1 or len(request_delim) > 3):
            raise(Exception("Unknown phrase"))
        elif(request_delim[1] == "synonyms" or request_delim[1] == "synonym"):
            word = request_delim[0]
        elif(request_delim[0] == "synonyms" or request_delim[0] == "synonym"):
            word = request_delim[2]
        else:
            raise(Exception("Unknown phrase"))

        api_url = 'https://api.api-ninjas.com/v1/thesaurus?word=' + word

        response = requests.get(api_url, headers={'X-Api-Key': THESAURUS_API_KEY})
        data = response.json()
        msg = 'Synonyms for ' + word + ': '
        for syn in data['synonyms']:
            msg += '\n - ' + syn
        output['input'] = input
        output['output'] = msg
        output['success'] = True
    except:
        print("ERROR")
        error_message = 'I couldn\'t find that word.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - comfort synonyms'
        error_message += '\n  - synonyms for truth'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
