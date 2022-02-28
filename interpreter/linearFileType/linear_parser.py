with open('input_linear.orbit') as f:
    tables = f.read().split(',')

dropOperators = ['x', 'k', '=', 'p', 'i', '+', '-', '/', '*']
passDown = False

# TODO This needs redone with the new table and operator classes

def executeTable(tables, returnData={}, first=False):
    global passDown, dropOperators
    offset = 0
    table = []

    data = {'x': None, 'savedData': [], 'type': bin}
    
    for i in range(0, 9 if not first else 1):
        table.append(tables[i+offset])
        operator = tables[i+offset]
        if operator in dropOperators:
            subData = data.copy() if passDown else {}
            passDown = False
            offset += executeTable(tables[i+offset+1:], subData)
            executeDropOp(operator, data, subData)
        else:
            executeInPlaceOp(operator, data)
    print(formatTable(table), '\n')
    returnData = data
    return i+offset

def executeInPlaceOp(operator, data):
    pass
    

def executeDropOp(operator, data, subData):
    # this code for x
    data = subData

def formatTable(table):
    if len(table) == 9:
        ret = []
        for i in range(0, 9, 3):
            ret.append(','.join(table[i:i+3]))
        return '\n'.join(ret)
    else:
        return ','.join(table)


executeTable(tables, first=True)
