from input_handler import handle_input
from orbit_parser import formatted_parser, linear_parser
import sys

input = handle_input(sys.argv)
parsed_input = None

# linear orbit file or formatted?
if len(input.split('\n')) == 1:
    parsed_input = linear_parser(input)
else:
    parsed_input = formatted_parser(input)

# TODO Write and implement interpreter here

