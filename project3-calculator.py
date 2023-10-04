logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    print(logo)
    num1 = float(input('Enter your first number?\n'))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:

        operation = input('Choose your operation?\n')
        num2 = float(input('Enter your next number?\n'))
        func = operations[operation]
        answer = func(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if(input('Want to continue or start again, y or n?\n') == 'y'):
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()





