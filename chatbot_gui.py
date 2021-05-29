import nltk  # Natural Language Toolkit that is used to work with human language data
from nltk.stem import WordNetLemmatizer  # lemmatization is used to group words together based on similarity (variants)
import pandas as pd # Used to create dataframes
import datetime
import pickle  # used to save a Python object in a binary format (serializing and de-serializing)
import numpy as np
from keras.models import load_model  # Keras is an open-source deep learning API
import json  # used to store text files in an easy-to-read (for humans) and widely-used format
import random  # will be used to choose among options to make the chatbot more natural
from tkinter import * # to create the bot GUI

lemmatizer = WordNetLemmatizer()

chatbot_model = load_model('chatbot_model.h5') # this will load our model generated in machine-language

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def lemmatize_sentence(sentence):
    words_lem = nltk.word_tokenize(sentence)
    words_lem = [lemmatizer.lemmatize(word.lower()) for word in words_lem]
    return words_lem


# This will return a bag of words in form of an array that can be equal to 0 (not present in the sentence) or to 1 (word present)
def bagofwords(sentence, words, show_details=True):
    # First we will tokenize the sentence to separate the words
    words_lem = lemmatize_sentence(sentence)
    bow = [0] * len(words)
    for s in words_lem:
        for i, w in enumerate(words): # where is the index and w the word
            if s == w:
                # we assign one if the word is contained in our vocabulary
                bow[i] = 1
                if show_details: # variable used to check which word was found in the bow
                    print("Word found in the bow: {}".format(w))
    return (np.array(bow))

# This function will calculate probabilities for each intent,
# the chatbot will select the highest to provide an appropriate answer to the user
"""def predict_class(sentence, model):
    # We arbitrarily define an error threshold and select the words that are above it
    bow = bagofwords(sentence, words, show_details=False)
    prediction = model.predict(np.array([bow]))[0]
    threshold = 0.25
    for i, j in enumerate(prediction): # What comes out our model generated with Keras
        if j > threshold: # filters words
            results = [i, j] # creates an array with all the predictions
    # Now we will sort those arrays by decreasing probability
    results.sort(key=lambda x: x[1], reverse=True)
    results_list = []
    for i in results:
        results_list.append({"Intent": classes[i[0]], "Probability": str(i[1])})
        # appends every class from the pickle file and its corresponding probability
    return results_list"""

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bagofwords(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.05
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def create_response(ints, intents_json): # Output is an intent coming from the JSON file
    tag = ints[0]['intent'] #returns the tag from the JSON file
    intents_list = intents_json['intents']
    for i in intents_list:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            # if the tag is present in our file, then the response will be selected randomly based on what is in the JSON file
            break
    return result


def bot_response(message):
    ints = predict_class(message, chatbot_model) # determines the intent of the message
    response = create_response(ints, intents) # finds accordingly a bot response
    return response

# Main function to allow the user to interact with the bot (send a message)
def send():
    message = entryBox.get("1.0", 'end-1c').strip()
    entryBox.delete("0.0", END)

    if message != '': # if the user has typed a message (not empty)
        chatLog.config(state=NORMAL)
        chatLog.insert(END, "USER: " + message + '\n\n') # Text box for the user: prints the message he typed
        chatLog.config(foreground="#442265", font=("Verdana", 12))

        response = bot_response(message)
        chatLog.insert(END, "BOT: " + response + '\n\n') # Text box for the bot: prints the corresponding response

        chatLog.config(state=DISABLED)
        chatLog.yview(END) # End of the conversation


base = Tk()
base.title("UNIL HEC Bot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# This will create the graphical interface for the chat window
chatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")

chatLog.config(state=DISABLED)

# This will bind the scrollbar to the chat window
scrollBar = Scrollbar(base, command=chatLog.yview, cursor="heart")
chatLog['yscrollcommand'] = scrollBar.set

# This button will send the message to the program, to which the bot will respond
sendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=send) # it activates the main function of our program, the 'send' function.

# This will create a box to allow the user typing his message
entryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
# entryBox.bind("<Return>", send)


# Let's now place all components of the GUI on the screen
scrollBar.place(x=376, y=6, height=386)
chatLog.place(x=6, y=6, height=386, width=370)
entryBox.place(x=128, y=401, height=90, width=265)
sendButton.place(x=6, y=401, height=90)

# This will run the chatbot
base.mainloop()
