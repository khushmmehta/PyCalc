from Source.SimpleMath import *
from Source.Algebra import *

print("\x1b[1;34mWELCOME TO PYCALC!\nType help as a command to get started.\n")


def command_evaluator():
    command = str(input("\x1b[0;39mInput your command:\n"))
# START OF ARITHMETIC COMMANDS
    if command == "help":
        help_command()
    elif command == "arithmetic help":
        arithmetic_help()
    elif command == "add":
        add()
    elif command == "subtract":
        subtract()
    elif command == "multiply":
        multiply()
    elif command == "divide":
        divide(command)
    elif command == "reciprocal":
        divide(command)
    elif command == "square" or command == "cube" or command == "exponent":
        exponent(command)
    elif command == "square root" or command == "cube root" or command == "root":
        root(command)
    elif command == "long solve":
        long_solve()
# END OF ARITHMETIC COMMANDS
# START OF ALGEBRAIC COMMANDS
    elif command == "algebra help":
        algebra_help()
    elif command == "quadratic equation":
        quadratic_eq()
    elif command == "linear equations in two variables":
        linear_eq_two_vars()
    elif command == "binomial" or command == "trinomial":
        polynomial_solver(command)
# END OF ALGEBRAIC COMMANDS
    else:
        print("\x1b[1;31mInvalid command!\n")


while True:
    command_evaluator()
