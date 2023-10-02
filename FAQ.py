import re
from collections import Counter

def find_frequently_asked_questions(chat_data, threshold=2):
    question_pattern = r'[?]\s*'

    questions = []

    for line in chat_data:
        match = re.search(question_pattern, line)
        if match:
            question = line.strip()
            questions.append(question)

    question_counts = Counter(questions)

    frequently_asked_questions = [question for question, count in question_counts.items() if count >= threshold]

    return frequently_asked_questions

# Read chat data from a text file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_data = file.readlines()

frequently_asked_questions = find_frequently_asked_questions(chat_data)

if frequently_asked_questions:
    print("Frequently Asked Questions in the group:")
    for question in frequently_asked_questions:
        print(question)
else:
    print("No frequently asked questions found in the group.")
