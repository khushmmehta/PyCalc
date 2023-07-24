from Source.Defaults import *


def algebra_help():
    print("\x1b[1;32mThe current available algebraic commands are:\n"
          "\x1b[1;32mMiscellaneous Commands:\n"
          "\x1b[0;3;32m    help, arithmetic help, algebra help\n"
          "\x1b[0;1;32mquadratic equation (From the format [ ax² + bx + c = 0 ], type in a, b and c respectively in the input prompts to get x.)\n"
          "\x1b[0;1;32mMathematical Constants:\n"
          "\x1b[0;3;32m    pi (3.14159...), tau (6.48318...)"
          "\n")


def polynomial_solver(command):
    print("\x1b[1;33mOnly use x as a variable and write strictly in mathematical terms!")
    polynomial = input("\x1b[0;39m")
    print(polynomial)
    # if command == "binomial":
    #     ans = float(term_to_num(input("The solution to the binomial: ")))
    #     cx = float(term_to_num(input("Coefficient of x: ")))
    #     c = float(term_to_num(input("Base number: ")))
    #     x = simplify_num(round((-c + ans) / cx))
    #     print(f"\x1b[1;32mThe solution for x is {x}!\n")
    # elif command == "trinomial":
    #     ans = float(term_to_num(input("The solution to the trinomial: ")))
    #     cx2 = float(term_to_num(input("Coefficient of x²: ")))
    #     cx = float(term_to_num(input("Coefficient of x: ")))
    #     c = float(term_to_num(input("Base number: ")))
    #     discriminant = cx ** 2 - (4 * cx2 * (c - ans))
    #
    #     if discriminant < 0:
    #         print("\x1b[1;32mThe given trinomial has no solutions!\n")
    #     elif discriminant == 0:
    #         alpha = simplify_num(round((-cx + discriminant ** (1 / 2)) / (2 * cx2), ACCURACY))
    #         print(f"\x1b[1;32mThe solution for x is {alpha}!\n")
    #     elif discriminant > 0:
    #         alpha = simplify_num(round((-cx + discriminant ** (1 / 2)) / (2 * cx2), ACCURACY))
    #         beta = simplify_num(round((-cx - discriminant ** (1 / 2)) / (2 * cx2), ACCURACY))
    #         print(f"\x1b[1;32mThe solutions for x are ({alpha}, {beta})!\n")


def linear_eq_two_vars():
    a1 = float(term_to_num(input("Coefficient a₁: ")))
    b1 = float(term_to_num(input("Coefficient b₁: ")))
    c1 = float(term_to_num(input("Result of the second equation (c₁): ")))
    a2 = float(term_to_num(input("Coefficient a₂: ")))
    b2 = float(term_to_num(input("Coefficient b₂: ")))
    c2 = float(term_to_num(input("Result of the second equation (c₂): ")))

    d = (a1 * b2) - (a2 * b1)
    dx = (c1 * b2) - (c2 * b1)
    dy = (a1 * c2) - (a2 * c1)
    x = simplify_num(round(dx / d, ACCURACY))
    y = simplify_num(round(dy / d, ACCURACY))

    print(f"\x1b[1;32mThe solution set (x, y) is ({x}, {y})!\n")


def quadratic_eq():
    a = float(term_to_num(input("The first term (a): ")))
    b = float(term_to_num(input("The first term (b): ")))
    c = float(term_to_num(input("The first term (c): ")))

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print("\x1b[1;32mThe roots of the equation are not real!\n")
    elif discriminant == 0:
        alpha = simplify_num(round((-b + (discriminant ** (1 / 2))) / (2 * a), ACCURACY))
        print(f"\x1b[1;32mThe sole root of the equation is {alpha}!\n")
    elif discriminant > 0:
        alpha = simplify_num(round((-b + (discriminant ** (1 / 2))) / (2 * a), ACCURACY))
        beta = simplify_num(round((-b - (discriminant ** (1 / 2))) / (2 * a), ACCURACY))
        print(f"\x1b[1;32mThe roots of the equation are {alpha}, {beta}!\n")
