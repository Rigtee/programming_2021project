import json
import random
import re

with open('intents.json') as file:
    intents = json.load(file)

bot_template = "BOT: {0}"
user_template = "USER: {0}"

responses = {
    'question': [
        "I don't know :(", 'you tell me!'
    ],
    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?',
        'oh wow!',
        ':)'
    ],
    'default': 'default message'
}

rules = {'I want (.*)': ['What would it mean if you got {0}',
                         'Why do you want {0}',
                         "What's stopping you from getting {0}"],
         'do you remember (.*)': ['Did you think I would forget {0}',
                                  "Why haven't you been able to forget {0}",
                                  'What about {0}',
                                  'Yes .. and?'],
         'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
         'if (.*)': ["Do you really think it's likely that {0}",
                     'Do you wish that {0}',
                     'What do you think about {0}',
                     'Really--if {0}']}


def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


def respond(message):
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        response = response.format(phrase)
    return response

def match_rule(rules, message):
    response, phrase = "default", None
    for pattern, responses in rules.items():
        match = re.search(pattern, message)
        if match is not None:
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    return response, phrase

print(match_rule(rules, "do you remember your last birthday"))

def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message

send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")