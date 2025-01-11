class Table:
    def __init__(self, name, operators):
        self.name = name
        self.operators = operators

    def __str__(self):
        """
        Format the table into a human-readable format.
        If it's a 3x3 table, it will be displayed in a grid.
        """
        operators = [i.strip() for i in self.operators]
        if len(operators) == 9:  # If it's a 3x3 grid
            formatted_table = [[None, None, None] for _ in range(3)]
            x = iter(range(9))
            formatted_table[0][0] = operators[next(x)]
            formatted_table[0][1] = operators[next(x)]
            formatted_table[0][2] = operators[next(x)]
            formatted_table[1][2] = operators[next(x)]
            formatted_table[2][2] = operators[next(x)]
            formatted_table[2][1] = operators[next(x)]
            formatted_table[2][0] = operators[next(x)]
            formatted_table[1][0] = operators[next(x)]
            formatted_table[1][1] = operators[next(x)]

            # Format the rows in a human-readable way
            return f"Table: {self.name}\n" + '\n'.join(
                [' '.join(str(cell) if cell is not None else ' ' for cell in row) for row in formatted_table]
            )
        else:
            return f"Table: {self.name}\n" + ' '.join(operators)

# Function to parse linear input text into a list of tables
def linear_parser(input_text):
    print(f"Parsing linear input: {input_text}")
    tables = []
    # Simulating parsing logic, replace with actual parsing logic
    tables.append(Table("root", ["p"]))
    tables.append(Table("root.0", ["x 72", "\\", "\\", "k", "\\", "\\", "\\"]))
    tables.append(Table("root.0.0", ["1 1 1", "\\", "1", "\\", "P"]))
    tables.append(Table("root.0.1", ["1 1 1", "\\", "1", "P", "1", "1"]))
    tables.append(Table("root.1", ["x 101", "\\", "\\", "k", "\\", "\\", "\\"]))
    tables.append(Table("root.1.0", ["1 1 1", "\\", "1", "\\", "P"]))
    tables.append(Table("root.1.1", ["1 1 1", "\\", "1", "P", "1", "1"]))
    tables.append(Table("root.2", ["x 108", "\\", "\\", "k", "\\", "\\", "\\"]))
    tables.append(Table("root.2.0", ["1 1 1", "\\", "1", "\\", "P"]))
    tables.append(Table("root.2.1", ["1 1 1", "\\", "1", "P", "1", "1"]))
    
    return tables

# Function to print the list of tables in a readable format
def print_tables(tables):
    # Output all tables in a human-readable format
    print("\nTables after parsing:")
    for table in tables:
        print(table)

# Main program flow
if __name__ == "__main__":
    input_text = "root:\np"  # Example input, replace with actual input
    tables = linear_parser(input_text)  # Parsing the input into tables
    print_tables(tables)  # Printing the tables in a human-readable format

