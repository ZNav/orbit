tableTitleSeperator = '.'

def tableLookupByTitle(tables, title):
    # TODO Error handling
    return [i.title for i in tables].index(title)

class Table:
    title = None
    operators = []

    def __init__(self, title, operators):
        self.title = title
        self.operators = operators
