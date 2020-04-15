import sys


def text_analyzer(text=""):
    """ This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    c_upper = 0
    c_lower = 0
    c_punt = 0
    c_space = 0

    if text == "":
        text_analyzer(input("Please enter the text to analyze:\n"))
    else:
        for t in text:
            if t.isupper():
                c_upper += 1
            if t.islower():
                c_lower += 1
            if t.isspace():
                c_space += 1
            if t in (".", ",", "-", "'"):
                c_punt += 1
        total = c_upper+c_lower+c_space+c_punt
        print(f"The text contains {total} characters:")
        print(f"- {c_upper} upper letters")
        print(f"- {c_lower} lower letters")
        print(f"- {c_punt} puntuation marks")
        print(f"- {c_space} spaces")


argv_len = len(sys.argv) - 1
if(argv_len == 1):
    text_analyzer(sys.argv[1])