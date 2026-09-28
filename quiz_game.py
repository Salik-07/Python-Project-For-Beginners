import random
from termcolor import cprint

QUESTION = "question"
ANSWER = "answer"
OPTIONS = "options"

def ask_question(index, question, options):
    print(f"Question {index}: {question}")
    
    for option in options:
        print(option)

    return input("Your answer: " ).upper().strip();

def run_quiz(quiz):
    random.shuffle(quiz)
    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])
        
        if answer == item[ANSWER]:
            cprint("Correct!", "green")
            score += 1
        else:
            cprint(f"Wrong! The correct answer is {item[ANSWER]}", "red")

        print()

    print(f"Quiz over! Your final score is {score} out of {len(quiz)}")

def main():
    quiz = [{
        QUESTION: "What is the capital of France?",
        ANSWER: "C",
        OPTIONS: ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"]
    }, {
        QUESTION: "Which planet is know as the red planet?",
        ANSWER: "B",
        OPTIONS: ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"]
    },{
        QUESTION: "What is the largest ocean on Earth?",
        ANSWER: "D",
        OPTIONS: ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"]
    }]

    run_quiz(quiz)

if __name__ == "__main__":
    main()