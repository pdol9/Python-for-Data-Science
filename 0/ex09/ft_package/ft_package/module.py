from typing import Iterable, Any

def count_in_list(items: Iterable[Any], value: Any) -> int:
    """
    Return how many times `value` appears in `items`.
    Works with any iterable (lists, tuples, generators).
    """
    # Try fast path if it's a sequence with count()
    try:
        return items.count(value)  # type: ignore[attr-defined]
    except Exception:
        # Fallback: iterate
        return sum(1 for x in items if x == value)
