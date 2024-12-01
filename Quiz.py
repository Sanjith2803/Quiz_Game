def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. Japan", "B. England", "C. Germany", "D. Spain"],
        "answer": "A"
    },
    {
        "prompt": "What is the smallest country in the world?",
        "options": ["A. Spain", "B. Vatican City", "C. Japan", "D. France"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who is the author of the 'Harry Potter' series?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(questions)