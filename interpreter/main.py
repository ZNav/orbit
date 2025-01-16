import sys

class Table:
    def __init__(self, name):
        self.name = name
        self.data = []  # Holds the data for the table
        self.type = None  # Type (string, binary, number, mixed)

    def add_data(self, row):
        # Debugging: Show data being added
        print(f"Adding data to {self.name}: {row}")
        self.data.append(row)

    def set_type(self, type_):
        # Debugging: Confirm type being set
        self.type = type_
        print(f"Set table {self.name} type to {type_}")

    def get_output(self):
        output = ""
        print(f"Generating output for table {self.name} with type {self.type}")  # Debugging
        if self.type == "string":
            output = ''.join(self.data[0])  # Join characters into a string
        elif self.type == "binary":
            output = ''.join([chr(num) for num in self.data[0]])  # Convert binary values to characters
        elif self.type == "number":
            output = ' '.join(map(str, self.data[0]))  # Join numbers as space-separated string
        elif self.type == "mixed":
            # For mixed type, treat numbers as binary and characters as text
            for item in self.data[0]:
                if isinstance(item, int):
                    output += chr(item)  # Convert binary numbers to characters
                else:
                    output += item  # Keep text as-is
        return output

    def __str__(self):
        return f"Table: {self.name}"


def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    tables = {}
    current_table = None
    current_type = None
    is_data_line = False  # To track whether we are on a data line after 'p'

    for line in lines:
        line = line.strip()  # Strip leading/trailing whitespace

        if not line or line.startswith("#"):  # Skip empty lines or comment lines
            continue

        if line.endswith(":"):  # Table name (e.g., root:)
            table_name = line[:-1].strip()  # Remove the colon and strip extra whitespace
            current_table = Table(table_name)
            tables[table_name] = current_table
            print(f"Processing table: {table_name}")  # Debugging: show table being processed
        elif line.startswith("t ="):  # Type declaration (e.g., t = string)
            current_type = line.split("=")[1].strip()  # Extract the type after 't ='
            if current_table:  # Set the type for the current table
                current_table.set_type(current_type)
                print(f"Set table {current_table.name} type to {current_type}")  # Debugging: show type being set
        elif line.startswith("p"):  # Data line (e.g., p H e l l o)
            data_line = line[2:].strip()  # Remove the "p" from the start and strip extra spaces
            row = data_line.split()  # Split the line into individual components (words, numbers, etc.)

            print(f"Raw data: {row}")  # Debugging: show raw data line

            if row:  # If the row has data
                # Convert the data based on the type
                if current_type == "binary":
                    row = [int(x) for x in row]  # Convert binary values to integers
                elif current_type == "number":
                    row = [int(x) for x in row]  # Convert to integers for number type
                elif current_type == "string":
                    row = [x for x in row]  # Keep the string as-is (list of characters)
                elif current_type == "mixed":
                    # Handle mixed types (convert numbers to characters, leave text as-is)
                    row = [int(x) if x.isdigit() else x for x in row]
                
                # Add the processed row to the current table
                current_table.add_data(row)
                print(f"Processed row: {row}")  # Debugging: show processed row

    return tables


def process_tables(tables):
    output = ""
    for table_name, table in sorted(tables.items()):  # Sort tables by name to maintain order
        if table.data:  # Only process table if data exists
            output += table.get_output()  # Get the output for each table
        else:
            print(f"Warning: Table {table_name} has no data.")  # Debugging: show if a table has no data
    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_file>")
        return

    file_path = sys.argv[1]

    # Parse the file and retrieve the tables
    print(f"Parsing file: {file_path}")  # Debugging print
    tables = parse_file(file_path)

    # Process the tables and print the output
    result = process_tables(tables)
    print(f"Final Output: {result}")  # Final output


if __name__ == "__main__":
    main()

