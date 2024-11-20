# Name : Arin Verma
# Enrollment No. : 0176AL221031

# Assignment 2       Submission Date : 18/11/24


# Q1.  Program for quiz app

import random

# Dictionary to store users
users_db = {}

# A bank of 20 questions for each topic
questions_bank = {
    "Math": [
        ("What is 2+2?", "4"),
        ("What is 10/2?", "5"),
        ("What is 5*6?", "30"),
        ("What is 9-3?", "6"),
        ("What is 3^2?", "9"),
        ("What is the square root of 16?", "4"),
        ("What is 7*7?", "49"),
        ("What is 15+5?", "20"),
        ("What is 100-45?", "55"),
        ("What is 9*8?", "72"),
        ("What is 25/5?", "5"),
        ("What is 100/10?", "10"),
        ("What is 5+15?", "20"),
        ("What is 3*9?", "27"),
        ("What is 1000-500?", "500"),
        ("What is 50/5?", "10"),
        ("What is 10*10?", "100"),
        ("What is 12*12?", "144"),
        ("What is 5^3?", "125"),
        ("What is 10^2?", "100")
    ],
    "Science": [
        ("What planet is known as the Red Planet?", "Mars"),
        ("What is the chemical symbol for water?", "H2O"),
        ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
        ("What is the powerhouse of the cell?", "Mitochondria"),
        ("What planet is closest to the sun?", "Mercury"),
        ("What force keeps us on the ground?", "Gravity"),
        ("What is the hardest natural substance?", "Diamond"),
        ("How many bones are in the human body?", "206"),
        ("What is the symbol for gold?", "Au"),
        ("What is the speed of light?", "300000000"),
        ("What is the human body’s largest organ?", "Skin"),
        ("What gas do humans exhale?", "Carbon Dioxide"),
        ("What is the center of an atom called?", "Nucleus"),
        ("What do bees make?", "Honey"),
        ("What is the largest planet in the solar system?", "Jupiter"),
        ("What is the chemical symbol for oxygen?", "O"),
        ("What is the process plants use to make food?", "Photosynthesis"),
        ("What is the study of life called?", "Biology"),
        ("How many planets are in the solar system?", "8"),
        ("What metal is liquid at room temperature?", "Mercury")
    ],
    "History": [
        ("Who was the first president of the USA?", "George Washington"),
        ("What year did World War I begin?", "1914"),
        ("Who was the first man on the moon?", "Neil Armstrong"),
        ("What year did the Titanic sink?", "1912"),
        ("What ancient civilization built the pyramids?", "Egyptians"),
        ("Who was known as the Iron Lady?", "Margaret Thatcher"),
        ("What year did World War II end?", "1945"),
        ("Who was the first emperor of Rome?", "Augustus"),
        ("What year did the Berlin Wall fall?", "1989"),
        ("Who discovered America?", "Christopher Columbus"),
        ("What was the name of the ship on which the Pilgrims traveled to America?", "Mayflower"),
        ("In which year was the Magna Carta signed?", "1215"),
        ("Who was the last queen of France?", "Marie Antoinette"),
        ("Who was the first female Prime Minister of India?", "Indira Gandhi"),
        ("In which year was the US Declaration of Independence signed?", "1776"),
        ("Who was the leader of the Soviet Union during World War II?", "Joseph Stalin"),
        ("In which city was Archduke Franz Ferdinand assassinated?", "Sarajevo"),
        ("Who was the first woman to fly solo across the Atlantic?", "Amelia Earhart"),
        ("What famous battle took place in 1066?", "Battle of Hastings"),
        ("Which empire was ruled by Julius Caesar?", "Roman Empire")
    ]
}

def register_user():
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already taken. Try again.")
        return register_user()
    password = input("Enter a password: ")
    users_db[username] = password
    print("User registered successfully!")


def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Try again.")
        return False

# Function to generate multiple-choice options relevant to the topic
def generate_options(correct_answer, topic):
    options = [correct_answer]

    if topic == "Math":
        # Generate numbers jo correct answer ke close ho
        correct_number = int(correct_answer)
        while len(options) < 3:
            random_option = str(correct_number + random.choice([-3, -2, -1, 1, 2, 3]))
            if random_option not in options:
                options.append(random_option)

    elif topic == "Science":
        distractors = ["Oxygen", "Hydrogen", "Helium", "Carbon", "Nitrogen", "Gravity", "Pluto", "Earth", "Venus"]
        while len(options) < 3:
            random_option = random.choice(distractors)
            if random_option != correct_answer and random_option not in options:
                options.append(random_option)

    elif topic == "History":
        distractors = ["1492", "Napoleon", "Einstein", "Alexander", "1918", "1969", "1775", "Elizabeth I", "Henry VIII"]
        while len(options) < 3:
            random_option = random.choice(distractors)
            if random_option != correct_answer and random_option not in options:
                options.append(random_option)

    random.shuffle(options)
    return options


def start_quiz():
    topics = list(questions_bank.keys())
    print(f"\nAvailable topics: {', '.join(topics)}")
    selected_topic = input("Please select your topic (Math, Science, History): ").capitalize()
    if selected_topic not in topics:
        print("Invalid topic selected!")
        return start_quiz()
    else:
        print(f"\nYour topic is: {selected_topic}")
    questions = random.sample(questions_bank[selected_topic], 5)
    score = 0

    for question, correct_answer in questions:
        options = generate_options(correct_answer, selected_topic)
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            user_answer_index = int(input("Choose the correct answer (1, 2, or 3): ")) - 1
            if options[user_answer_index].strip().lower() == correct_answer.strip().lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The correct answer was: {correct_answer}")
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")

    print(f"\nYou scored {score} out of 5.\n")
    return score


# Main program loop
def main():
    print("Welcome to the Quiz Application!")
    while True:
        choice = input("Do you want to (1) Register or (2) Login? Enter 1 or 2: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                break

    while True:
        start_quiz()
        retry = input("Do you want to (1) Reattempt or (2) Exit? Enter 1 or 2: ")
        if retry == '2':
            print("Thank you for playing! Goodbye!")
            break


main()





