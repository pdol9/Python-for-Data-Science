import sys


def whatis(args):
    if len(args) < 2:
        return
    try:
        if len(args) > 2:
            raise ValueError("more than one argument is provided.")
        try:
            val = int(args[1])
        except ValueError:
            print("AssertionError: argument is not an integer.")
            return
    except ValueError as e:
        print(f"AssertionError: {e}")
        return
    print("I'm Even." if val % 2 == 0 else "I'm Odd.")


if __name__ == '__main__':
    whatis(sys.argv)
