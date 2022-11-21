import argparse
import sys

parser = argparse.ArgumentParser(description="This is Hunter's script")

parser.add_argument('-m', dest='basic', help='Enter Some Text')

parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]',
default=0, type=int, required=False, help='<required> Enter a simple Integer')

parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]',
default=0.0, type=float, required=False, help='Enter a simple float')

parser.add_argument('-s', '--string', dest='varString', metavar='[a string]',
default='hello', type=str, required=False, help='Enter a simple string')

parser.add_argument('-l', dest='varList', metavar='[strings]', default=[],
nargs='+', required=False, help='Enter a list of strings (space delimited)')

parser.add_argument('-t', '--set-true', dest='bool_t', default=False,
action='store_true', required=False, help='Toggle from default False to True')

parser.add_argument('-f', '--set-false', dest='bool_f', default=True,
action='store_false', required=False, help='Toggle from default True to False')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')


args = parser.parse_args()

if len(sys.argv) == 1:
    print (parser.print_help())
    exit(0)

print ("Your integer value is: " + str (args.varInteger))
print ("Your float value is: " + str(args.varFloat))
print ("Your string is: " + str(args.varString))
print ("Your list is: " + str(args.varList))
