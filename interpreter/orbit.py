from operator_function import Operator, is_drop_op
from table import Table, table_title_seperator, table_lookup_by_title

verbose = False

def string_table_to_array(table):
    """Convert a formatted table string to a list of operators in a specific order."""
    ret = []
    split_table = [i.split(' ') for i in table.split('\n')]
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

def parse_linear_table(input_text, tables, table_name):
    """Parse a linear input table."""
    child_id = 0
    offset = 0
    table = []

    for i in range(9):  # 9 operators expected for 3x3 table
        operator = input_text[i+offset]
        table.append(operator)
        if is_drop_op(operator):
            # Calculate the new offset when parsing child tables
            child_offset = parse_linear_table(input_text[i+offset+1:], tables, f"{table_name}.{child_id}")
            if child_offset is None:
                raise ValueError(f"Failed to parse child table {table_name}.{child_id}")
            offset += child_offset  # Add the child table's offset to the main offset
            child_id += 1
    
    tables.append(Table(table_name, table))
    return 9  # Returning 9 because we expect to parse 9 operators per table

def link_child_tables(r, tables):
    """Link child tables to their parent."""
    child_id = 0
    get_title = lambda: r.title + table_title_seperator + str(child_id)
    for drop_op in filter(is_drop_op, r.operators):
        child_index = table_lookup_by_title(tables, get_title())  # Get the index of the child table
        drop_op.table = tables.pop(child_index)  # Use the index to pop the table
        link_child_tables(drop_op.table, tables)  # Recursively link any child tables
        child_id += 1

def parse_input(input_text):
    """Parse the input and link all tables."""
    tables = []
    initial_table_name = 'root'

    # Parse linear table format
    parse_linear_table(input_text, tables, initial_table_name)
    
    root = tables.pop(0)  # Get the root table
    link_child_tables(root, tables)
    
    if verbose:
        print("Parsed tables:", [table.title for table in tables])

