tableTitleSeperator = '.'

def tableLookupByTitle(tables, title):
    # TODO Error handling
    return [i.title for i in tables].index(title)

# TODO Update to work with classes (takes array of strings now)
def formatTable(table):
    if len(table) == 9:
        ret = []
        for i in range(0, 9, 3):
            ret.append(','.join(table[i:i+3]))
        return '\n'.join(ret)
    else:
        return ','.join(table)

class Table:
    title = None
    operators = []

    def __init__(self, title, operators):
        self.title = title
        self.operators = operators
