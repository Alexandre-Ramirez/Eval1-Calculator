operand1 = None
operator = None
operand2 = None

def main():
    ask_user_input()
    result = calculate(operand1, operator, operand2)
    display_result(operand1, operator, operand2, result)

    """
def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "))

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    global operand2
    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))
    
"""
def ask_user_float_input():
    try :
        in_float = float(input(operand1))
    except:
        return False
    return True
    try :
        in_float = float(input(operand2))
    except:
        return False
    return True


def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = ask_user_float_input("Enter the first operand: ")

    global operator
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /, ^): ")

    global operand2
    # Get second operand from the user
    operand2 = ask_user_float_input("Enter the second operand: ")


def calculate(ope1, oper, ope2):
    # Perform the operation based on the operator
    match oper:
        case '+':
            res = ope1 + ope2
        case '-':
            res = ope2 - ope2
        case '*':
            res = ope1 * ope2
        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case ' ':
            print("Invalid operator.")
            return
        case '^^':
            res = pow(ope1,ope2)

    return res

def display_result(op1, ope, ope2, res):
    print(str(op1) + " " + ope + " " + str(ope2) + " = " + str(res))

# Call the main function to run the program
main()