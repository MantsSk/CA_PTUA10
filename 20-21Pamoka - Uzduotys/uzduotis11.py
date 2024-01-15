import logging
import random

logging.basicConfig(filename='quiz_game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = int(correct_answer)

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def validate_answer(self, choice):
        return self.options[choice - 1] == self.options[self.correct_answer - 1]

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def conduct_quiz(self, player):
        logging.info("Quiz started.")
        for question in self.questions:
            try:
                question.display_question()
                choice = int(input(f"Enter your choice (1-{len(question.options)}): "))

                if question.validate_answer(choice):
                    print("Correct!\n")
                    player.score += 1
                else:
                    print("Incorrect!\n")
            except (IndexError, ValueError):
                logging.error(f"Invalid choice for question: {question.text}")
                print("Incorrect! Invalid choice!\n")

        logging.info("Quiz completed.")
        print(f"Quiz completed. Your score: {player.score}/{len(self.questions)}")

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def read_questions_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            questions = []
            for i in range(0, len(lines), 7):
                text = lines[i].strip()
                options = [option.strip() for option in lines[i+1:i+5]]
                correct_answer = lines[i+5].strip()
                questions.append(Question(text, options, correct_answer))
            return questions
    except FileNotFoundError:
        logging.error("Quiz questions file not found.")
        return []

questions = read_questions_from_file('quiz_questions.txt')

if not questions:
    print("Quiz questions not available. Exiting.")
else:
    random.shuffle(questions)

    player_name = input("Enter your name: ")
    player = Player(player_name)

    quiz = Quiz(questions)
    quiz.conduct_quiz(player)
