def TemperatureConverter():
    tempC= int(input("Enter a temperature in Celsius: "))
    tempF= tempC*(9/5)+32
    print(f"{tempC}°C is {tempF}°F")
    tempF= int(input("Enter a temperature in Fahrenheit: "))
    tempC= (tempF-32) *(5/9)
    print(f"{tempF}°F is {tempC}°C")
    
    
    

def calcMain():
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    Sum(num1,num2)
    Dif(num1,num2)
    Prod(num1,num2)
    Quo(num1,num2)
    Mod(num1,num2)
    Int(num1,num2)
    
def Sum(a,b):
    print(f"Sum: {a+b:.1f}")
def Dif(a,b):
    print(f"difference: {abs(a-b):.1f}")
def Prod(a,b):
    print(f"Product: {a*b:.1f}")
def Quo(a,b):
    print(f"Quotient: {a/b:.1f}")
def Mod(a,b):
    print(f"Modulus: {a%b:.1f}")
def Int(a,b):
    print(f"Result of integer division: {int(a/b):.1f}")


def nameMain():
    name = input("Enter your full name: ")
    print(f'''Your initials are: {initials(name)}
Total number of characters excluding spaces: {countCharacters(name)}
Your name in reverse order is: {reverseName(name)}''')
    

def initials(nm):
    initials= ''
    index = 0
    while index< len(nm):
        if nm[index] !=' ':
            initials += nm[index].upper()
            index=nm.find(' ',index)+1
            if index == 0: 
                break
        else:
            index += 1
    return initials
def countCharacters(nm):
    return len(nm.replace(" ",""))
def reverseName(nm):
    return nm[::-1]
    
    