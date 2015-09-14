# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

def myhelp():
   print """ 
   Usage operation: 
        '0'                        Display this usage message 
        '1'                        Add 
        '2'                        Subtract 
        '3'                        Multiply 
        '4'                        Divide 
        """

# take input from the user
def menu():
   print("Select operation:\n")
   print("0.Help")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide\n")
   # choice = input("Enter choice(1/2/3/4):")
   # return choice
   return input("Enter choice(0/1/2/3/4):")

choice = menu()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   myhelp()

elif choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   #print("Invalid input")
   myhelp()