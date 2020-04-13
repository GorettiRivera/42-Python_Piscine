import sys


def check(number):
    if (number == 0):
        sys.stdout.write("I'm Zero\n")
    elif (number % 2 == 0):
        sys.stdout.write("I'm Even\n")
    else:
        sys.stdout.write("I'm Odd\n")


if (len(sys.argv) == 1):
    sys.exit()
if (len(sys.argv) > 2 or (sys.argv[1].isdigit()) is False):
    print("ERROR")
    sys.exit()
else:
    check(int(sys.argv[1]))
