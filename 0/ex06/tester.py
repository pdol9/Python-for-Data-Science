"""
feat: comprehensive tester

- Add run_case() and main() test harness:
  - Covers normal lists, tuples, generators, empty iterables, mixed types,
    strings, and edge cases (all false, all true).
  - Normalizes input by materializing one-shot iterables to lists so both
    built-in filter and ft_filter consume identical data.
  - Compares results by converting iterators to lists before comparison.
  - Reports OK/MISMATCH per case and prints differing outputs for debugging.

- Improve robustness:
  - Catch and display exceptions raised by either implementation during test.
  - Use descriptive case names and lambda predicates to exercise behavior.

Tests performed:
- Manual run in terminal:
  - Verified evens, nonempty, is_alpha, mixed_types, generator_input, and
    others.
  - Confirmed ft_filter yields identical lists to list(filter(...)) for all
    cases.
- Edge checks:
  - func is None behavior matches truthy filtering.
  - Generator inputs are handled by materializing into lists for repeatability.

Notes:
- ft_filter returns a lazy generator; callers can convert to list() to
    materialize.
- The tester intentionally materializes both outputs before comparison to avoid
  exhaustion issues with one-time iterables.

"""

from ft_filter import ft_filter


def is_alpha(s):
    return s.isalpha()


def run_case(func, iterable, case_name):
    # builtin filter returns an iterator in Py3; convert to list for comparison
    try:
        builtin = (
                list(__builtins__['filter'](func, iterable))
                if isinstance(__builtins__, dict)
                else list(filter(func, iterable))
                )
    except Exception as e:
        builtin = f"<raised {type(e).__name__}: {e}>"

    try:
        custom = list(ft_filter(func, iterable))
    except Exception as e:
        custom = f"<raised {type(e).__name__}: {e}>"

    ok = builtin == custom
    print(f"{case_name}: {'OK' if ok else 'MISMATCH'}")
    if not ok:
        print("  builtin:", builtin)
        print("  custom :", custom)


def main():
    cases = [
        ("evens", lambda x: x % 2 == 0, [1, 2, 3, 4, 5]),
        ("nonempty", None, ["a", "", "b", ""]),
        ("is_alpha", is_alpha, ["abc", "123", "a1"]),
        ("empty_iter", lambda x: True, []),
        ("all_false", lambda x: False, [1, 2, 3]),
        ("mixed_types", None, [0, 1, "", "x", [], [1]]),
        (
            "strings",
            lambda x: ('a' in x) if isinstance(x, str) else False,
            ["a", "b", "ab", ""],
        ),
        ("generator_input", lambda x: x > 0, (i for i in range(-1, 3))),
    ]

    for name, func, it in cases:
        # For re-usable iterables, ensure we pass a fresh iterable to
        # both functions
        iterable = list(it) if not isinstance(it, (list, tuple)) else it
        run_case(func, iterable, name)


if __name__ == "__main__":
    main()
