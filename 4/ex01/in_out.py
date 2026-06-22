def square(x: int | float) -> int | float:
    """
    Calculates the square of the input and returns the resulting value.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Computes x raised to the power of x and returns the result.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a stateful function that repeatedly applies an operation.

    Initializes a closure with a starting value and a transformation
    function. Each call to the returned function applies the operation
    to the previous result and returns the updated value.
    """
    count = 0

    def inner() -> float:
        """Apply the stored operation to the current value.

        On the first invocation, the operation is applied to the initial
        value provided to the enclosing function. On subsequent calls,
        the operation is applied to the previously computed result,
        allowing the state to persist across invocations.
        """
        nonlocal count

        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count

    return inner
