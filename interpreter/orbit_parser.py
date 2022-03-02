from table import tableLookupByTitle, tableTitleSeperator, Table
from operator_function import Operator, isDropOp

verbose = False

def stringTableToArray(table): # TODO redo this
    ret = []
    splitTable = [i.split(' ') for i in table.split('\n')]
    if len(splitTable) == 1:
        return [splitTable[0][0]]
    
    ret.append(splitTable[0][0])
    ret.append(splitTable[0][1])
    ret.append(splitTable[0][2])
    ret.append(splitTable[1][2])
    ret.append(splitTable[2][2])
    ret.append(splitTable[2][1])
    ret.append(splitTable[2][0])
    ret.append(splitTable[1][0])
    ret.append(splitTable[1][1])
    return ret

def linkChildTables(r, tables):
    childId = 0
    nextTitle = lambda: r.title + tableTitleSeperator + str(childId)
    for dropOp in filter(isDropOp, r.operators):
        dropOp.table = tables.pop(tableLookupByTitle(tables, nextTitle()))
        linkChildTables(dropOp.table, tables)
        childId += 1

def createTableFromArray(title, operatorStringArray):
    return Table(title, [Operator(o) for o in operatorStringArray])


def parseLinearTable(inputText, tables, tableName, first=False):
    childId = 0
    offset = 0
    table = []
    
    for i in range(0, 9 if not first else 1):
        operator = inputText[i+offset]
        table.append(operator)
        if isDropOp(operator):
            offset += parseLinearTable(inputText[i+offset+1:], tables, tableName+'.'+str(childId))
            childId += 1
    
    tables.append(createTableFromArray(tableName, table))
    return i+offset

def LinearParser(inputText):
    tables = []
    initialTableName = 'root'
    parseLinearTable(inputText, tables, initialTableName, True)
    
    root = tableLookupByTitle(tables, initialTableName)
    linkChildTables(root, tables)

    return [root]


def FormattedParser(inputText):
    roots = []
    remaingingTables = inputText
    tables = []

    while True:
        headerEnd = remaingingTables.find(':')
        headerBegin = remaingingTables[:headerEnd].rfind('\n')
        headerBegin = 0 if headerBegin < 0 else headerBegin+1

        if headerEnd < 0:
            break

        # TODO Add error checking here
        bodyBegin = headerEnd+2
        bodyEnd = remaingingTables[bodyBegin:].find('\n\n')
        bodyEnd = None if bodyEnd < 0 else bodyEnd + bodyBegin

        if verbose:
            print('header', headerBegin, headerEnd, 'body', bodyBegin, bodyEnd)
            print('header -\n'+remaingingTables[headerBegin:headerEnd])
            print('body -\n'+remaingingTables[bodyBegin:bodyEnd])

        tableTitle = remaingingTables[headerBegin:headerEnd]
        tables.append(createTableFromArray(tableTitle, stringTableToArray(remaingingTables[bodyBegin:bodyEnd])))
        remaingingTables = remaingingTables[bodyBegin:]

    for i, t in enumerate(tables):
        if len(t.title.split(tableTitleSeperator)) == 1:
            # TODO do performance testing on whether they should be popped or just read
            # also this may error when there are multiple roots (untested)
            roots.append(tables.pop(i))

    for r in roots:
        linkChildTables(r, tables)
    
    return roots