from Source.Defaults import *


def help_command():
    print("\x1b[1;32mThe current available arithmetic commands are:\n"
          "\x1b[1;32mMiscellaneous Commands:\n"
          "\x1b[0;3;32m    help, arithmetic help, algebr help\n"
          "\x1b[0;1;32mMathematical Constants:\n"
          "\x1b[0;3;32m    pi (3.14159...), tau (6.48318...)"
          "\n")


def arithmetic_help():
    print("\x1b[1;32mThe current available arithmetic commands are:\n"
          "\x1b[1;32mMiscellaneous Commands:\n"
          "\x1b[0;3;32m    help, arithmetic help, algebra help\n"
          "\x1b[0;1;32mArithmetic Commands:\n"
          "\x1b[0;3;32m    add, subtract, multiply, divide, reciprocal\n"
          "\x1b[0;1;32mAdvanced Commands:\n"
          "\x1b[0;1;32m    Exponent-Based Commands:\n"
          "\x1b[0;3;32m        square (squares the given number), cube (cubes the given number), exponent (raises x by y)\n"
          "\x1b[0;1;32m    Root-Based Commands:\n"
          "\x1b[0;3;32m        square root (gives the square root of the number), cube root (gives the cube root of the number), root (roots x by y)\n"
          "\x1b[0;1;32m    long solve (use without any letters only!)\n"
          "\x1b[0;1;32mMathematical Constants:\n"
          "\x1b[0;3;32m    pi (3.14159...), tau (6.48318...)"
          "\n")


def add():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print(f"\x1b[1;32mThe result is {simplify_num(round(x + y, ACCURACY))}!\n")


def subtract():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print(f"\x1b[1;32mThe result is {simplify_num(round(x - y, ACCURACY))}!\n")


def multiply():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print(f"\x1b[1;32mThe result is {simplify_num(round(x * y, ACCURACY))}!\n")


def divide(subcommand):
    if subcommand == "divide":
        x = float(term_to_num(input("Type the first number here: ")))
        y = float(term_to_num(input("Type the second number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x / y, ACCURACY))}!\n")
    elif subcommand == "reciprocal":
        x = float(term_to_num(input("Type the number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(1 / x, ACCURACY))}!\n")


def exponent(subcommand):
    if subcommand == "square":
        x = float(term_to_num(input("Type the number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** 2, ACCURACY))}!\n")
    elif subcommand == "cube":
        x = float(term_to_num(input("Type the number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** 3, ACCURACY))}!\n")
    elif subcommand == "exponent":
        x = float(term_to_num(input("Type the base number here: ")))
        y = float(term_to_num(input("Type the number you want to raise it to here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** y, ACCURACY))}!\n")


def root(subcommand):
    if subcommand == "square root":
        x = float(term_to_num(input("Type the number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** (1 / 2), ACCURACY))}!\n")
    elif subcommand == "cube root":
        x = float(term_to_num(input("Type the number here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** (1 / 3), ACCURACY))}!\n")
    elif subcommand == "root":
        x = float(term_to_num(input("Type the base number here: ")))
        y = float(term_to_num(input("Type the number you want to raise it to here: ")))
        print(f"\x1b[1;32mThe result is {simplify_num(round(x ** (1 / y), ACCURACY))}!\n")


def long_solve():
    x = term_to_num((input("Write your question in mathematical terms: ")))
    print(f"\x1b[1;32mThe result is {simplify_num(round(arithmetic_replace(x), ACCURACY))}!\n")
