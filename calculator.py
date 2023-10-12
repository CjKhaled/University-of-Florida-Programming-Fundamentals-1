import math
solution = 0
calculator_continue = True
final_sum = []
total_calculations = 0

def menu():
    print("Current Result: 0.0\n")
    print("Calculator Menu") # sets up menu
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")

def calculate(number1, number2):
    answer = solution
    if operation == 1:
        answer = number1 + number2
    if operation == 2:
        answer = number1 - number2
    if operation == 3:
        answer = number1 * number2
    if operation == 4:
        answer = number1 / number2
    if operation == 5:
        answer = number1**number2
    if operation == 6:
        answer = math.log(number2,number1)
    return answer

while calculator_continue is True:
    menu()
    print()
    operation = float(input("Enter Menu Selection: ")) # Input for operation
    if operation == 0:
        print("Thanks for using this calculator. Goodbye!")
        calculator_continue = False
        exit(1)
    if operation == 7:
        if total_calculations == 0:
            print("Error: No calculations yet to average!")
            operation = float(input("Enter Menu Selection: "))
        print(f"Sum of calculations: {sum(final_sum)}\n")
        print(f"Number of calculations: {total_calculations}\n")
        print(f"Average of calculations: {sum(final_sum) / total_calculations:.2f}")
        continue
    if operation > 7 and operation < 0:
        print("Error: Invalid Selection!")
    else:
        num1 = float(input("Enter first operand:"))
        num2 = float(input("Enter second operand:"))
        solution = calculate(num1 , num2)
        final_sum.append(solution)
        total_calculations += 1