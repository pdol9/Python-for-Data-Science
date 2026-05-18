def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Return a list of BMI values."""
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans -> True if BMI value is above the limit."""
    return [value > limit for value in bmi]
