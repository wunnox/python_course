import argparse

parser = argparse.ArgumentParser(description='Description of the programme')

# Adding arguments
parser.add_argument('positional_arg', help="A positional argument")
parser.add_argument('-o', '--optional', help="An optional argument")

args = parser.parse_args()

print(args.positional_arg)
print(args.optional)
