import re

# Read the exported chat file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_content = file.readlines()

# Initialize a set to store unique names
participants = set()

pattern = re.compile(r'^(.*?):\s')

# Iterate through each line in the chat
for line in chat_content:
    match = re.match(pattern, line)
    if match:
        sender_name = match.group(1)
        participants.add(sender_name)

# Convert the set of names to a list
participant_list = list(participants)

for participant in participant_list:
    print(participant)
