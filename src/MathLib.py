from MathRequest import MathRequest

    def get_calculate():
        match MathRequest.get_oper():
            case '+':
                res = MathRequest.get_ope1() + MathRequest.get_ope2()
            case '-':
                res = MathRequest.get_ope1() - MathRequest.get_ope2()
            case '*':
                res = MathRequest.get_ope1() * MathRequest.get_ope2()
            case '/':
                if MathRequest.get_ope2() == 0:
                    print("Error: Division by zero is undefined.")
                    return
                res = MathRequest.get_ope1() / MathRequest.get_ope2()
            case '^':
                res = 1
                for count in range(int(MathRequest.get_ope1())):
                    res = res * MathRequest.get_ope2()
            case _:
                print("Invalid operator.")
                return
        return res