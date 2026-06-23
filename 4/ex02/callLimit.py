def callLimit(limit: int):
    """Create a decorator that limits the number of function calls.

    Initializes a call counter and returns a decorator capable of
    restricting how many times a function may be executed. Once the
    specified limit is reached, further calls are blocked.
    """
    count = 0
    def callLimiter(function):
        """Decorate a function with call-count restrictions.

        Wraps the provided function with logic that tracks how many times
        it has been invoked and enforces the maximum number of allowed
        executions defined by the enclosing decorator.
        """
        def limit_function(*args: Any, **kwds: Any):
            """Execute the wrapped function while enforcing a call limit.

            Forwards all positional and keyword arguments to the wrapped
            function and increments the shared call counter after a successful
            execution. If the maximum number of allowed calls has been reached,
            an error message is displayed and the function is not executed.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            result = function(*args, **kwds)
            count += 1
            return result
        return limit_function
    return callLimiter


"""
NOTES:

# *args and **kwargs ensure compatibility with any function signature.

# Python effectively transforms:

@callLimit(3)
def f():
    ...

 into:

f = callLimit(3)(f)

- callLimit(3) returns the decorator 'callLimiter'.
- callLimiter(f) returns the wrapped function 'limit_function'.

- If 'return limit_function' is omitted, callLimiter(f) returns None,
- so Python effectively does:

f = None

- Calling f() then raises:
- TypeError: 'NoneType' object is not callable


The chain is:

    callLimit(limit)
        ↓ returns
    callLimiter
        ↓ receives original function
    limit_function
        ↓ becomes the new function
        f

# Returning values
* 'return limit_function' → gives back the wrapped function.
* 'return result' → preserves the original function's return value.

# preserved variable:
  'nonlocal count':
 * count is a free variable captured by a closure.
 * nonlocal binds 'count' to the variable defined in the enclosing
  function, enabling the closure to preserve and update state.
 * A closure is:
    - an inner function (limit_function)
    - together with the variables it remembers from outer scopes
    (count, limit, and potentially function)

The reason count survives between calls is that limit_function closes over it.

"""
