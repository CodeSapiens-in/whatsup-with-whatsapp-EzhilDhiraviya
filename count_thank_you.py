import re

with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_data = file.read()

thank_you_count = len(re.findall(r'thank\s*you', chat_data, re.IGNORECASE))

# Print the result
print(f"The phrase 'thank you' (case-insensitive) appears {thank_you_count} times in the chat.")
