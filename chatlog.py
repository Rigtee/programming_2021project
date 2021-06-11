# Try to open the log_chatbox.txt

try:
    df = pd.read_csv('log_chatbox.txt')

# If it raises an error, create a new file with the column names
except FileNotFoundError:
    df = pd.DataFrame(columns=['Input', 'Output', 'Time', 'Date', 'Intents_predicted', 'Status', 'Language'])
# Analyze what the model is predicting as well as the probability level

reptest = predict_class(message, chatbot_model)
# Create a new row for the log chatbox
new_row = {'Input': message, 'Output': response, 'Time': datetime.time(datetime.now()),
           'Date': datetime.date(datetime.now()), 'Intents_predicted': reptest[0]['intent'],
           'Probability prediction': reptest[0]['probability'], 'Status': 'Student', 'Language': 'EN'}
# Append row of log to the dataframe
df = df.append(new_row, ignore_index=True)
# Save the CSV file with the new line
df.to_csv('log_chatbox.txt', index=False)

# Output the message of the machine

# chatLog.insert(END, "BOT: " + response + '\n\n') # Text box for the bot: prints the corresponding response

# Extract the link from the intent predicted

# ras = bot_response_link(message)
#
# # If there is no link, nothing happened
#
# if ras:
#
#     # If a link exists, it is opened in a browser
#
#     callback(ras)
#
#     # A message with the link is also put in the browser
#
#     chatLog.insert(END, "Bot: " + ras + '\n\n')