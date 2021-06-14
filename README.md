# Project for the Programming class at HEC Lausanne (Spring Semester 2021)

This project aims at implementing a chatbot system that is able to interact with incoming and current students enrolled at the University of Lausanne (UNIL). The chatbot is helping students by guiding them through the choice of courses, the university buildings (map), the office hours...

Functions of the chatbot include:
* Giving information about courses for bachelor/master/PhD students in a database in which students can find a course based on multiple criteria


Content of the folder:

* chatbot_train.py Program used to build the model
* chatbot_gui.py  Main file where the chtabot can be launched
* chatbot_model.h5 Model buildt using chatbot_train.py. The file will be used in chatbot_gui.py
* classes.pkl datafile built using chatbot_train.py. It will be used to predict answer
* courses.py python module with different functions used to answer questions related to classes and teachers
* intents.json file with answers, questions, websites for different subjects. The file will be needed to train the model in chatbot_train.py
* json_modification.py program allowing the user to modify the json file intents.json
* log_chatbox.txt chatbot logs created with the send() function in the program chatbot_gui.py
* programmeshec.db database with class and teacher information
