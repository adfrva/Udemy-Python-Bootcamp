from question_model import Question
from data import question_data

print("Welcome to PyQuiz")

q_data = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    q_data.append(new_question)

is_over = False
question_counter = 0
guess_streak = 0

while not is_over:

    if question_counter == len(q_data):
        is_over = True
        print("We're out of questions, goodbye!")
    
    else:
        q_text = q_data[question_counter].text
        q_answer = q_data[question_counter].answer
        guess = input(f"{q_text} - True or False? ")

        if q_answer.lower() == guess.lower():
            print("Correct!")
            guess_streak += 1
        elif guess.lower() == "off":
            is_over = True
            print("Goodbye!")
        else:
            print("Thats wrong :(")
            guess_streak = 0

        print(f"Current guess streak: {guess_streak}")
        question_counter += 1