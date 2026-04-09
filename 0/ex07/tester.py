import sys
from sos import sos


def exec_test(arglist):
    BLUE = "\033[32m"
    RESET = "\033[0m"
    if len(arglist) > 2:
        arg = arglist[1] + " " + arglist[2]
    elif len(arglist) > 1:
        arg = arglist[1]
    else:
        arg = "no arg provided"
    print("Input argument:", arg)
    print(BLUE)
    sos(arglist)
    print(RESET, end="")


def main():
    tests = [
        # pass
        ["prog", "sos"],
        ["prog", "hello 123"],
        ["prog", "what a nice weather"],
        # fail 
        ["prog", "he%%o"],
        ["prog", "he$o"],
        ["prog", "h @ g A ."],
        ["prog", "sos", "test"],
        ["prog", "good work!"],
        ["prog", "fast-car."],
        ["prog", ""],
        ["prog", '"quoted arg"'],
        ["prog"],                   # missing argv[1]
        # additional edge cases:
        ["prog", "   "],            # only spaces
        ["prog", "newline\nchar"],    # contains newline
        ["prog", "a" * 1000],       # very long string
    ]

    for t in tests:
        exec_test(t)
        print("-" * 40)


if __name__ == "__main__":
    main()
