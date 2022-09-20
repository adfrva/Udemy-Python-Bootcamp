print("Welcome to the Python Calculator")

def add(num1, num2):
    answer = int(num1) + int(num2)

    return(answer)

def subtract(num1, num2):
    answer = int(num1) - int(num2)

    return(answer)

def multiply(num1, num2):
    answer = int(num1) * int(num2)

    return(answer)

def divide(num1, num2):
    answer = int(num1) / int(num2)

    return(answer)

is_done = False

while not is_done:
    user_num1, user_num2 = input("Enter two numbers for operation: ").split()
    print("\n-\n+\n*\n/\n")
    user_operation = input("Type the operation for the numbers: ")

    answer = 0

    if user_operation == "+":
        answer = add(user_num1, user_num2)
    elif user_operation == "-":
        answer = subtract(user_num1, user_num2)
    elif user_operation == "*":
        answer = multiply(user_num1, user_num2)
    elif user_operation == "/":
        answer = divide(user_num1, user_num2)
    
    print(f"{user_num1} {user_operation} {user_num2} = {str(answer)}")
    end_prompt = input("Would you like to continue? Yes or No").lower()

    if end_prompt == "no":
        is_done = True
        print("Goodbye")