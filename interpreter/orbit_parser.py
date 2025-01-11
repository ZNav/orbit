from table import table_lookup_by_title, table_title_seperator, Table
from operator_function import Operator, is_drop_op

verbose = True  # Turn on verbose debugging
__all__ = ['linear_parser', 'formatted_parser', 'verbose']

def string_table_to_array(table):
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
    
    print(f"Parsing table: {table_name}, first={first}")
    
    for i in range(0, 9 if not first else 1):
        operator = input_text[i + offset]
        table.append(operator)
        if is_drop_op(operator):
            print(f"Found drop operator: {operator}, processing child table")
            offset += parse_linear_table(input_text[i + offset + 1:], tables, f"{table_name}.{child_id}")
            child_id += 1
    
    tables.append(create_table_from_array(table_name, table))
    print(f"Created table: {table_name} with operators: {table}")
    
    return i + offset

def linear_parser(input_text):
    tables = []
    initial_table_name = 'root'

    print(f"Parsing linear input: {input_text}")
    
    parse_linear_table(input_text, tables, initial_table_name, True)
    
    print(f"Tables after parsing: {tables}")
    
    root = table_lookup_by_title(tables, initial_table_name)
    print(f"Root table: {root}")
    
    link_child_tables(root, tables)

    return [root]

def formatted_parser(input_text):
    roots = []
    remaining_tables = input_text.strip()  # Ensure no leading/trailing whitespace
    tables = []

    print(f"Parsing formatted input: {input_text}")
    
    # Split input into table blocks based on empty lines or sections
    sections = remaining_tables.split('\n\n')
    for section in sections:
        if section.strip():  # Ignore empty sections
            # Split each section into header and body
            header_end = section.find(':')
            header = section[:header_end].strip()
            body = section[header_end + 1:].strip()

            print(f"Found header: {header}, body: {body}")
            
            table_array = string_table_to_array(body)
            tables.append(create_table_from_array(header, table_array))
    
    print(f"Tables after parsing: {tables}")
    
    for i, t in enumerate(tables):
        if len(t.title.split(table_title_seperator)) == 1:
            roots.append(tables.pop(i))

    for r in roots:
        link_child_tables(r, tables)
    
    return roots

