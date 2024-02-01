# codsoft task 2 
# Simple calculator

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error! can not divide by zero...!"
    
    return a//b

def modulo(a,b):
    return a%b


print("Select operation:")
print("1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n Modulo")

choice = input("Enter choice 1/2/3/4/5:")

a =float(input("Enter the first number:"))
b =float(input("Enter the second number:"))

if choice=='1':
    print(f"{a} + {b} =", add(a,b))
elif choice=='2':
    print(f"{a} - {b} =", subtract(a,b))
elif choice=='3':
    print(f"{a} * {b} =", multiply(a,b))
elif choice=='4':
    print(f"{a} / {b} =", divide(a,b))
elif choice=='5':
    print(f"{a} % {b} =", modulo(a,b))
else:
    print("Wrong choice...!")




