from input_handler import InputHandler
from orbit_parser import FormattedParser, LinearParser
import sys

input = InputHandler(sys.argv)
parsedInput = None

# linear orbit file or formatted?
if len(input.split('\n')) == 1:
    parsedInput = LinearParser(input)
else:
    parsedInput = FormattedParser(input)

# TODO Write and implement interpreter here

