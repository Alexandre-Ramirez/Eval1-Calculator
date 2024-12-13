class MathLib:

    @classmethod
    def execute(self, mathRequest):

        match mathRequest.set_res() :
            case 'add' :
                mathRequest.set_res(mathRequest.get_ope1() + mathRequest.get_ope2())
            case 'sub' :
                mathRequest.set_res(mathRequest.get_ope1() - mathRequest.get_ope2())
            case 'mul' :
                mathRequest.set_res(mathRequest.get_ope1() * mathRequest.get_ope2())
            case 'div' :
                mathRequest.set_res(mathRequest.get_ope1() / mathRequest.get_ope2())
            case 'pow' :
                mathRequest.set_res(mathRequest.get_ope1() ^ mathRequest.get_ope2())
            case 'root' :
                mathRequest.set_res(mathRequest.get_ope1() ** mathRequest.get_ope2())
