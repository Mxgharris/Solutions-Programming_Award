from random import randint as r, choice as ch
from quizDatabaseHelper import *
def printmenu():
    '''print a list of menu items'''
    title ="Welcome to Max's quiz"
    deco = "-"
    menu = '''
1. Multiplication
2. Addition
3. Subtraction
4. Advanced
5. Desplay All Results
6. Search result by person
7. Quit
    '''
    print(f'{title}\n{deco*len(title)}\n{menu}')

def validator(m):
        while True:
            try:
                if m=="menu":
                    choice = int(input('Enter a menu choice (1-7): '))
                    if choice in range(1,8):
                        return choice
                    else:
                        print('Your choice is out of range')
                elif m=="ans":
                    value= int(input('Enter your answer: '))
                    return value
            except ValueError:
                print('Sorry you must enter an integer')

def quiz(s, x):
    '''Handles all the quiz operations'''
    score = 0
    divices = []
    
    if s == "ad":
        divices = [r(1, 3) for _ in range(5)]
    
    for i in range(5):
        if s == "a" or (s == "ad" and divices[i] == 1):  
            num1 = r(1, x)
            num2 = r(1, x)
            correct = num1 + num2
            print(f'{num1} + {num2}')
        elif s == "s" or (s == "ad" and divices[i] == 2): 
            num1 = r(1, x)
            num2 = r(1, x)
            correct = num1 - num2
            print(f'{num1} - {num2}')
        elif s == "m" or (s == "ad" and divices[i] == 3): 
            num1 = r(1, x)
            num2 = r(1, x)
            correct = num1 * num2
            print(f'{num1} x {num2}')
            
        answer = validator("ans")
        if answer == correct:
            print('Correct\n')
            score += 1
        else:
            print('Incorrect\n')
    
    return score
'''def displayAll():
    #prints all scores
    print('All results printed')
    try:
        with open("scores.txt", mode= "r", encoding="utf-8") as scores:
            for line in scores:
                print(line)
    except FileNotFoundError:
        print("No scores avalable yet.")'''

def displayAll():
    readDbdata()

'''def searchByPerson():
    #searches the score by person name
    print('Search initiated')
    search = input("Enter the name: ")
    found= False
    try:
        with open("scores.txt", mode= "r", encoding="utf-8") as scores:
            for line in scores:
                if line.startswith(search+":"):
                    print(line.strip())
                    found=True
        if not found:
            print(f"No results found for {search}.")
    except FileNotFoundError:
        print("No scores avalible yet.")'''

def searchByPerson():
    '''Searches for a person's score by name'''
    Nm = input("Who do you want to check: ")
    rt = searchPerson(Nm)
    if rt:
        print(rt)
    else:
        print(f"No results found for {Nm}.")



'''def recordscores(name,score):
    with open("scores.txt", mode= "a", encoding="utf-8") as scores:
        scores.write(f"{name}: {score}\n")'''

def recordscores(name, score):
    '''Saves score and name to the database'''
    updateOrAdd(name, score)
           
        

def main():
    '''Main application function'''
    name = input("Hello, what is your name: ").strip()
    
    while True:
        printmenu()
        score = -1
        choice = validator("menu")
        
        if choice == 7:  # Exit the program
            print("Have a nice rest of your day!")
            break
        elif choice == 1:
            print('Multiplication Started!\n\n\n\n')
            score = quiz("m", 10)
            print(f'Correct answers = {score}\n')
        elif choice == 2:
            print('Addition Started!\n\n\n\n')
            score = quiz("a", 10)
            print(f'Correct answers = {score}\n')
        elif choice == 3:
            print('Subtraction Started!\n\n\n\n')
            score = quiz("s", 10)
            print(f'Correct answers = {score}\n')
        elif choice == 4:
            print('Advanced Quiz Started!\n\n\n\n')
            score = quiz("ad", 100)
            print(f'Correct answers = {score}\n')
        elif choice == 5:
            displayAll()
        elif choice == 6:
            searchByPerson()
        
        if score > -1:
            recordscores(name, score)
        
main()

