import sys


def encode(text: str) -> str:
    """Encode plain text to Morse."""
    if not hasattr(encode, "_MORSE"):
        encode._MORSE = {
                "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
                "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
                "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---", 
                "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
                "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
                "Z": "--..",  " ": "/",
                "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
                }
    MORSE = encode._MORSE
    return " ".join(MORSE.get(ch.upper(), "") for ch in text)


def sos(argv):
    """Only alphanumerical characters and space are valid input."""
    try:
        if len(argv) != 2:
            raise ValueError("You must provide only one (\" \") argument to the program. ")
        user_input = argv[1]
        is_valid_char = lambda ch: ch.isalnum() or ch.isspace()
        invalid = [ch for ch in user_input if not is_valid_char(ch)]
        if invalid:
            raise ValueError("the arguments are bad.")
        output = encode(user_input)
        print(output)
    except ValueError as e:
        print(f"AssertionError: {e}")


def main(argv):
    """Program takes a single string as an argument and encodes it into Morse Code."""
    sos(argv)


if __name__ == "__main__":
    main(sys.argv)
