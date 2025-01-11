__all__ = ['is_drop_op', 'Operator']

operator_functions = {
    'P': lambda data, table_output=None: print(f"Printing: {data}")
}

drop_ops = ['x', 'c', 'k', 'p']  # List of drop operators

def is_drop_op(op):
    return op.string in drop_ops

class Operator:
    def __init__(self, op):
        self.func = operator_functions.get(op)  # Fetch the operator function
        self.string = op
        self.table = None

    def run(self, data, table_output=None):
        if self.func:
            self.func(data, table_output)  # Executes the associated function (e.g., print)

