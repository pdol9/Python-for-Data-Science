def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D list, prints its shape,
    and returns a sliced version.
    """

    # check top-level type
    if not isinstance(family, list):
        raise TypeError("family must be a list")

    # empty list case
    if len(family) == 0:
        raise ValueError("family is empty")

    # verify all rows are lists
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must contain lists")

    # verify rectangular shape
    row_len = len(family[0])

    for row in family:
        if len(row) != row_len:
            raise ValueError("all rows must have the same size")

    # original shape
    print(f"My shape is : ({len(family)}, {row_len})")

    # slicing
    sliced = family[start:end]

    # new shape
    print(f"My new shape is : ({len(sliced)}, {row_len})")

    return sliced
