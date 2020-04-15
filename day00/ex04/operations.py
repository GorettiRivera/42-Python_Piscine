import sys


def math_op(a, b):
    """ This function calculates the four elementary mathematical operations of arithmetic\
    (addition, subtraction, multiplication, division) and the modulo operation."""
    r_add = a + b
    r_subs = a - b
    r_mul = a * b
    try:
        r_div = a / b
        r_mod = a % b
    except(ZeroDivisionError):
        r_div = "ERROR (div by zero)"
        r_mod = "ERROR (modulo by zero)"

    return(r_add, r_subs, r_mul, r_div, r_mod)


usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
argv_len = len(sys.argv)-1
if argv_len == 2:
    if (sys.argv[1].isdigit() and sys.argv[2].isdigit()) is False:
        print("InputError: only numbers\n" + usage)
    else:
        o_add, o_subs, o_mul, o_div, o_mod = math_op(int(sys.argv[1]), int(sys.argv[2]))
        print(f"Sum:\t\t{o_add}")
        print(f"Difference:\t{o_subs}")
        print(f"Product:\t{o_mul}")
        print(f"Quotient:\t{o_div}")
        print(f"Remainder:\t{o_mod}")

if argv_len < 1:
    print(usage)
if argv_len > 2:
    print("InputError: too many arguments\n" + usage)
