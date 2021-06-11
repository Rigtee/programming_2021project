# Packages

import pandas as pd # Used to create dataframes
from datetime import datetime # To have the current time


# Load the txt file

df = pd.read_csv('log_chatbox_test.txt')

# Set up a class with all the needed functions to manipulate the dataframe

class text_mod:
    
    def __init__(self,txt_log):
        
        # Values are sorted before iniiating an initial order
        
        new_row = []
        
        for j in range(len(txt_log)):
            
            new_row.append(j+1)
            
        # Values are sorted before iniiating an initial order
            
        temp_txt = txt_log.sort_values(by=['Date', 'Time'])
        
        # Add a new row with number sorted by time
        
        temp_txt['Number'] = new_row
        
        self.txt_log = temp_txt
        
        self.txt_log_filters = temp_txt
        
    def full_line_content(self,j,data_filters):
        
        # Function used later in another function to format data in a nice way

        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')        
        print("{:<6}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}".format('\nn°','Prob. model',data_filters.columns[2],data_filters.columns[3],data_filters.columns[4],data_filters.columns[5],data_filters.columns[6],))
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("{:<5}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}".format(data_filters.iloc[j][8],round(data_filters.iloc[j][7],3),data_filters.iloc[j][2][:8],data_filters.iloc[j][3],data_filters.iloc[j][4],data_filters.iloc[j][5],data_filters.iloc[j][6]))
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("Input:   ",data_filters.iloc[j][0])   
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')

        print("Output:  ",data_filters.iloc[j][1])   
        
    def limited_log(self, probl=0, probh=1, yyyyl = 1999, yyyyh = 2022, mml = 0, mmh = 12, ddl = 1, ddh = 31, hhl=0, hhh=24):
        
        # We start with the filtered dataframe -> take into account previous choices
        
        txt_log = self.txt_log
        
        # Initiate the dataframe saved at the end without data modifications other than removing lines
                
        mod_txt_log = txt_log
        
        
        # Loop to slect data following probability and time criterias
        
        for i in range(len(mod_txt_log)):
            
            # Use the function datetime.strptime to format the two strings as time type
    
            date_temp = datetime.strptime((mod_txt_log['Date'][i] + ' ' + mod_txt_log['Time'][i][:8]), '%Y-%m-%d %H:%M:%S')
            
            # Time conditions
            
            if date_temp.year < yyyyl or date_temp.year > yyyyh or date_temp.month < mml or date_temp.month > mmh or date_temp.day < ddl or date_temp.day > ddh or date_temp.hour < hhl or date_temp.hour > hhh:
                
                mod_txt_log = mod_txt_log.drop(i)
                
        # We use conditions here with txt_log because it is still a non-modified dataframe (at least in this function)
                
        mod_txt_log = mod_txt_log[(mod_txt_log['Probability prediction'] >= probl) & (mod_txt_log['Probability prediction'] <= probh)]
        
        # Print a non detailed view of the remaining dataset
        
        print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format('n°',mod_txt_log.columns[0],'Prob. model',mod_txt_log.columns[2],mod_txt_log.columns[3],mod_txt_log.columns[4],mod_txt_log.columns[5],mod_txt_log.columns[6],mod_txt_log.columns[1]))
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')


        for j in range(len(mod_txt_log)):
            
            print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format(mod_txt_log.iloc[j][8],mod_txt_log.iloc[j][0][:32],round(mod_txt_log.iloc[j][7],3),mod_txt_log.iloc[j][2][:8],mod_txt_log.iloc[j][3],mod_txt_log.iloc[j][4],mod_txt_log.iloc[j][5],mod_txt_log.iloc[j][6],mod_txt_log.iloc[j][1][:32]))
            
        
        # save the new settings
        
        self.txt_log_filters = mod_txt_log
        
        
    def limited_print(self, details=False, sort=False, type='date', ascending=False):
        
        
        # Specific function to print the content of the filtered dataframe
        
        txt_log_filters = self.txt_log_filters
        
        if sort == True:
            
            # Take into account two sorting parameters
            
            if type == 'date':
                
                # In the two cases ask the given sorting order is taken into account
                
                if ascending == False:
                    
                    txt_log_filters = txt_log_filters.sort_values('Date',ascending=False)
                    
                else:
                    
                    txt_log_filters = txt_log_filters.sort_values('Date',ascending=True)
                
            elif type == 'prob':
                    
                if ascending == False:
                    
                    txt_log_filters = txt_log_filters.sort_values('Probability prediction',ascending=False)
                    
                else:
                
                    txt_log_filters = txt_log_filters.sort_values('Probability prediction',ascending=True)
        
        # two types of formats with or without details
        
        if details==False:
        
            print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format('n°',txt_log_filters.columns[0],'Prob. model',txt_log_filters.columns[2],txt_log_filters.columns[3],txt_log_filters.columns[4],txt_log_filters.columns[5],txt_log_filters.columns[6],txt_log_filters.columns[1]))
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
        
            
            for j in range(len(txt_log_filters)):
                
                print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format(txt_log_filters.iloc[j][8],txt_log_filters.iloc[j][0][:32],round(txt_log_filters.iloc[j][7],3),txt_log_filters.iloc[j][2][:8],txt_log_filters.iloc[j][3],txt_log_filters.iloc[j][4],txt_log_filters.iloc[j][5],txt_log_filters.iloc[j][6],txt_log_filters.iloc[j][1][:32]))
                
        # That's the detailed print
                
        else:
            
            for j in range(len(txt_log_filters)):
                
                self.full_line_content(j,txt_log_filters)
                
    def refresh(self):
        
        # Simply clean the filtered dataframe
        
        txt_log = self.txt_log
            
        self.txt_log_filters = txt_log
        
    def __str__(self):
    
        txt_log = self.txt_log
        
        print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format('n°',txt_log.columns[0],'Prob. model',txt_log.columns[2],txt_log.columns[3],txt_log.columns[4],txt_log.columns[5],txt_log.columns[6],txt_log.columns[1]))
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------')

        
        for j in range(len(txt_log)):
            
            print("{:<5}{:<35}{:<14}{:<10}{:<12}{:<20}{:<10}{:<10}{:<10}".format(txt_log.iloc[j][8],txt_log.iloc[j][0][:32],round(txt_log.iloc[j][7],3),txt_log.iloc[j][2][:8],txt_log.iloc[j][3],txt_log.iloc[j][4],txt_log.iloc[j][5],txt_log.iloc[j][6],txt_log.iloc[j][1][:32]))
            
            
        # Specific functions are used to print the result. Nothing is thus "returned"
        
        return ("")

# The class is used on the txt loaded file df

text = text_mod(df)


#print(text)
text.limited_print(details=True)
text.limited_print(details=False)
text.limited_print(details=False,sort=True,type='date',ascending=False)
text.limited_print(details=False,sort=True,type='prob',ascending=True)


text.full_line_content(5)
text.limited_log(ddl=30)
text.limited_log(ddh=27)
text.refresh()

# The class is used on the txt loaded file df

text = text_mod(df)

# A state 0 is used to present a specific result the first time the program starts. Afterwards, the state will be changed

state = 0

# While loop with a specific solution to get out

while state != 5:

    if state==0:
        
            # Specific message the first time
        
            print("\n\nHello! This program will be used to simplify the use of a text file for non-initiated. The content of this txt file will be important to correctly analyze the chatbox output and update it.\n\nHere are the available options:")
    else:
        
        # General ouptut after the end of an action
        
        # \n is being used to create space between lines
        
        print("\n\n#########################################################################")
        print("\n\nWould you like to do something else ?\n")
        
    # Different action choices are presented to the users
        
    print("\n1. View the logs of the whole text file")
    print("2. Filter logs")
    print("3. Vizualize the filtered logs (detail/sorting options)")
    print("4. refresh the modified logs")
    print("5. Exit the application")

    print("\nWhat would you like to do ? Please enter en action between 1 and 5")
    
    # The user is being asked what action he would like to perform
    
    try:
        
        state = int(input("Enter number: "))


    except ValueError:
        
        print("\n\n#########################################################################")
        print("\nThis is not a number! Please try an integer between 1 and 5\n")
        print("\n#########################################################################")
    
    #♣state = int(input("Enter number: "))
    
    # The first state is a generic view of the content of the whole dataset
    
    if state==1:
        
        print("Here is the full content\n")
        
        # The def _str_ is use here
        
        print(text)
        
    # The second state allows the user to see the content of a specific topic
        
    elif state==2:
        
        # define first all the default values for the filter function
        
        probl_default = 0
        probh_default = 1 
        yyyyl_default = 1999
        yyyyh_default = 2022
        mml_default = 0
        mmh_default = 12
        ddl_default = 1
        ddh_default = 31
        hhl_default = 0
        hhh_default= 24

        message = input("Do you want to filter logs using date? (y/n): ")
    
        if message == "y":
            
            message = input("Do you want to set up year parameters? (y/n): ")
            
            if message == "y":
            
                date_year = input("Please write the earliest accepted year : ")
                
                
                try:
                    
                    yyyyl_default = int(date_year)
        

                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
                date_year = input("Please write the latest accepted year : ")
                
                try:
                    
                    yyyyh_default = int(date_year)
        

                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
            message = input("Do you want to set up month parameters? (y/n): ")
            
            if message == "y":
            
                date_month = input("Please write the earliest accepted month : ")
                
                
                try:
                    
                    mml_default = int(date_month)
        

                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
                date_month = input("Please write the latest accepted month : ")
                
                try:
                    
                    mmh_default = int(date_month)
        

                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
            message = input("Do you want to set up day parameters? (y/n): ")
            
            if message == "y":
            
                date_day = input("Please write the earliest accepted day : ")
                
                
                try:
                    
                    ddl_default = int(date_day)
        

                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
                date_day = input("Please write the latest accepted day : ")
                
                try:
                    
                    ddh_default = int(date_day)
                    
                except ValueError:
                    
                    print("\nThis is not a number!\n")
                    
            message = input("Do you want to set up hour parameters? (y/n): ")
            
            if message == "y":
            
                date_hour = input("Please write the earliest accepted hour : ")
                
                
                try:
                    
                    hhl_default = float(date_hour)
        

                except ValueError:
                    
                    print("\nThis is not a coorect number!\n")
                    
                date_hour = input("Please write the latest accepted hour : ")
                
                try:
                    
                    hhh_default = float(date_hour)
                    
                except ValueError:
                    
                    print("\nThis is not a correct number!\n")
                    


        message = input("Do you want to select logs using the predicted model certainty? (y/n): ")

        if message == "y":
        
            prob_l = input("Please write the lowest probability (between 0 and 1) : ")
            
            
            try:
                
                probl_default = float(prob_l)
    

            except ValueError:
                
                print("\nThis is not a number!\n")
                
            prob_h = input("Please write the highest probability (between 0 and 1) : ")
            
            try:
                
                probh_default = float(prob_h)
    

            except ValueError:
                
                print("\nThis is not a number!\n")  

        print("\n")                  
                
        text.limited_log(probl_default, probh_default, yyyyl_default, yyyyh_default, mml_default, mmh_default, ddl_default, ddh_default, hhl_default, hhh_default)

        
        
    # State 3 allows the creation of a new topic
        
    elif state==3:
        
        details = False
        sort = False
        type_ = 'date'
        ascending = False
        
        message = input("Do you want to view results with a detailed view? (y/n): ")
    
        if message == "y":
                
            details = True
            
        message = input("Do you want to sort results? (y/n): ")
    
        if message == "y":
            
            sort = True
            
            message = input("Do you want to sort results by date? (y/n): ")
            
            if message == "y":
                
                type_ = 'date'
                
            message = input("Do you want to sort results by the predicted model certainty? (y/n): ")
                
            if message == "y":
                
                type_ = 'prob'
                    
            message = input("Do you want to sort results in ascending order? (y/n): ")
                
            if message == "y":
                
                ascending = True
              
            if message == "n":
                
                ascending = False
                

        text.limited_print(details, sort, type_, ascending)

    elif state==4:
        
        # Refresh the modified dataframe
        
        text.refresh()
        
        
        print("\n\n#########################################################################")
        print("\nThe filtered dataframe has been refreshed!")

    elif state==5:

        print("\nGood day to you!")        
    
    else:
        
        print("Warning: The output is not an integer between 1 and 5")




    
    
        
    