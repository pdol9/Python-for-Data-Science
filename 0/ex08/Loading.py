import os


def _os_write(s: str):
    """
    Writes the given string to stdout's file descriptor (fd 1) using os.write
    after encoding to bytes, performing an immediate, unbuffered output.
    """
    os.write(1, s.encode())


def _fmt_time(t: float) -> str:
    """
    Format a time duration (seconds) into a short human-readable string.

    Behavior:
    - Takes a non-negative number of seconds and returns either "H:MM:SS"
      (if hours are present) or "MM:SS" (if less than one hour).
    - Rounds down to whole seconds for display.
    - Ensures negative or NaN inputs are clamped to zero.

    Args:
    - t: Duration in seconds (float).

    Returns:
    - A formatted time string suitable for compact progress output.
    """
    s = int(max(0.0, t))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def _now_cpu_seconds() -> float:
    """
    Return the process CPU time in seconds.

    Behavior:
    - Uses os.times() and sums the process's user, system, and children
      user/system times to produce a single CPU-seconds value.
    - This is NOT wall-clock (real) time; it measures CPU time consumed
      by the process and its terminated children.
    - Useful when only the os module is permitted and a timing source is
      required.

    Returns:
    - Float: total process CPU time in seconds (user + system + children).
    """
    # sum of user + system + children user + children system (process CPU time)
    t = os.times()
    return t.user + t.system + t.children_user + t.children_system


def ft_tqdm(lst: range) -> None:
    """
    Generator that iterates the given range while printing a single-line
    tqdm-like progress bar to stdout.

    Behavior and features:
    - Prints and updates a single progress line (in-place) using carriage
      return, ensuring previous output is overwritten by padding shorter lines.
    - Adapts bar width to the current terminal width via os.get_terminal_size()
    - Displays: percentage, Unicode block progress bar, counter (idx/total),
      elapsed CPU time, estimated remaining CPU time, and iterations/sec.
    - Uses process CPU time (from _now_cpu_seconds) for elapsed/ETA/rate.
      This means timings reflect CPU usage, not wall-clock time; for
      I/O/sleep-heavy tasks the reported rate/ETA may be meaningless.
    - Writes directly to stdout file descriptor using os.write (bytes).
    - On completion prints a final full bar with a newline.

    Args:
    - lst: range (or any sequence-like object with len() and iteration) to
      iterate.

    Returns:
    - Generator that yields the items from `lst` and updates the progress bar.

    Notes:
    - The function is not allowed to import time/sys and relies only on os
    """
    total = len(lst)
    start = _now_cpu_seconds()
    prev_len = 0
    for idx, i in enumerate(lst, 1):
        now = _now_cpu_seconds()
        elapsed = now - start
        rate = idx / elapsed if elapsed > 1e-12 else float('inf')
        # Estimated remaining time in seconds
        rem = (total - idx) / rate if rate not in (0.0, float('inf')) else 0.0

        cols = os.get_terminal_size().columns
        percent = int(idx * 100 / total)
        stats = f"[{_fmt_time(elapsed)}<{_fmt_time(rem)}, {rate:6.2f}it/s]"
        counter = f" {idx}/{total} "

        reserved = len(f"{percent:3d}%|") + len(counter) + len(stats) + 2
        bar_width = max(10, cols - reserved)
        filled = int((idx / total) * bar_width)
        bar = "█" * filled + " " * (bar_width - filled)

        line = f"{percent:3d}%|{bar}|{counter}{stats}"
        if len(line) < prev_len:
            line = line + " " * (prev_len - len(line))
        prev_len = len(line)

        _os_write("\r" + line)
        yield i

    total_elapsed = _now_cpu_seconds() - start
    rate = total / total_elapsed if total_elapsed > 1e-12 else float('inf')
    stats = f"[{_fmt_time(total_elapsed)}<{_fmt_time(0)}, {rate:6.2f}it/s]"
    cols = os.get_terminal_size().columns
    reserved = len("100%|") + len(f" {total}/{total} ") + len(stats) + 2
    bar_width = max(10, cols - reserved)
    bar = "█" * bar_width
    final_line = f"100%|{bar}| {total}/{total} {stats}"
    if len(final_line) < prev_len:
        final_line = final_line + " " * (prev_len - len(final_line))
    _os_write("\r" + final_line + "\n")


"""
An overview of python feature called generator

A Python generator is a special function that returns an iterator to produce a
sequence of values lazily, meaning it generates items one at a time only when
requested rather than storing them all in memory.  This is achieved using the
yield statement, which pauses the function's execution, saves its state, and
returns a value; the function resumes from that point on the next call to
next() or during iteration.

Generators are defined like regular functions but use yield instead of return,
allowing them to handle large datasets, infinite sequences, and data streams
efficiently without memory overload.  There are two primary ways to create
them: generator functions (using def and yield) and generator expressions
(using parentheses () instead of list comprehension brackets []).
"""
