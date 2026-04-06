import sys


def filterstring(argv):
    """
    Function prints a list of words provided as a single string of words.
    Words which have length greater than that of the second argument (integer)
    will be printed.
    Raises ValueError if string contains any char other than letters or spaces
    or integer isn't valid.
    """
    try:
        if len(argv) != 3:
            raise ValueError("the arguments are bad.")
        try:
            num = int(argv[2])
        except ValueError:
            raise ValueError("the arguments are bad.")
        user_input = argv[1]
        # validate input string for invalid characters
        is_valid_char = lambda ch: ch.isalpha() or ch.isspace()
        invalid = [ch for ch in user_input if not is_valid_char(ch)]
        if invalid:
            raise ValueError("the arguments are bad.")
        # print those words from input whose length is greater than provided int
        is_longer = lambda w: len(w) > num
        long_words = [w for w in user_input.split() if is_longer(w)]
        print(long_words)
    except ValueError as e:
        print(f"AssertionError: {e}")


def main(argv):
    """
    Parameters are a string of valid characters and an integer e.i. word length
    Main program accepts following input: "This is a simple test" 3
    """
    filterstring(argv)


if __name__ == "__main__":
    main(sys.argv)
