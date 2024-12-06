from MathRequest import MathRequest

class Mathlib:
    def __init__(self,res):
        self.res = res


    def get_calculate(MathRequest):
        ope1 = MathRequest.get_ope1()
        oper = MathRequest.get
        ope2 = MathRequest.get_ope1()

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

        MathRequest.set_res(res)