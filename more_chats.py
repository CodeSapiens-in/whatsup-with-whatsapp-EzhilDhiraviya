import re
from collections import defaultdict

# Read the WhatsApp chat file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_data = file.read()

# Split the chat into individual messages
messages = re.findall(r'\[(.*?)\] (.*?): (.*)', chat_data)

# Initialize a dictionary to store message counts for each sender
message_counts = defaultdict(int)

# Iterate through messages and count messages sent by each sender
for timestamp, sender, message in messages:
    message_counts[sender] += 1

# Find the sender with the most messages
most_active_sender = max(message_counts, key=message_counts.get)

# Print the results
print(f"The sender with the most messages is '{most_active_sender}' with {message_counts[most_active_sender]} messages.")
