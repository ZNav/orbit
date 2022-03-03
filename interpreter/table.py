table_title_seperator = '.'

def table_lookup_by_title(tables, title):
    # TODO Error handling
    return [i.title for i in tables].index(title)

class Table:
    def __init__(self, title, operators):
        self.title = title
        self.operators = operators
    
    def get_formatted(self):
        operators = [i.string for i in self.operators]

        if len(operators) == 9:
            formatted_table = [[None, None, None] for i in range(3)]
            x = iter(range(9)) # TODO Redo?
            formatted_table[0][0] = operators[next(x)]
            formatted_table[0][1] = operators[next(x)]
            formatted_table[0][2] = operators[next(x)]
            formatted_table[1][2] = operators[next(x)]
            formatted_table[2][2] = operators[next(x)]
            formatted_table[2][1] = operators[next(x)]
            formatted_table[2][0] = operators[next(x)]
            formatted_table[1][0] = operators[next(x)]
            formatted_table[1][1] = operators[next(x)]
            return '\n'.join([' '.join(i) for i in formatted_table])
        else:
            return ' '.join(operators)
