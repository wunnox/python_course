import argparse

parser = argparse.ArgumentParser(description='Description of the programme')
subparsers = parser.add_subparsers(dest='command')

# Subparser for the 'add' command
add_parser = subparsers.add_parser('add')
add_parser.add_argument('numbers', nargs="+", type=int)

# Subparser for the 'subtract' command
subtract_parser = subparsers.add_parser('subtract')
subtract_parser.add_argument('numbers', nargs="+", type=int)

args = parser.parse_args()

print(args.numbers)

