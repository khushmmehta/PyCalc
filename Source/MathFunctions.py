accuracy = 15

pi = 3.141592653589793
tau = 6.283185307179586


def term_to_num(n):
    if n == "pi":
        return pi
    elif n == "tau":
        return tau
    else:
        return n


def simplify_num(n):
    if float(n) == int(n):
        return int(n)
    else:
        return float(n)


def help_command():
    print("\x1b[1;32mThe current available commands are:\n"
          "\x1b[1;32mMiscellaneous Commands:\n"
          "\x1b[0;3;32m    help\n"
          "\x1b[0;1;32mArithmetic Commands:\n"
          "\x1b[0;3;32m    add, subtract, multiply, divide, reciprocal\n"
          "\x1b[0;1;32mAdvanced Commands:\n"
          "\x1b[0;1;32m    Exponent-Based Commands:\n"
          "\x1b[0;3;32m        square (squares the given number), cube (cubes the given number), exponent (raises x by y)\n"
          "\x1b[0;1;32m    Root-Based Commands:\n"
          "\x1b[0;3;32m        square root (gives the square root of the number), cube root (gives the cube root of the number), root (roots x by y)\n"
          "\x1b[0;1;32mMathematical Constants:\n"
          "\x1b[0;3;32m    pi (3.14159...), tau (6.48318...)"
          "\n")


def add():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print("\x1b[1;32mThe result is ", simplify_num(round(x + y, accuracy)), "!\n")


def subtract():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print("\x1b[1;32mThe result is ", simplify_num(round(x - y, accuracy)), "!\n")


def multiply():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print("\x1b[1;32mThe result is ", simplify_num(round(x * y, accuracy)), "!\n")


def divide():
    x = float(term_to_num(input("Type the first number here: ")))
    y = float(term_to_num(input("Type the second number here: ")))
    print("\x1b[1;32mThe result is ", simplify_num(round(x / y, accuracy)), "!\n")


def exponent(subcommand):
    if subcommand == "square":
        x = float(term_to_num(input("Type the number here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** 2, accuracy)), "!\n")
    elif subcommand == "cube":
        x = float(term_to_num(input("Type the number here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** 3, accuracy)), "!\n")
    elif subcommand == "exponent":
        x = float(term_to_num(input("Type the base number here: ")))
        y = float(term_to_num(input("Type the number you want to raise it to here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** y, accuracy)), "!\n")


def root(subcommand):
    if subcommand == "square root":
        x = float(term_to_num(input("Type the number here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** (1 / 2), accuracy)), "!\n")
    elif subcommand == "cube root":
        x = float(term_to_num(input("Type the number here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** (1 / 3), accuracy)), "!\n")
    elif subcommand == "root":
        x = float(term_to_num(input("Type the base number here: ")))
        y = float(term_to_num(input("Type the number you want to raise it to here: ")))
        print("\x1b[1;32mThe result is ", simplify_num(round(x ** (1 / y), accuracy)), "!\n")


def reciprocal():
    x = float(term_to_num(input("Type the number here: ")))
    print("\x1b[1;32mThe result is ", simplify_num(round(1 / x, accuracy)), "!\n")
