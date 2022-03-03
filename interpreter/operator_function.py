__all__ = ['is_drop_op', 'Operator']

operator_functions = {'P': print} # TODO
drop_ops = ['x', 'c', 'k', 'p'] # TODO

def is_drop_op(op):
    return op.string in drop_ops # TODO

class Operator:
    def __init__(self, op):
        self.func = None
        # self.func = operator_functions[op]
        self.string = op
        self.table = None

    def run(self, data, table_output=None):
        self.func(data, table_output)
