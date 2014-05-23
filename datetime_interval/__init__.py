"""
The builtin `datetime` module provides classes for points in time (`date`, and
`datetime`) as well as durations (`timedelta`), but it does not account for
time durations at a specific point. This module provides `Interval`, which
contains a start and end `date` or `datetime`, and a duration `timedelta`.
This is useful for representing calendar events. This module also provides
`PeriodicInterval` which can be used for repeating events, by containing a
period `timedelta` and a count of occurrences (either an `int` or `forever`).
"""

from datetime_interval.interval import Interval
from datetime_interval.periodic_interval import forever, PeriodicInterval
