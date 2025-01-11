import sys

class Table:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.subtables = []

    def add_data(self, row):
        self.data.append(row)

    def add_subtable(self, subtable):
        self.subtables.append(subtable)

    def get_binary_data(self):
        binary_data = ""
        print(f"Processing table {self.name}:")
        for row in self.data:
            for char in row:
                if isinstance(char, int):  # Ensure it's numeric
                    binary_value = format(char, '08b')
                    binary_data += binary_value
                    print(f"Converted {char} to {binary_value}")
        return binary_data

    def __str__(self):
        return f"Table: {self.name}"


def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    tables = {}
    current_table = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.endswith(":"):
            table_name = line[:-1]
            current_table = Table(table_name)
            tables[table_name] = current_table
        elif current_table is not None:
            row = [int(x) if x.isdigit() else x for x in line.split()]
            current_table.add_data(row)

    return tables


def process_tables(tables):
    binary_data = ""
    for table_name, table in sorted(tables.items()):  # Sort to maintain order
        binary_data += table.get_binary_data()
    return binary_data


def binary_to_text(binary_data):
    # Remove any non-binary characters (such as spaces)
    binary_data = ''.join([bit for bit in binary_data if bit in '01'])
    ascii_text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:  # Ensure it's a full byte
            ascii_text += chr(int(byte, 2))
    return ascii_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <input_file> [-a]")
        return

    file_path = sys.argv[1]
    show_all = '-a' in sys.argv

    tables = parse_file(file_path)
    binary_data = process_tables(tables)
    ascii_text = binary_to_text(binary_data)

    if show_all:
        print("Tables after parsing:")
        for table in tables.values():
            print(table)
        print("\nBinary Data:", binary_data)

    print("\nBinary to Text Output:")
    print(ascii_text)


if __name__ == "__main__":
    main()

