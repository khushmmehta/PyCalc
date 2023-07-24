ACCURACY = 15

PI = 3.141592653589793
TAU = 6.283185307179586


def term_to_num(n):
    if n == "pi":
        return PI
    elif n == "tau":
        return TAU
    else:
        return n


def simplify_num(n):
    if float(n) == int(n):
        return int(n)
    else:
        return float(n)


def arithmetic_replace(equation: str):
    replaceable = ["x", "^"]
    replacer = ["*", "**"]

    equation = equation.replace(replaceable[0], replacer[0])
    equation = equation.replace(replaceable[1], replacer[1])

    return eval(equation)


def algebraic_replacer(equation: str, x: float):
    replaceable = ["x", "^"]
    replacer = [x, "**"]

    equation = equation.replace(replaceable[0], replacer[0])
    equation = equation.replace(replaceable[1], replacer[1])

    return eval(equation)
