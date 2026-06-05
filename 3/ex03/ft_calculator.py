class calculator:
    """
    User-defined class which overloads Python's arithmetic operators so that
    a calculator object behaves like a vector. Then a scalar is applied to
    every element of that list and prints the resulting vector.
    """
    def __init__(self, vector):
        self.v = vector

    def __add__(self, object) -> None:
        self.v = [item + object for item in self.v]
        print(self.v)

    def __mul__(self, object) -> None:
        self.v = [item * object for item in self.v]
        print(self.v)

    def __sub__(self, object) -> None:
        self.v = [item - object for item in self.v]
        print(self.v)

    def __truediv__(self, object) -> None:
        try:
            self.v = [item / object for item in self.v]
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return
        print(self.v)
