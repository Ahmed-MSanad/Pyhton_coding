from calculator_art import logo
# add:
def add(n1,n2):
    return n1+n2
# subtract:
def subtract(n1,n2):
    return n1-n2
# multiply:
def multiply(n1,n2):
    return n1*n2
# divide:
def divide(n1,n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/':divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    want_to_continue = True
    while(want_to_continue):
        user_operation = input("Pic an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[user_operation]
        answer = function(num1,num2)
        print(f"{num1} {user_operation} {num2} = {answer}")
        num1 = answer
        userWilling = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to exit or type 'a' for new calculation.: ")
        if userWilling == 'n':
            want_to_continue = False
        elif userWilling == 'y':
            want_to_continue = True
        elif userWilling == 'a':
            want_to_continue = False
            calculator()

calculator()
