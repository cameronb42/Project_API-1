import requests
import sys
import argparse
import textwrap

#HOST = "34.121.122.205"
HOST = "34.70.63.106"

parser = argparse.ArgumentParser( 
    formatter_class=argparse.RawDescriptionHelpFormatter,description=textwrap.dedent('''
                              ~ Group 1 Tool Commands ~
			       -----------------------
        Choose one of the following! If you need help please type -> python3 cli.py -h
			       md5 - use: md5 string
			   factorial - use: factorial num
			   fibonacci - use: fibonacci num
			    is-prime - use: is-prime num
			keyval - use: keyval -Redis_options string'''))
			
parser.print_help()

subparsers = parser.add_subparsers(help='commands', dest='cli')

#Creating all parsers for the API functions
#md5
md5_parser = subparsers.add_parser('md5', help='Displays a string as a json value hex')
md5_parser.add_argument('md5_string', help='Displays a string as a json value hex',action='store')

#factorial
fact_parser = subparsers.add_parser('factorial', help=' an integer as a factorial')
fact_parser.add_argument('fact_integer', help='Returns an integer as a factorial', action='store')

#fibonacci
fib_parser = subparsers.add_parser('fibonacci', help='Returns fibbonacci value')
fib_parser.add_argument('fib_integer', help='Returns fibbonacci value', action='store')

#is-prime
prime_parser = subparsers.add_parser('is-prime', help='Returns a true or false')
prime_parser.add_argument('prime_integer', help='Returns a true or false', action='store')

#keyval 
keyval_parser = subparsers.add_parser('keyval', help='Use this to control the Redis Keyvals. Enter a key value then chose an option: -post, -get, -put, -delete')
#keyval_parser.add_argument('keyval_parser', action='store', help='The Keyval thing')
keyval_parser.add_argument('-post', dest='keypost', help='This writes a new key-value pair')
keyval_parser.add_argument('-get',dest='keyget', help='This to retrieve the value')
keyval_parser.add_argument('-put',dest='keyput', help='This overwrite the value on an existing key')
keyval_parser.add_argument('-delete', dest='keydelete', help='Use to delete key (and value) supplied')


args = parser.parse_args()


def md5(user_str):
    md5=requests.get(f'http://{HOST}/md5/{user_str}')
    print(md5.text)

def factorial(user_int):
    factorial=requests.get(f'http://{HOST}/factorial/{user_int}')
    print(factorial.text)
	
def fibonacci(user_int):
    fibonacci=requests.get(f'http://{HOST}/fibonacci/{user_int}')
    print(fibonacci.text)

def prime(user_int):
    prime=requests.get(f'http://{HOST}/is-prime/{user_int}')
    print(prime.text)


def keyvalpost(user_str):
    print(f'http://{HOST}/keyval')
    parts = user_str.split('=')
    data = {'key':parts[0], 'value':parts[1]}
    keyvalpost=requests.post(f'http://{HOST}/keyval', json=data)
    print(keyvalpost.text)

def keyvalget(user_str):
    keyvalget=requests.get(f'http://{HOST}/keyval/{user_str}')
    print(keyvalget.text)

def keyvalput(user_str):
    parts = user_str.split('=')
    data = {'key':parts[0], 'value':parts[1]}
    keyvalput=requests.put(f'http://{HOST}/keyval', json=data)
    print(keyvalput.text)

def keyvaldelete(user_str):
    keyvaldelete=requests.delete(f'http://{HOST}/keyval/{user_str}')
    print(keyvaldelete.text)




if args.cli == 'md5':
    md5(args.md5_string)

if args.cli == 'factorial':
    factorial(args.fact_integer)

if args.cli == 'fibonacci':
    fibonacci(args.fib_integer)

if args.cli == 'is-prime':
    prime(args.prime_integer)

if args.cli == 'keyval':
    if args.keypost:
        keyvalpost(args.keypost)

    if args.keyget:
        keyvalget(args.keyget)

    if args.keyput:
        keyvalput(args.keyput)

    if args.keydelete:
        keyvaldelete(args.keydelete)
