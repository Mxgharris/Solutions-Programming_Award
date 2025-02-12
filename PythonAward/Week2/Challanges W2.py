from random import randint as r
def zeroGorL():
    num=int(input("Enter a number: "))
    if num>0:
        print("Positive")
    elif num<0:
        print("Negative")
    else:
        print("Zero")
        
def guessNum():
    num = r(1,10)
    while True:
        guess=int(input("Guess a number between 1 and 10: "))
        if num>guess:
            print("Too low")
        elif num<guess:
            print("Too high")
        else:
            print("Correct")
            break
        
def multTable():
    num=int(input("Enter a number: "))
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

def countDown():
    num=int(input("Enter a number to count down from: "))
    for i in range(num,-1,-1):
        print(i)
        
def fizzBuzz():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print(f"{i} FizzBuzz")
        elif i%5==0:
            print(f"{i} Buzz")
        elif i%3==0:
            print(f"{i} Fizz")
        else:
            print(f"{i}")

def primeChecker():
    num=int(input("Enter a number: "))
    p=0
    if num<=1:
        print("Not prime")
        p="n"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not prime")
            p="n"
    if p!="n":
        print("Prime")
    
            
    
    
    
    
    