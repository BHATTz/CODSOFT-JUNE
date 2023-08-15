# Define a list of dictionaries with quiz questions and their answers
quiz_questions = [
    {
        'question': 'For which of the following disciplines is Nobel Prize awarded?',
        'choices': ['a) Physics and Chemistry', 'b) Physiology or Medicine', 'c) Literature, Peace and Economics', 'd) All of the above'],
        'correct_answer': 'd'
    },
    {
        'question': 'Garampani sanctuary is located at',
        'choices': ['a) Junagarh, Gujarat', 'b) Diphu, Assam', 'c) Kohima, Nagaland', 'd) Gangtok, Sikkim'],
        'correct_answer': 'b'
    },
    {
        'question': 'What is the tallest mammal?',
        'choices': ['a) Elephant', 'b) Blue Whale', 'c) Lion', 'd) Giraffe'],
        'correct_answer': 'd'
    }
]

def display_question(question_data):
    print(question_data['question'])
    for choice in question_data['choices']:
        print(choice)

def main():
    print("Welcome to the Quiz Game!")
    print("Answer questions by typing the letter corresponding to your choice.")
    
    total_questions = len(quiz_questions)
    correct_answers = 0
    
    for question in quiz_questions:
        display_question(question)
        user_answer = input("Your answer: ").lower()
        
        if user_answer == question['correct_answer']:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect. The correct answer is:", question['correct_answer'].upper())
    
    final_score = (correct_answers / total_questions) * 100
    print("\nQuiz Completed!")
    print(f"Your Score: {final_score:.2f}%")
    
    if final_score >= 70:
        print("Great job! You did well.")
    else:
        print("Keep practicing to improve.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thank you for playing!")

# Start the quiz game
main()
