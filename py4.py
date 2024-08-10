
# Exersice 1 [A]
def user(x,y,z):
    print(f" Hello {x} !")
    print(f"You are {y} years old.")
    print(f"By The Way You Was Born {z} ;)")

user_input1 = input("Enter Your Name: ")
user_input2 = int(input("Enter Your Age: "))

user(user_input1,user_input2,  2016-user_input2 )

#Exersice 2 [B]

def add(num1 , num2): 
    addition= num1 + num2 
    return addition

def sub(num1 , num2):
    subtraction = num1 - num2
    return subtraction

def multi(num1 , num2):
    multiplication = num1 * num2
    return multiplication

def div(num1 , num2):
    divition = num1 / num2
    return divition

x = int(input("ENTER THE FIRST NUMBER: "))
y = int(input("ENTER THE SECOND NUMBER: "))

print(f"The sum is : {add(x,y)}")
print(f"The difference is : {sub(x,y)}")
print(f"The product is : {multi(x,y)}")
print(f"The quotient is : {div(x,y)}")
