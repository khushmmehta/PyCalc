from Source.MathFunctions import *

print("\x1b[1;34mWELCOME TO PYCALC!\nType help as a command to get started.\n")


def command_evaluator():
    command = str(input("\x1b[0;39mInput your command:\n"))

    if command == "help":
        help_command()
    elif command == "add":
        add()
    elif command == "subtract":
        subtract()
    elif command == "multiply":
        multiply()
    elif command == "divide":
        divide()
    elif command == "square" or command == "cube" or command == "exponent":
        exponent(command)
    elif command == "square root" or command == "cube root" or command == "root":
        root(command)
    elif command == "reciprocal":
        reciprocal()
    else:
        print("\x1b[1;31mInvalid command!\n")


while True:
    command_evaluator()
