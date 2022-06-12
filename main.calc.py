#Calculator code
def calculator():
 calculation_function = ("operation symbol")
 ("enter choice of operation")
 num1 = float(input("first number"))
 num2 = float(input("second number"))
#Operation Symbol
{'+'},{'-'},{'*'},{'/'}
#OPERATIONS == INPUT
print("'1' for add")
def add(num1,num2):
 return num1 + num2
print("'2' for subtraction")
def subtract(num1,num2):
 return num1 - num2
print("'3' for multiplication")
def multiply(num1,num2):
 return num1 * num2
print("'4' for division")
def divide(num1,num2):
 return num1 / num2

 while True:
 #Take user input
  choice = input ("Enter('1','2','3','4')")
#Check If Choice Is One Of The Four Operations
 if choice=='1':
  print(num1 + num2)
 elif choice=='2':
  print(num1 - num2)
 elif choice=='3':
  print(num1 * num2)
 elif choice=='4':
  print(num1 / num2)

#Check If User Wants To Perform Another Calculation
#If no, Break While Loop
('next_calculation?'('yes/no'))
input("type 'y' to continue or type 'n'to begin new calculation or end ")
if input == 'yes':
 ('continue with answer')
elif input == 'no':
 print('begin new calculation or end')
else:
 print('invalid command')