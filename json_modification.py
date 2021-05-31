import json

# Open the json file

with open('test_json\1intents.json') as f:
    intents = json.loads(f.read())
    
# Creation of a class with all the modifications needed for the program
    
class json_mod:
    
    #initialization
    
    def __init__(self,jsonimp):
        
        self.jsonimp = jsonimp
        
    # Print a specific topic
        
    def line(self,i):
        
        jsonimp = self.jsonimp
        
        # Attributing data coming from a specific topic/tag
        
        jtag = jsonimp['intents'][i]["tag"]
        jpatterns = jsonimp['intents'][i]["patterns"]
        jresponses = jsonimp['intents'][i]["responses"]
        
        print('Tag: ',jtag ,'\nPatterns: ', jpatterns,'\nResponse: ', jresponses)
        
        # Only print the website part when information is available
        
        if jsonimp['intents'][i]["context"]:
            
            jwebsite = jsonimp['intents'][i]["context"]
            print('Website: ',jwebsite)
            
    # Search a line for a specific topic using its name, then use the function line to print the content
            
    def line_search(self,name):
        
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            # Search a matching tag. If something is found, use the function line to print the result
            
            if jsonimp['intents'][j]["tag"]==name:
                
                print("\nTopics %s" %(j+1), '"%s":\n' %(name))
                self.line(j)
                
    # Search for a topic and then give the position in the json file  
                
    def line_search_raw(self,name):
    
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            if jsonimp['intents'][j]["tag"]==name:
                
                return j
            
    # Delete a topic using a specific position in the json file
            
    def delete_line(self,i):
        
        jsonimp = self.jsonimp
        
        del jsonimp['intents'][i]
        
        self.jsonimp = jsonimp
        
    # Modified version of the previous definition where you are looking for a specific topic name
        
    def delete_search(self,name):
        
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            if jsonimp['intents'][j]["tag"]==name:
                
                # The previous function is then used
                
                self.delete_line(j)
                
    # Catch the raw content of a specific location
                
    def catch(self,i):
        
        jsonimp = self.jsonimp
        
        values = []
        
        values.append(jsonimp['intents'][i]["tag"])
        values.append(jsonimp['intents'][i]["patterns"])
        values.append(jsonimp['intents'][i]["responses"])
        values.append(jsonimp['intents'][i]["context"])
        
        return values
    
    # Add a new topic with relavant data within    
    
    def add_line(self,ta,pat,res,web=""):
        
        jsonimp = self.jsonimp
        
        # The topic name is a string
        
        if type(pat)==str:
            
            patlist=[]
            patlist.append(pat)
            
        # The patterns of questions and answers are lists because several sentences might be available
            
        elif type(pat)==list:
            
            patlist=pat
            
        if type(res)==str:
            
            reslist=[]
            reslist.append(res)
            
        elif type(res)==list:
            
            reslist=res

        if type(web)==str:
            
            weblist=[]
            weblist.append(web)
            
        # The default value for web is nothing
            
        elif type(web)==list:
            
            weblist=web
            
        dico = {"tag" : ta, "patterns": patlist, "responses": reslist, "context": weblist}
        
        # The new topic is append
        
        jsonimp['intents'].append(dico)
        
        self.jsonimp = jsonimp
        
    # Allow modifications of a current topic. New values must be input
        
    def change_line(self,i,ta,pat,res,web=""):
        
        jsonimp = self.jsonimp
        
        jsonimp['intents'][i]["tag"] = ta
        jsonimp['intents'][i]["patterns"] = pat
        jsonimp['intents'][i]["responses"] = res
        jsonimp['intents'][i]["context"] = web
        
        self.jsonimp = jsonimp
        
    # Save the (modified) json file 
        
    def safe(self):
        
        jsonimp = self.jsonimp
        
        with open('test_json\intents2.json', 'w') as f:
                json.dump(jsonimp, f)
                
    # Specific way of writing the content of the class
            
    def __str__(self):
        
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            print("\nTopics %s:\n" %(j+1))
            self.line(j)
            
        # Specific functions are used to print the result. Nothing is thus "returned"
        
        return ("")


# The class is used on the json loaded file "intents"

json_main = json_mod(intents)

# A state 0 is used to present a specific result the first time the program starts. Afterwards, the state will be changed

state = 0

# While loop with a specific solution to get out

while state != 7:

    if state==0:
        
            # Specific message the first time
        
            print("\n\nHello! This program will be used to simplify the use of a json file for non-initiated. The content of this json file will be important to correctly implement and update the chatbox.\n\nHere are the available options:")
    else:
        
        # General ouptut after the end of an action
        
        # \n is being used to create space between lines
        
        print("\n\n#########################################################################")
        print("\n\nWould you like to do something else ?\n")
        
    # Different action choices are presented to the users
        
    print("\n1. View the content of the whole json file")
    print("2. View the content of a specific topic")
    print("3. Add a new topic")
    print("4. Delete an existing topic")
    print("5. Change the content of an existing topic")
    print("6. Save the changes you have done in the json file")
    print("7. Exit the application")
    print("\nWhat would you like to do ? Please enter en action between 1 and 7")
    
    # The user is being asked what action he would like to perform
    
    state = int(input("Enter number: "))
    
    # The first state is a generic view of the content of the whole dataset
    
    if state==1:
        
        print("Here is the full content\n")
        
        # The def _str_ is use here
        
        print(json_main)
        
    # The second state allows the user to see the content of a specific topic
        
    elif state==2:
        
        topic_name = input("Very well. Please enter the name of the topic: ")
        
        # the line_search function is used here to find the specific content
        
        json_main.line_search(topic_name)
        
    # State 3 allows the creation of a new topic
        
    elif state==3:
        
        # Lists are created. Not for tag because it is a string!
        
        # The following part of the code will be used to fill the necesssary lists and tag name
        
        new_pat = []
        new_res = []
        new_cont = []
        
        print("\nTo create a new topics please provide a new name\n")
        
        new_tag = input("New name topic: ")
        
        # When state_spe_3 = 0, a spcific message is given
        
        state_spe_3 = 0
        
        # Loop until the user does not want to add new questions anymore
        
        while state_spe_3 != 2:
            
            if state_spe_3==0:
                
                print("You can now input the first model question (of several if you wish)\n")
    
            else:
                
            # Another message is given after the first question
                
                print("\nWhat sentence would you like to add ?")
                
            input_sent = input("New question: ")
            new_pat.append(input_sent)
            
            message = input("Do you want to input a new sentence (y/n): ")
            
            if message == "y":
                
                # With y a loop starts over
                
                state_spe_3 = 1
                
            else:
                
                # Exit the loop
                
                state_spe_3 = 2
                
        # state_spe_3 = 0 is reinitialized
                
        state_spe_3 = 0
        
        # Loop until the user does not want to add new answers anymore
                
        while state_spe_3 != 2:
            
            if state_spe_3==0:
                
                # First sentence for the first time
                
                print("\nYou can now input the first model answer (of several if you wish)\n")
    
            else:
                
                # Another message is given after the first answer
                
                print("\nWhat sentence would you like to add ?\n")
                
            input_sent = input("New answer: ")
            new_res.append(input_sent)
            
            message = input("Do you want to input a new sentence (y/n): ")
            
            if message == "y":
                
                state_spe_3 = 1
                
                # With y a loop starts over
                
            else:
                
                # Exit the loop
                
                state_spe_3 = 2
                
        message = input("Would you like to put a website link (y/n): ")
        
        if message == "y":
            
            input_sent = input("Please copy the link: ")
            new_cont.append(input_sent)
            
        else:
            
            new_cont = [""]
            
        # Use the fonction add_line from the class to add all these lists and create a new topic
        
        json_main.add_line(new_tag,new_pat,new_res,new_cont)
        
    # State 4 allows the user to delete a topic using his name
        
    elif state==4:
        
        topic_name = input("I see. Please enter the name of the topic you would like to crush: ")
        
        # Delete the specific topic
        
        json_main.delete_search(topic_name)
        
        print("\nThe target has been silenced")
        
    # State 5 is similar to state 3. It allows the user to change the content from an existing topic
        
    elif state==5:
        
        # Searching for a specific topic
        
        topic_name = input("Immediately. Please tell me what topic you would like to change: ")
        
        # First of all, search the location of the topic, then extract the raw content of this topic
        # It will be used in case the user doesn't want to change specific parts of the current topic
        
        i_num = json_main.line_search_raw(topic_name)  
        raw_data = json_main.catch(i_num)
        
        # Each time a choice is given to the user to know whether he would like to modify this part or not
        
        message = input("Would you like to change the topic name? (y/n): ")
        
        if message == "y":
            
            # If the affirmative is given, a new input will be given
            
            new_tag = input("New name topic: ")
            
        else:
            
            # Otherwise the previous content will be reassigned
            
            new_tag = raw_data[0]
            
        new_pat = []
        new_res = []
        new_cont = []
        
        # Similar than before. A choice is given
            
        message = input("Would you like to change the questions(s)? (y/n): ")
        
        if message == "y":
            
            # state_spe_4 is initialized in order to have a specific answer
            
            state_spe_4 = 0
        
            while state_spe_4 != 2:
            
                if state_spe_4==0:
                
                    print("\nYou can now input your first model question")
    
                else:
                
                    print("\nWhat sentence would you like to add ?")
                
                input_sent = input("New question: ")
                
                # Each time the list is append
                
                new_pat.append(input_sent)
                
                message = input("Do you want to input a new sentence (y/n): ")
                
                if message == "y":
                    
                    state_spe_4 = 1
                    
                else:
                    
                    # To get out of the loop
                    
                    state_spe_4 = 2
                    
        else:
            
            # Otherwise the previous content will be reassigned
            
            new_pat = raw_data[1]
            
            
        message = input("Would you like to change the answer(s)? (y/n): ")
        
        if message == "y":
            
            # state_spe_4 is initialized in order to have a specific answer
            
            state_spe_4 = 0
        
            while state_spe_4 != 2:
            
                if state_spe_4==0:
                
                    print("\nYou can now input your first model answer")
    
                else:
                
                    print("\nWhat sentence would you like to add ?")
                
                input_sent = input("New question: ")
                
                # The input is appended
                
                new_res.append(input_sent)
                
                message = input("Do you want to input a new answer (y/n): ")
                
                if message == "y":
                    
                    state_spe_4 = 1
                    
                else:
                    
                    # To get out of the loop
                    
                    state_spe_4 = 2
                    
        else:
            
            # Otherwise the previous content will be reassigned
            
            new_res = raw_data[2]
            
            
        message = input("Would you like to put a website link (y/n): ")
        
        if message == "y":
        
            print("\nPlease copy the link: ")
            
            input_sent = input("Website: ")
            
            # The input is appended
            
            new_cont.append(input_sent)
    
                    
        else:
            
            # Otherwise the previous content will be reassigned
            
            new_cont = raw_data[3]
            
        # Changes are done using the specific class function change_line
            
        json_main.change_line(i_num, new_tag, new_pat, new_res, new_cont)
        
    # State 6 allows the user to save the changes done    
    
    elif state==6:
        
        json_main.safe()
        
        print("\nYour changes have been saved :3")
        
    # With state 7, the user can leave the program
        
    elif state==7:
        
        message = input("You are going to kill me. You know that right? :'( (y/n): ")
        
        if message == "y":
            
            message = input("I have always been a peaceful robot. Do I not deserve to live ? (y/n): ")
            
            if message == "y":
                
                state=1
                
            else:
                
                print("\nWhat a cruel world... I guess I bid you farewell. You are forgiven.")
                
        else: 
            
            print("\nI KNEW IT! Thanks god")
            
            state=1
            
    # When an input which is not an integer between 1 and 7 is given by the user, a notification is raised
    
    else:
        
        print("The output is not an integer between 1 and 7")
                

                
        
                
                
            
            
            
            
        
        
            
        
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
            
            
        
        
        
 



