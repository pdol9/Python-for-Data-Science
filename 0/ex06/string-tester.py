from filterstring import filterstring


def exec_test(s: str, n: int, result: str):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    RED = "\033[31m"

    argv = ["prog", s, n]
    print(f"\nMinimal word length = {n}")
    print(f"Input: {argv}")
    color = GREEN if result == "pass" else RED
    print(f"Result:{color} ", end="")
    filterstring(argv)
    print(RESET, end="")


def main():

    # input integers (length)
    valid_len = [str(i) for i in range(10)] + ["-2"]
    invalid_len = ["", "a", "1a", "3-"]

    # input strings
    tests = {
            # valid case
            "valid": [
                "This is a bit of a SIMPLE test to validate our Main program where using numerical values inside text string is not allowed",
                # extra edge cases
                "",
                "    ",
                "Word",
                "Supercalifragilisticexpialidocious"
                ],
            # invalid
            "invalid": [
                "This isn't just a simple test to validate our Main program .",
                "There are more than 3 test cases",
                "This is another example, we need to test!",
                "Using other characters like ?, - and * should not pass",
                "Last but not least are numerical values like 123456"
                ]
            }

    # run tests on single input string while incrementing length
    for n in valid_len:
        # treat as expected-to-pass
        s = tests["valid"][0]
        exec_test(s, n, "pass")

    # test valid input strings through fixed length
    for s in tests["valid"]:
        # treat as expected-to-pass
        n = 2
        exec_test(s, n, "pass")

    # test various string input with fixed length
    for s in tests["invalid"]:
        # treat as expected-to-fail
        n = 2
        exec_test(s, n, "fail")

    # run tests with invalid length on a single string case
    for n in invalid_len:
        # treat as expected-to-fail
        s = tests["valid"][0]
        exec_test(s, n, "fail")


if __name__ == "__main__":
    main()
