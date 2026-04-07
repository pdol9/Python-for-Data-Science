"""
feat: implement ft_filter iterator

- Implement ft_filter to mirror built-in filter behavior:
  - Accepts func (callable or None) and iterable.
  - Returns a generator (lazy iterator) that yields items for which
    func(item) is truthy, or yields truthy items when func is None.
  - Uses no imports; uses generator expression and idiomatic checks.
"""


def ft_filter(function, iterable):
    # func: expected to be a callable (predicate) or None
    # iterable: any object you can iterate over (list, tuple, string,
    # generator, etc.).
    """Return an iterator yielding those items of iterable for which function
    (item) is true. If function is None, return the items that are true."""
    if function is None:        # func=None means "keep truthy items".
        return (x for x in iterable if x)
    return (x for x in iterable if function(x))


"""
Return type (iterator)

An iterator is an object that yields items one at a time, on demand, instead
of producing the whole collection immediately. Key points:

Key points

1. Laziness: an iterator computes each item only when requested (e.g., by
next()). That can save memory and work for large or infinite sequences.
Built-in filter in Python 3 returns an iterator (a filter object), not a list.
You can iterate over it once or convert it to a list with list(filter(...)).

2. Creation vs. consumption:

- Eager (list): all results are computed and stored immediately; uses memory
proportional to the number of results.
- Lazy (iterator): results are computed as you iterate; memory usage is small.

3. How to make one:

    Generator expression: (x for x in iterable if predicate(x))

4. When to use which:

- Return a list if callers expect indexable/len-able results or you need all
results immediately.
- Return an iterator to be memory-efficient or to compose pipelines (map/
filter/itertools), e.g. when you process items sequentially or when the full
result set would be large.
"""
