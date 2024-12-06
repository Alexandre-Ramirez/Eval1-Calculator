class MathRequest:

    from MathLib import res

    def __init__ (self, ope1, oper, ope2):
        self.ope1 = ope1
        self.oper = oper
        self.ope2 = ope2
        self.res = None

    def get_res(self):
        if self.oper == '+':
            return self.ope1 + self.ope2
        elif self.oper == '-':
            return self.ope1 - self.ope2
        elif self.oper == '*':
            return self.ope1 * self.ope2
        elif self.oper == '/':
            if self.ope2 == 0:
                raise ZeroDivisionError("Division par zéro")
            return self.ope1 / self.ope2
        else:
            raise ValueError("Opérateur non pris en charge")

    def set_res(self, value):
        self.res = value

    def to_string(self):
        return f"{self.ope1} {self.oper} {self.ope2} = {self.get_res()}"

    def get_ope1(self):
        return self.ope1

    def get_oper(self):
        return self.oper

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return self.ope1

    def set_res(self, value):
        return self.oper

    def to_string(self):
        return self.ope2