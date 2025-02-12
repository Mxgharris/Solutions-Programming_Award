from math import sqrt as s, pi as pi
def circCalcs():
    radi= int(input("Enter the radius of the circle: "))
    unit= input("Enter the units of the radius: ")
    print(f'''The area of the circle is {pi*radi**2:.5f}{unit}^3
The circumferance of the circle is {pi*2*radi:.5f}{unit}^2''')
    
from random import randint as r
def diceRoll():
    r1=r(1,6)
    r2=r(1,6)
    print(f"Roll one is {r1} and roll two is {r2}, and the sum is {r1+r2}.")
    
from time import sleep as sl
def countDown():
    c=int(input("Enter the time to count down from in seconds: "))
    for i in range(c,-1,-1):
        print(i)
        sl(1)
        
import string
import random
def passwordGen(length):
    u=string.ascii_uppercase
    l=string.ascii_lowercase
    d=string.digits
    sp=string.punctuation
    allch=u+l+d+sp
    password= "".join(random.choice(allch) for _ in range(length))
    return password

from time import time as t
def timer():
    input("Press enter to start the timer.")
    st=t()
    print(st)
    input("Press enter to end timer.")
    end=t()
    print(f"The elapsed time is {end-st:.4f} seconds")
        
    
    