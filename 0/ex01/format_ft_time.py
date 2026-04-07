from datetime import datetime, timezone
import time

"""
Expected output:
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific
notation
Oct 21 2022$
"""

now = datetime.now(timezone.utc)
seconds_double = float(now.timestamp())
seconds_double = float(now.timestamp())
seconds_sci = float(time.time())

print("Seconds since January 1, 1970: " + f"{seconds_double:,.4f}" + " or " +
      f"{seconds_sci:.2e}" + " in scientific notation")
print(now.strftime("%b %d %Y"))

# print(now.strftime("%Y-%m-%d %H:%M:%S"))   # "2026-03-28 12:34:56"
# print(now.strftime("%Y-%m-%d"))           # "2026-03-28"
# print(now.isoformat())                   # "2026-03-28T12:34:56.789012+00:00"

# print( f"{seconds_sci:.6e}")  # e.g., 1.702345e+09
