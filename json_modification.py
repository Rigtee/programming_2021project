import json

with open('test_json\intents.json') as f:
    intents = json.loads(f.read())
    
class json_mod:
    
    def __init__(self,jsonimp):
        
        self.jsonimp = jsonimp
        
    def line(self,i):
        
        jsonimp = self.jsonimp
        
        jtag = jsonimp['intents'][i]["tag"]
        jpatterns = jsonimp['intents'][i]["patterns"]
        jresponses = jsonimp['intents'][i]["responses"]
        
        print('Tag: ',jtag ,'\nPatterns: ', jpatterns,'\nResponse: ', jresponses)
        
        if jsonimp['intents'][i]["context"]:
            
            jwebsite = jsonimp['intents'][i]["context"]
            print('Website: ',jwebsite)
            
            
    def line_search(self,name):
        
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            if jsonimp['intents'][j]["tag"]==name:
                
                print("\nTopics %s" %(j+1), '"%s":\n' %(name))
                self.line(j)
                
    def line_search_raw(self,name):
    
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            if jsonimp['intents'][j]["tag"]==name:
                
                return j
            
            
    def delete_line(self,i):
        
        jsonimp = self.jsonimp
        
        del jsonimp['intents'][i]
        
        self.jsonimp = jsonimp
        
        
    def delete_search(self,name):
        
        jsonimp = self.jsonimp
        
        size = len(jsonimp['intents'])
        
        for j in range(size):
            
            if jsonimp['intents'][j]["tag"]==name:
                
                self.delete_line(j)
                
    def catch(self,i):
        
        jsonimp = self.jsonimp
        
        values = []
        
        values.append(jsonimp['intents'][i]["tag"])
        values.append(jsonimp['intents'][i]["patterns"])
        values.append(jsonimp['intents'][i]["responses"])
        values.append(jsonimp['intents'][i]["context"])
        
        return values
        
    
    def add_line(self,ta,pat,res,web=""):
        
        jsonimp = self.jsonimp
        
        if type(pat)==str:
            
            patlist=[]
            patlist.append(pat)
            
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
            
        elif type(web)==list:
            
            weblist=web
            
        dico = {"tag" : ta, "patterns": patlist, "responses": reslist, "context": weblist}
        jsonimp['intents'].append(dico)
        
        self.jsonimp = jsonimp
        
        
    def change_line(self,i,ta,pat,res,web=""):
        
        jsonimp = self.jsonimp
        
        jsonimp['intents'][i]["tag"] = ta
        jsonimp['intents'][i]["patterns"] = pat
        jsonimp['intents'][i]["responses"] = res
        jsonimp['intents'][i]["context"] = web
        
        self.jsonimp = jsonimp
        
        
    def safe(self):
        
        jsonimp = self.jsonimp
        
        with open('test_json\intents2.json', 'w') as f:
                json.dump(jsonimp, f)
                
            
    def __str__(self):
        
        jsonimp=self.jsonimp
        
        size = len(jsonimp['intents'])
        for j in range(size):
            print("\nTopics %s:\n" %(j+1))
            self.line(j)
        return ("")



json_main = json_mod(intents)

state = 0
while state != 7:
    
    if state==0:
        
            print("\n\nHello! This program will be used to simplify the use of a json file for non-initiated. The content of this json file will be important to correctly implement and update the chatbox.\n\nHere are the available options:")
    else:
        
        print("\n\n#########################################################################")
        print("\n\nWould you like to do something else ?\n")
        
    print("\n1. View the content of the whole json file")
    print("2. View the content of a specific topic")
    print("3. Add a new topic")
    print("4. Delete an existing topic")
    print("5. Change the content of an existing topic")
    print("6. Save the changes you have done in the json file")
    print("7. Exit the application")
    print("\nWhat would you like to do ? Please enter en action between 1 and 7")
    
    
    state = int(input("Enter number: "))
    
    if state==1:
        
        print("Here is the full content\n")
        print(json_main)
        
    elif state==2:
        
        topic_name = input("Very well. Please enter the name of the topic: ")
        json_main.line_search(topic_name)
        
    elif state==3:
        
        
        new_pat = []
        new_res = []
        new_cont = []
        
        print("\nTo create a new topics please provide a new name\n")
        
        new_tag = input("New name topic: ")
        
        state_spe_3 = 0
        
        while state_spe_3 != 2:
            
            if state_spe_3==0:
                
                print("You can now input the first model question (of several if you wish)\n")
    
            else:
                
                print("\nWhat sentence would you like to add ?")
                
            input_sent = input("New question: ")
            new_pat.append(input_sent)
            
            message = input("Do you want to input a new sentence (y/n): ")
            
            if message == "y":
                
                state_spe_3 = 1
            else:
                
                state_spe_3 = 2
                
        state_spe_3 = 0
                
        while state_spe_3 != 2:
            
            if state_spe_3==0:
                
                print("\nYou can now input the first model answer (of several if you wish)\n")
    
            else:
                
                print("\nWhat sentence would you like to add ?\n")
                
            input_sent = input("New answer: ")
            new_res.append(input_sent)
            
            message = input("Do you want to input a new sentence (y/n): ")
            
            if message == "y":
                
                state_spe_3 = 1
            else:
                
                state_spe_3 = 2
                
        message = input("Would you like to put a website link (y/n): ")
        
        if message == "y":
            
            input_sent = input("Please copy the link: ")
            new_cont.append(input_sent)
        else:
            
            new_cont = [""]
        
        json_main.add_line(new_tag,new_pat,new_res,new_cont)
        
    elif state==4:
        
        topic_name = input("I see. Please enter the name of the topic you would like to crush: ")
        
        json_main.delete_search(topic_name)
        
        print("\nThe target has been silenced")
        
    elif state==5:
        
        topic_name = input("Immediately. Please tell me what topic you would like to change: ")
        
        i_num = json_main.line_search_raw(topic_name)  
        raw_data = json_main.catch(i_num)
        
        message = input("Would you like to change the topic name? (y/n): ")
        
        if message == "y":
            
            new_tag = input("New name topic: ")
            
        else:
            
            new_tag = raw_data[0]
            
        new_pat = []
        new_res = []
        new_cont = []
            
        message = input("Would you like to change the questions(s)? (y/n): ")
        
        if message == "y":
            
            state_spe_4 = 0
        
            while state_spe_4 != 2:
            
                if state_spe_4==0:
                
                    print("\nYou can now input your first model question")
    
                else:
                
                    print("\nWhat sentence would you like to add ?")
                
                input_sent = input("New question: ")
                new_pat.append(input_sent)
                
                message = input("Do you want to input a new sentence (y/n): ")
                
                if message == "y":
                    
                    state_spe_4 = 1
                    
                else:
                    
                    state_spe_4 = 2
                    
        else:
            
            new_pat = raw_data[1]
            
            
        message = input("Would you like to change the answer(s)? (y/n): ")
        
        if message == "y":
            
            state_spe_4 = 0
        
            while state_spe_4 != 2:
            
                if state_spe_4==0:
                
                    print("\nYou can now input your first model answer")
    
                else:
                
                    print("\nWhat sentence would you like to add ?")
                
                input_sent = input("New question: ")
                new_res.append(input_sent)
                
                message = input("Do you want to input a new answer (y/n): ")
                
                if message == "y":
                    
                    state_spe_4 = 1
                    
                else:
                    
                    state_spe_4 = 2
                    
        else:
            
            new_res = raw_data[2]
            
            
        message = input("Would you like to put a website link (y/n): ")
        
        if message == "y":
        
            print("\nPlease copy the link: ")
            
            input_sent = input("Website: ")
            new_cont.append(input_sent)
    
                    
        else:
            
            new_cont = raw_data[3]
            
        json_main.change_line(i_num, new_tag, new_pat, new_res, new_cont)
        
        
    elif state==6:
        
        json_main.safe()
        
        print("\nYour changes have been saved :3")
        
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
    else:
        
        print("the output is not an integer between 1 and 7")
                

                
        
                
                
            
            
            
            
        
        
            
        
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
            
            
        
        
        
 



