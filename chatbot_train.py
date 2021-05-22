# To have details on the packages used, please refer to the chatbot_gui.py file
import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

lemmatizer = WordNetLemmatizer()
# This is a pre-trained tokenizer for English that divides the text into a list of sentences
# by using an unsupervised algorithm to build a model for abbreviation
# words, collocations, and words that start sentences.
nltk.download('punkt')

# This is a corpus reader from the NLTK package
nltk.download('wordnet')

words = []
classes = []
documents = []
bad_characters = ['?', '!']  # characters to be avoided for training the model
data = open('intents.json').read() # test_json/
intents = json.loads(data)

for ints in intents['intents']:
    for pat in ints['patterns']:

        # NLTK function to tokenize each word
        word = nltk.word_tokenize(pat)
        words.extend(word)
        # Add the documents to our documents list
        documents.append((word, ints['tag']))

        # Add the classes to our class list
        if ints['tag'] not in classes:  # adds everything that is new
            classes.append(ints['tag'])

#words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in bad_characters] #cancel plural and so on. Works with words, not list


words_clean = []

for word in words:
    if word not in bad_characters:  # to avoid taking unwanted characters
        words_clean.append(lemmatizer.lemmatize(word.lower()))

words = sorted(list(set(words_clean)))  # restores the variable in a sorted list of words. Delete duplicates

classes = sorted(list(set(classes)))  # same for classes

# Those print statements are used as a sanity check to get an overview on the model
print(len(documents), "Documents")
print(len(classes), "Classes", classes)
print(len(words), "Unique lemmatized words", words)

# Pickle dump function takes the object to pickle and the file to which the object has to be saved
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Let's start training our model by initializing training data
training_data = []
output_empty = [0] * len(classes)  # creates an empty dataframe that will be filled later
for doc in documents:
    # Initializes the bag of words as a list
    bow = []
    # List of tokenized words for the pattern
    pattern_words = doc[0]
    # Lemmatize each word, i.e creating the base word to which all related words will be linked
    #for word in pattern_words:
    #    pattern_words = lemmatizer.lemmatize(word.lower())
    #for word in words:
    #    bow.append(1) if word in pattern_words else bow.append(0)  # check for every words of the dictionary. Else 0

    #for word in pattern_words:
    #    pattern_words.append(lemmatizer.lemmatize(word.lower()))
    # We create our bag of words array like before: value if 1 if we match  the word found in current pattern
    for word in words:
        if word in pattern_words:
            bow.append(1)
        else:
            bow.append(0)

    # The output for each pattern is a 0 for each tag and 1 for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    # This constitutes our training data
    training_data.append([bow, output_row])

# Now we will shuffle our features and turn them into a Numpy array (easier to analyze)
random.shuffle(training_data)
training_data = np.array(training_data,dtype=object)

# As usual, we create train and test lists with X as patterns and Y as intents

train_X = list(training_data[:, 0])
train_Y = list(training_data[:, 1])
print("Training data successfully created")

# Creating model, we chose a 3-layer model (common)
# The first layer 128 neurons, the second layer has 64 neurons while the third layer (output)
# contains a number of neurons equal to the number of intents to predict output (softmax activation)

model = Sequential()
model.add(Dense(128, input_shape=(len(train_X[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_Y[0]), activation='softmax'))

# Compilation of the model
# A stochastic gradient descent with the Nesterov accelerated gradient gives good results for this model,
# therefore we decided to use it

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fitting and saving of the model

hist = model.fit(np.array(train_X), np.array(train_Y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)

print("Model successfully created")