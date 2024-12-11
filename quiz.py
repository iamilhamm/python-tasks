def welcome_message():
    print("Welcome to the Python Challenge! Let's test your knowledge!")
    print("There will be 5 multiple-choice questions for you to answer.")

def display_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            user_answer = int(input("Your answer (enter the number): "))  
            
            if 1 <= user_answer <= len(options):  
                if user_answer == correct_answer:  
                    print("That's right! Well done")
                    return True
                else:
                    print(f"Incorrect, The correct answer was: {options[correct_answer - 1]}")
                    return False
            else:
                print(f"Please enter a number between 1 and {len(options)}")  

        except ValueError:  
            print("Please enter a number.")

def display_results(score, total_questions): 
    print(f"The total score of your quiz is {score} out of {total_questions}")
    if score == total_questions: 
        print("You answered all of them correctly")
    elif score >= total_questions * 0.8:
        print("You did well.")
    elif score >= total_questions * 0.5:
        print("Good Effort, not so bad!")
    else:
        print("Take time and go over the content!")

def main():
    welcome_message()
    questions = [
        {"question": "What does the <a> tag in HTML represent?", "options": ["An image element", "A link element", "A list element", "A table element"], "correct_answer": 2},
        {"question": "Which CSS property is used to change the background color of an element?", "options": ["color", "background-color", "border-color", "font-color"], "correct_answer": 2},
        {"question": "Which of the following is the correct way to create a function in JavaScript?", "options": ["function myFunction { }", "function myFunction() { }", "function myFunction():", "def myFunction"], "correct_answer": 2},
        {"question": "Which of the following is used to retrieve data from a MySQL database?", "options": ["DELETE", "INSERT", "SELECT", "UPDATE"], "correct_answer": 3},
        {"question": "Which of the following data types is mutable in python?", "options": ["Tuple", "List", "String", "Dictionary"], "correct_answer": 2}
    ]

    score = 0
    for q in questions:
        is_correct = display_question(q["question"], q["options"], q["correct_answer"])
        if is_correct:
            score += 1

    display_results(score, len(questions))  
    print("Hope you enjoyed answering the Quiz!")

if __name__ == "__main__":
    main()
