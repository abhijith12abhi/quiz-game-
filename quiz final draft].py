import time    

questions = [{
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_option": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_option": 0
    },
    {
        "question": "What is the capital of kerala?",
        "options": ["kochi", "trivandrum", "kasargod", "calicut"],
        "correct_option": 2
    },
    {
        "question": "the battle of plassey was fought in?",
        "options": ["1757", "1782", "1788", "1817"],
        "correct_option": 1
    },
    {
        "question": "under akbar the mir bakshi was required to look after?",
        "options": ["military", "state treasury", "royal household", "land revenue system"],
        "correct_option": 1
    },
    {
        "question": "tripitakas are scared book of ?",
        "options": ["budhhits", "hindus", "jain ", " none of above"],
        "correct_option": 1
    },
    {
        "question": "baby frog is known as ?",
        "options": ["tadpole", "froges", "lich", "drews"],
        "correct_option": 1
    },
    {
        "question": "national animal of india?",
        "options": ["monkey", "Lion", "tiger", "cheta"],
        "correct_option": 1
    },
    {
        "question": "Who is the designer of national flag of india?",
        "options": ["jawaharlal nehuru", "ambedkar", "pingali venakkya", "gandhi"],
        "correct_option": 1
    },
    {
        "question": "Who is the ceo of reliance?",
        "options": ["tata", "adani", "ambani", "hr"],
        "correct_option": 1
    }


    ]

def ask_question(question_data, question_number):
    print(f"Question {question_number + 1}: {question_data['question']}")
    for i, option in enumerate(question_data['options']):
        print(f"{i + 1}. {option}")
    
    user_choice = input("Enter the number of your answer: ")
    return int(user_choice) - 1

def main():
    print("Welcome to the Quiz Game!")
    score = 0
    time_limit = 10 
    
    for question_number, question_data in enumerate(questions):
        print("\n" + "=" * 20)
        print(f"Question {question_number + 1}/{len(questions)}")
        print("=" * 20)
        
        start_time = time.time()
        user_choice = ask_question(question_data, question_number)
        end_time = time.time()
        
        if end_time - start_time > time_limit:
            print("Time's up!")
            continue
        
        if user_choice == question_data['correct_option']:
            
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['options'][question_data['correct_option']]}\n")
    
    print("\n" + "=" * 20)
    print("Quiz Completed!")
    print("=" * 20)
    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()