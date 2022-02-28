operatorFunctions = {'P': print} # TODO
dropOps = ['x', 'c', 'k', 'p'] # TODO

def isDropOp(op):
    return op.string in dropOps # TODO

class Operator:
    table = None
    func = None
    string = ''
    
    def __init__(self, op):
        # self.func = operatorFunctions[op]
        self.string = op

    def run(self, data, tableOutput=None):
        self.func(data, tableOutput)
