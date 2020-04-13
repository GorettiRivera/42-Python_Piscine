import sys


def reverse(string):
    string = string[::-1].swapcase()
    return string


i = len(sys.argv) - 1
if (i >= 1):
    while (i >= 1):
        sys.stdout.write(reverse(sys.argv[i]))
        if (i > 1):
            sys.stdout.write(' ')
        i = i - 1

if (len(sys.argv) > 1):
    sys.stdout.write('\n')
