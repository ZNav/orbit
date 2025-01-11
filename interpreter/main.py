import sys
import re

class Table:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def __repr__(self):
        return f"Table: {self.name}\n{self.rows}"

def parse_linear_table(input_text, tables, table_name):
    current_table = Table(table_name, [])
    for line in input_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Skip empty lines and comments
        if line.endswith(':'):
            # Found a new table
            table_name = line[:-1]
            tables.append(current_table)
            current_table = Table(table_name, [])
        else:
            current_table.rows.append(line)
    tables.append(current_table)

def linear_parser(input_text):
    tables = []
    initial_table_name = "root"
    parse_linear_table(input_text, tables, initial_table_name)
    return tables

def binary_to_text(tables):
    binary_strings = []
    for table in tables:
        for row in table.rows:
            # Extract the binary part (e.g., "x 72" => binary of 72)
            match = re.match(r'x (\d+)', row)
            if match:
                ascii_value = int(match.group(1))
                binary_strings.append(chr(ascii_value))
    return ''.join(binary_strings)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_file> [-a]")
        sys.exit(1)

    input_file = sys.argv[1]
    show_all_info = '-a' in sys.argv

    try:
        with open(input_file, 'r') as f:
            input_text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    if show_all_info:
        print("Parsing linear input:")
        print(input_text)
    
    tables = linear_parser(input_text)
    
    if show_all_info:
        print("\nTables after parsing:")
        for table in tables:
            print(table)

    result = binary_to_text(tables)
    print("\nBinary to Text Output:")
    print(result)

if __name__ == "__main__":
    main()

