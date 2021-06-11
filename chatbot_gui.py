import nltk # Natural Language Toolkit that is used to work with human language data
from nltk.stem import WordNetLemmatizer  # lemmatization is used to group words together based on similarity (variants)
import pandas as pd # Used to create dataframes
from datetime import datetime
import pickle  # used to save a Python object in a binary format (serializing and de-serializing)
import numpy as np
from keras.models import load_model  # Keras is an open-source deep learning API
import json  # used to store text files in an easy-to-read (for humans) and widely-used format
import random  # will be used to choose among options to make the chatbot more natural
from tkinter import * # to create the bot GUI
import webbrowser # To open pages on a browser
from courses import *
import distutils.util


        
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()

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

def getLink(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['context'])
            break
    return result

def bot_response(message):
    ints = predict_class(message, chatbot_model) # determines the intent of the message
    response = create_response(ints, intents) # finds accordingly a bot response
    return response

def bot_response_link(message):
    ints = predict_class(message, chatbot_model)
    res = getLink(ints, intents)
    return res

# Shorter version of webbrowser.open_new() function. It allows to open links in a browser

def callback(url):

    webbrowser.open_new(url)
    
state = 0

# Main function to allow the user to interact with the bot (send a message)
def send():
    message = entryBox.get("1.0", 'end-1c').strip()
    entryBox.delete("0.0", END)

    if message != '': # if the user has typed a message that is not empty
        global state
        print(state)
        chatLog.config(state=NORMAL)

        # Send the first message to the chatbot with the message from the user

        chatLog.insert(END, "USER: " + message + '\n\n') # Text box for the user: prints the message he typed
        chatLog.config(foreground="#442265", font=("Verdana", 12))

        # Using the message, analyzed it and then pick an answer attributed ot response

        if state == 0:
            if message == 'help':
                response = "I'm a versatile bot, I could do many things for you like:" \
                           "\n - Searching in the database of HEC courses" \
                           "\n - Finding a professor among the faculty" \
                           "\n - Giving you information about student housing" \
                           "\n - Describing the process to get a visa for Switzerland" \
                           "\n - ..." \
                           "\n The importance is to be clear about the thing you're looking for! If you do so, my robot neural net will be able" \
                           " to process information more efficiently to provide you with an accurate answer. What can I do for you now?"
                chatLog.insert(END, "BOT: " + response + '\n\n')
            else:
                response = bot_response(message)
                
                try:
                    
                    df = pd.read_csv('log_chatbox.txt')
                    
                except FileNotFoundError:
                    
                    df = pd.DataFrame(columns=['Input', 'Output','Time','Date', 'Intents_predicted','Status','Language']) 
                
                reptest = predict_class(message, chatbot_model)
                
                new_row = {'Input': message,  'Output': response,'Time':datetime.time(datetime.now()),'Date':datetime.date(datetime.now()), 'Intents_predicted': reptest[0]['intent'],'Probability prediction':reptest[0]['probability'], 'Status':'Student', 'Language':'EN'}
                #append row to the dataframe
                df = df.append(new_row, ignore_index=True)
                # Save the CSV file with the new line
                df.to_csv('log_chatbox.txt',index=False)
                
                chatLog.insert(END, "BOT: " + response + '\n\n')
                
                """ras = bot_response_link(message)
                
                if ras:
                    callback(ras)
                    ChatLog.insert(END, "Bot: " + ras + '\n\n')"""   
                    
                course_response = intents["intents"][8]["responses"][0]  # last 0 needed to isolate element of list "responses", otherwise prints with []
                professor_response = intents["intents"][9]["responses"][0]
                if response == course_response:
                    ask_search = "Type '1' to search by keyword and '2' by filters."
                    chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                    state = 1
                    print(state)

                elif response == professor_response:
                    ask_search = "The search is made to match last names in any position of the word. " \
                                 "\nEnter a keyword to find professors:"
                    chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                    state = 2
                    print(state)


        elif state == 1:
            if message == '1':
                ask_search = "Enter a keyword to find courses:"
                chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                state = 11
                print(state)
            elif message == '2':
                ask_search = "Here you can filter courses based on parameters, mainly the number of credits or " \
                             "the quantitative scale (HQ, SQ or NQ for high, semi or no quantitative respectively). "
                chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                ask_credits = "Enter the number of credits and the quantitative scale with a space between them " \
                              "(e.g. for 3 credits and highly quantitative, enter '3 HQ'):"
                chatLog.insert(END, "BOT: " + ask_credits + '\n\n')
                state = 13
                print(state)
            else:
                print(state)
                bad_input = "Sorry, I did not understand. Please try again by entering '1' for keyword and '2' for filters."
                chatLog.insert(END, "BOT: " + bad_input + '\n\n')

        elif state == 11:
            keyword_course = {"course_name": message}
            output = search_course_name(keyword_course)
            if output:
                keyword_found = "Information about the keyword found:"
                chatLog.insert(END, "BOT: " + keyword_found + '\n')
                for i in range(len(output)):
                    chatLog.insert(END, output[i] + '\n')
                ask_search = "Would you like to search for another course?"
                chatLog.insert(END, "BOT: " + ask_search + '\n\n')
            else:
                bad_output = "No course was found based on your keyword. Would you like to search for another course?"
                chatLog.insert(END, "BOT: " + bad_output + '\n\n')
            state = 14

        elif state == 13:
            input_message = message.split()
            information = {}
            information["course_credits"] = input_message[0]
            information["course_quantitative"] = input_message[1]
            output = search_information(information)
            if output:
                filter_found = 'Courses with your filters: ' + information["course_credits"] + " " + information["course_quantitative"]
                chatLog.insert(END, "BOT: " + filter_found + '\n')
                for i in range(len(output)):
                    chatLog.insert(END, output[i] + '\n')
                ask_search = "Would you like to search for another course?"
                chatLog.insert(END, "BOT: " + ask_search + '\n\n')
            else:
                bad_output = "No course was found based on your keyword. Would you like to search for another course?"
                chatLog.insert(END, "BOT: " + bad_output + '\n\n')
            state = 14

        elif state == 14:
            try:
                new_search = bool(distutils.util.strtobool(message))
                if new_search:
                    ask_search = "Type '1' to search by keyword and '2' by filters."
                    chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                    state = 1
                    print(state)
                else:
                    ask_continue = "What can I do for you now?"
                    chatLog.insert(END, "BOT: " + ask_continue + '\n\n')
                    state = 0
                    print(state)
            except ValueError:
                bad_input = "Sorry, I didn't understand that. Would you like to search for other courses (y/n) ?"
                chatLog.insert(END, "BOT: " + bad_input + '\n\n')

        elif state == 2:
            print(state)
            keyword_professor = {"course_professor": message}
            output = search_professor_name(keyword_professor)
            print(type(output))
            if output:
                keyword_found = "Information about the keyword found: "
                chatLog.insert(END, "BOT: " + keyword_found + '\n')
                for i in range(len(output)):
                    chatLog.insert(END, output[i] + '\n')
                ask_search = "Would you like to search for another professor?"
                chatLog.insert(END, "BOT: " + output + '\n'+ ask_search + '\n\n')
            else:
                bad_output = "No course was found based on your keyword. Would you like to search for another course?"
                chatLog.insert(END, "BOT: " + bad_output + '\n\n')
            state = 21


        elif state == 21:
            try:
                new_search = bool(distutils.util.strtobool(message))
                print(new_search)
                if new_search:
                    ask_search = "Enter a keyword to find professors:"
                    chatLog.insert(END, "BOT: " + ask_search + '\n\n')
                    state = 2
                else:
                    ask_continue = "What can I do for you now?"
                    chatLog.insert(END, "BOT: " + ask_continue + '\n\n')
                    state = 0
            except ValueError:
                bad_input = "Sorry, I didn't understand that. Would you like to search for other courses (y/n) ?"
                chatLog.insert(END, "BOT: " + bad_input + '\n\n')

        chatLog.config(state=DISABLED)
        chatLog.yview(END)  # End of the conversation


base = Tk()
base.title("UNIL HEC Bot")
base.geometry("600x600")
base.resizable(width=FALSE, height=FALSE)

# This will create the graphical interface for the chat window

chatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap=WORD)
welcome_message = "Hello and welcome fellow student! Beep-boop-bop, I'm a bot serving the HEC faculty of the University of Lausanne. " \
                  "Kind and clever, I could be useful too. Ask me anything you want about student life: courses, professors," \
                  " directions, food... \nType 'help' anytime in the entry box to find a list of the things I can do!"
chatLog.insert(END, "BOT: " + welcome_message + '\n\n')

chatLog.config(state=DISABLED)

# This will bind the scrollbar to the chat window

scrollBar = Scrollbar(base, command=chatLog.yview, cursor="double_arrow")
chatLog['yscrollcommand'] = scrollBar.set

# This button will send the message to the program, to which the bot will respond

sendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=send) # it activates the main function of our program, the 'send' function.

# This will create a box to allow the user typing his message

entryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

# entryBox.bind("<Return>", send)


# Let's now place all components of the GUI on the screen

scrollBar.place(x=550, y=6, height=486)
chatLog.place(x=6, y=6, height=486, width=500)
entryBox.place(x=128, y=501, height=90, width=400)
sendButton.place(x=6, y=501, height=90)

# This will run the chatbot
base.mainloop()
