import re
from collections import Counter

def find_most_interactive_date(chat_data):
    date_pattern = r'\[(\d{2}/\d{2}/\d{2})'

    date_counts = Counter()

    for line in chat_data:
        match = re.search(date_pattern, line)
        if match:
            date = match.group(1)
            date_counts[date] += 1

    if date_counts:
        most_interactive_date = max(date_counts, key=date_counts.get)
        interactions_on_date = date_counts[most_interactive_date]
        return most_interactive_date, interactions_on_date
    else:
        return None, 0

# Read chat data from a text file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_data = file.readlines()

most_interactive_date, interactions_on_date = find_most_interactive_date(chat_data)

if most_interactive_date:
    print("Date with the most interaction:", most_interactive_date)
    print("Number of interactions on that date:", interactions_on_date)
else:
    print("No interactions found in the chat data.")
