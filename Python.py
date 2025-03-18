from Quizdb import questions
from Quizdb import options
print("*************************************")
print("      Welcome to my Quiz Game        ")
print("*************************************")
i=0
score=0
for question in questions:
    print(question)
    print(options[i])
    i+=1
    answer=input("Enter your Answer(A/B/C/D):").upper()
    if answer==questions[question]:
        print("Correct answer")
        score+=1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {questions[question]}")
    print(f"Your current score is {score}/{i}")
print(f"You have given {score} correct answers.")
print(f"Your score is {score/5*100}%")

