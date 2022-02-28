import table as ta
import operator_function as op

with open('input.orbit') as f:
    inputText = f.read().replace('\n\n\n', '\n\n').replace('  ', ' ').replace('\t', '')

roots = []
remaingingTables = inputText
tables = []

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
    nextTitle = lambda: r.title + ta.tableTitleSeperator + str(childId)
    for dropOp in filter(op.isDropOp, r.operators):
        dropOp.table = tables.pop(ta.tableLookupByTitle(tables, nextTitle()))
        linkChildTables(dropOp.table, tables)
        childId += 1

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

    print('header', headerBegin, headerEnd, 'body', bodyBegin, bodyEnd)
    print('header -\n'+remaingingTables[headerBegin:headerEnd])
    print('body -\n'+remaingingTables[bodyBegin:bodyEnd])

    tableTitle = remaingingTables[headerBegin:headerEnd]
    tableOperators = []
    for o in stringTableToArray(remaingingTables[bodyBegin:bodyEnd]):
        tableOperators.append(op.Operator(o))
    remaingingTables = remaingingTables[bodyBegin:]
    tables.append(ta.Table(tableTitle, tableOperators))

for i, t in enumerate(tables):
    if len(t.title.split(ta.tableTitleSeperator)) == 1:
        roots.append(tables.pop(i))

for r in roots:
    linkChildTables(r, tables)