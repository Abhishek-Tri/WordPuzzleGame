import random

#this function shuffles the actual word
def suffle(word):
    w=random.sample(word,k=len(word))
    return ''.join(w)
#this function prints the problem word and calculates score
def printquestion(wrd,score):
    problemword=suffle(wrd)
    print("\narrange the word to form a valid word")
    print(problemword)
    userword=input()
    print()
    if userword.upper()==wrd:
        print("correct answer")
        score+=1
    else:
        print("wrong answer")
        score-=1
    return score
#main function of the game from where execution starts
def game():   
    score=0
    words=["FATHER","BREAK","COUNTRY","HUMANITY"]
    for wrd in words:
        score=printquestion(wrd,score)

    print()
    print("your score is:",score)
    print()


game()                       