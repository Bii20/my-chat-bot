import random
import time

# Define a set of questions with multiple choices
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Marie Curie"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "choices": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A) Oxygen", "B) Gold", "C) Osmium", "D) Hydrogen"],
        "answer": "A"
    },
    {
        "question": "What is the name of the longest river in the world?",
        "choices": ["A) Nile", "B) Amazon", "C) Yangtze", "D) Mississippi"],
        "answer": "A"
    }
]

def ask_question(question):
    """Display the question and choices, and get the user's answer."""
    print("\n" + question["question"])
    for choice in question["choices"]:
        print(choice)
    
    user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid input! Please enter A, B, C, or D: ").strip().upper()

    return user_answer == question["answer"]

def start_quiz():
    """Start the quiz and keep track of the score."""
    print("\nWelcome to the Trivia Quiz! 🎉")
    time.sleep(1)

    score = 0
    random.shuffle(questions)  # Shuffle questions for variety

    for i, question in enumerate(questions[:3], start=1):  # Ask 3 questions only
        print(f"\nQuestion {i}:")
        if ask_question(question):
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was: {question['answer']}")

    print(f"\nYour final score: {score}/{len(questions[:3])}")
    if score == 3:
        print("Perfect score! You're a trivia master! 🏆")
    elif score > 1:
        print("Good job! 👍")
    else:
        print("Better luck next time! 😅")

if __name__ == "__main__":
    start_quiz()
