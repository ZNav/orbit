from os.path import exists

__all__ = ['handle_input']

default_input_file = 'input.orbit'

def open_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def handle_input(argv, file_name=None):
    if file_name != None and exists(file_name):
        return open_file(file_name)
    if len(argv) > 1 and exists(argv[1]):
        return open_file(argv[1])
    elif exists(default_input_file):
        return open_file(default_input_file)
    else:
        return
        # TODO Invalid input error
