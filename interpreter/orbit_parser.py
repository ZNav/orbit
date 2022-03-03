from table import table_lookup_by_title, table_title_seperator, Table
from operator_function import Operator, is_drop_op

verbose = False
__all__ = ['linear_parser', 'formatted_parser', 'verbose']

def string_table_to_array(table): # TODO redo this
    ret = []
    split_table = [i.split(' ') for i in table.split('\n')]
    if len(split_table) == 1:
        return [split_table[0][0]]
    
    ret.append(split_table[0][0])
    ret.append(split_table[0][1])
    ret.append(split_table[0][2])
    ret.append(split_table[1][2])
    ret.append(split_table[2][2])
    ret.append(split_table[2][1])
    ret.append(split_table[2][0])
    ret.append(split_table[1][0])
    ret.append(split_table[1][1])
    return ret

def link_child_tables(r, tables):
    child_id = 0
    get_title = lambda: r.title + table_title_seperator + str(child_id)
    for drop_op in filter(is_drop_op, r.operators):
        drop_op.table = tables.pop(table_lookup_by_title(tables, get_title()))
        link_child_tables(drop_op.table, tables)
        child_id += 1

def create_table_from_array(title, operator_string_array):
    return Table(title, [Operator(o) for o in operator_string_array])

def parse_linear_table(input_text, tables, table_name, first=False):
    child_id = 0
    offset = 0
    table = []
    
    for i in range(0, 9 if not first else 1):
        operator = input_text[i+offset]
        table.append(operator)
        if is_drop_op(operator):
            offset += parse_linear_table(input_text[i+offset+1:], tables, table_name+'.'+str(child_id))
            child_id += 1
    
    tables.append(create_table_from_array(table_name, table))
    return i+offset

def linear_parser(input_text):
    tables = []
    initial_table_name = 'root'

    parse_linear_table(input_text, tables, initial_table_name, True)
    
    root = table_lookup_by_title(tables, initial_table_name)
    link_child_tables(root, tables)

    return [root]


def formatted_parser(input_text):
    roots = []
    remaining_tables = input_text
    tables = []

    while remaining_tables.find(':') < 0:
        header_end = remaining_tables.find(':')
        header_begin = remaining_tables[:header_end].rfind('\n')
        header_begin = 0 if header_begin < 0 else header_begin+1

        # TODO Add error checking here
        body_begin = header_end+2
        body_end = remaining_tables[body_begin:].find('\n\n')
        body_end = None if body_end < 0 else body_end + body_begin

        if verbose:
            print('header', header_begin, header_end, 'body', body_begin, body_end)
            print('header -\n'+remaining_tables[header_begin:header_end])
            print('body -\n'+remaining_tables[body_begin:body_end])

        table_title = remaining_tables[header_begin:header_end]
        table_array = string_table_to_array(remaining_tables[body_begin:body_end])
        tables.append(create_table_from_array(table_title, table_array))
        remaining_tables = remaining_tables[body_begin:]

    for i, t in enumerate(tables):
        if len(t.title.split(table_title_seperator)) == 1:
            # TODO do performance testing on whether they should be popped or just read
            # also this may error when there are multiple roots (untested)
            roots.append(tables.pop(i))

    for r in roots:
        link_child_tables(r, tables)
    
    return roots