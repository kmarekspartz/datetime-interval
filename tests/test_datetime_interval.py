from datetime import datetime, timedelta

from datetime_interval import Interval, forever, PeriodicInterval


def pairs(lst):
    i = iter(lst)
    first = prev = item = i.next()
    for item in i:
        yield prev, item
        prev = item
    yield item, first

now = datetime.now()
yesterday = now - timedelta(1)
tomorrow = now + timedelta(1)

last24s = [
    Interval(yesterday, now),
    Interval(yesterday, timedelta(1)),
    Interval(timedelta(1), now)
]

next24s = [
    Interval(now, tomorrow),
    Interval(now, timedelta(1)),
    Interval(timedelta(1), tomorrow)
]

for last24, last24_ in pairs(last24s):
    assert last24 is last24
    assert last24 is not last24_
    assert last24 == last24
    assert last24 == last24_
    assert last24 <= last24
    assert last24 <= last24_
    assert last24 >= last24
    assert last24 >= last24_


for next24, next24_ in pairs(next24s):
    assert next24 is next24
    assert next24 is not next24_
    assert next24 == next24
    assert next24 == next24_
    assert next24 <= next24
    assert next24 <= next24_
    assert next24 >= next24
    assert next24 >= next24_

def test_last_next(last24, next24):
    assert last24 is not next24
    assert next24 is not last24
    assert last24 != next24
    assert last24 < next24
    assert next24 > last24
    assert last24 <= next24
    assert next24 >= last24

for last24 in last24s:
    for next24 in next24s:
        test_last_next(last24, next24)

for last24 in last24s:
    assert yesterday in last24
    assert now in last24
    assert tomorrow not in last24
    next24 = last24 + timedelta(1)
    test_last_next(last24, next24)

for next24 in next24s:
    assert yesterday not in next24
    assert now in next24
    assert tomorrow in next24
    last24 = next24 - timedelta(1)
    test_last_next(last24, next24)



# IntervalComparisonError?