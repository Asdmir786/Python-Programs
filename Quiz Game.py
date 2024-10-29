# Quiz Questions and Answers
questions = [
    {"question": "What is the capital of Japan?", "options": ["a) Tokyo", "b) Kyoto", "c) Osaka"], "answer": "a"},
    {"question": "What is 8 x 7?", "options": ["a) 54", "b) 56", "c) 58"], "answer": "b"},
    {"question": "Which planet is known as the 'Red Planet'?", "options": ["a) Mars", "b) Jupiter", "c) Saturn"], "answer": "a"},
    {"question": "Who was the first President of the United States?", "options": ["a) George Washington", "b) Thomas Jefferson", "c) Abraham Lincoln"], "answer": "a"},
    {"question": "Who wrote Romeo and Juliet?", "options": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen"], "answer": "b"},
    {"question": "Which artist painted the Mona Lisa?", "options": ["a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh"], "answer": "a"},
    {"question": "In soccer, how many players are on the field for each team?", "options": ["a) 9", "b) 11", "c) 13"], "answer": "b"},
    {"question": "Who played Iron Man in the Marvel movies?", "options": ["a) Chris Evans", "b) Robert Downey Jr.", "c) Chris Hemsworth"], "answer": "b"},
    {"question": "Who is known as the 'King of Pop'?", "options": ["a) Elvis Presley", "b) Michael Jackson", "c) Freddie Mercury"], "answer": "b"},
    {"question": "Which company created the iPhone?", "options": ["a) Google", "b) Apple", "c) Samsung"], "answer": "b"},
    {"question": "Which animal is known for having black and white stripes?", "options": ["a) Zebra", "b) Tiger", "c) Panda"], "answer": "a"},
    {"question": "What is the largest planet in our solar system?", "options": ["a) Saturn", "b) Earth", "c) Jupiter"], "answer": "c"},
    {"question": "What is the main ingredient in guacamole?", "options": ["a) Avocado", "b) Tomato", "c) Lettuce"], "answer": "a"},
    {"question": "Which vitamin is known as the 'sunshine vitamin'?", "options": ["a) Vitamin A", "b) Vitamin C", "c) Vitamin D"], "answer": "c"},
    {"question": "Where is the Eiffel Tower located?", "options": ["a) London", "b) Paris", "c) Rome"], "answer": "b"}
]

# Initialize score
score = 0

# Game Start
print("Welcome to the Quiz Game!")
print("Answer each question by typing 'a', 'b', or 'c'.")

# Loop through each question
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    
    # Get the user's answer
    answer = input("Your answer: ").strip().lower()
    
    # Check if the answer is correct
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer was", q["answer"])

# Final Score
print("\nQuiz Completed!")
print(f"Your final score is: {score}/{len(questions)}")

# Show a message based on the score
if score == len(questions):
    print("Perfect score! Well done!")
elif score > len(questions) / 2:
    print("Good job! You got more than half correct.")
else:
    print("Better luck next time! Keep practicing.")
