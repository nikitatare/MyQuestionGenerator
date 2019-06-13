import random
import csv
def challenge():
    score=0
    questionsRight=0
    quizFile = open("queans.csv","r")
    quizData = quizFile.readlines()
    random.shuffle(quizData)
    questionno=1
    for i in range(5):
        x = quizData[i].strip()
        data = x.split(",")        
        question = data[0]
        CorrectAnswer = data[1]

        print(questionno,".",question)
        answer = input("What is your answer? ")
        if answer == CorrectAnswer:
            print("Correct!")
            score=score+1
            questionsRight=questionsRight+1
            questionno = questionno+1

        else:
            print("Incorrect.")
            print("Correc answer should be: "+CorrectAnswer)
            questionno = questionno+1
        print()

    totalScore = (score / 5) * 100
    print("You got ",score," questions right, and a score of ",totalScore,"%.")
if __name__ == "__main__":
    
    challenge()