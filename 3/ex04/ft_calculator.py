class calculator:
    """
    Perform vector arithmetic operations and dot product calculations.

    This utility class provides static methods for computing the dot product
    of two vectors, as well as component-wise addition and subtraction. All
    operations assume vectors of equal length and produce results in a
    human-readable format.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


"""
Vector calculation toolkit.

This class provides a collection of utility methods for performing
basic vector operations, including dot product, addition, and
subtraction. The methods are designed to operate on two vectors of
identical size and produce formatted output describing the result.

The tester invokes these methods directly from the class rather than
from an instance. For this reason, the methods are implemented as
static methods, allowing them to be called through the class itself
without creating an object beforehand. The class serves purely as a
namespace for related vector operations and is not intended to be
instantiated.

The exercise specification assumes that all input vectors are valid
and of equal length. Consequently, no error handling, input
validation, or edge-case management is required. All calculations
must be implemented using Python's built-in language features without
relying on external libraries or third-party dependencies.
"""
