import sys


def count_characters(user_input: str) -> dict:
    """Return counts of uppercase, lowercase, punctuation, digits,
    and spaces in user_input."""
    categories = {"upper": 0, "lower": 0, "punct": 0, "digits": 0, "spaces": 0}
    punct_set = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    for ch in user_input:
        if ch.isupper():
            categories["upper"] += 1
        elif ch.islower():
            categories["lower"] += 1
        elif ch.isdigit():
            categories["digits"] += 1
        elif ch.isspace():
            # counts all whitespace (spaces, tabs, newlines)
            categories["spaces"] += 1
        elif ch in punct_set:
            categories["punct"] += 1
        else:
            # characters that are neither of the above
            # (e.g., symbols from other scripts)
            pass
    return categories


def main(argv):
    try:
        if len(argv) > 2:
            raise ValueError("More than one (string) argument is provided.")
        if len(argv) < 2:
            try:
                user_input = input("What is the text to count?\n")
            except (EOFError, KeyboardInterrupt):
                return
        else:
            user_input = argv[1]
        counter = count_characters(user_input)
        sum = len(user_input)
        print(f"The text contains {sum} characters:")
        print("Upper-case:", counter["upper"])
        print("Lower-case:", counter["lower"])
        print("Punctuation:", counter["punct"])
        print("Digits:", counter["digits"])
        print("Spaces:", counter["spaces"])
    except ValueError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv)
