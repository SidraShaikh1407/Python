"""Aim:Write a program in Python that generates a quiz and uses two files – Question.txt and Answers.txt.
The program open Question.txt and read a question and displays the question with option on the
screen. The program then opens the Answers.txt file"""
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
def load_questions(filename):
    """Load questions from the file."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    questions = []
    temp_question = []
    
    for line in lines:
        if line.strip():  # If line is not empty
            temp_question.append(line.strip())
        else:
            if temp_question:  # Add question block to list
                questions.append("\n".join(temp_question))
                temp_question = []
    
    if temp_question:
        questions.append("\n".join(temp_question))  # Add last question

    return questions


def load_answers(filename):
    """Load answers from the file."""
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file.readlines()]


def run_quiz():
    questions = load_questions("Question.txt")
    answers = load_answers("Answers.txt")
    
    score = 0
    
    for i, question in enumerate(questions):
        print("\n" + question)  # Display question
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()
        
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answers[i].upper()}")

    print(f"\nYour final score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
