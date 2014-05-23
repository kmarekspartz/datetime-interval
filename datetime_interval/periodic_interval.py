"""
PeriodicInterval represents recurring intervals.
"""

from datetime import timedelta

from datetime_interval.interval import Interval


forever = float('inf')  # Represent infinite occurrences


class PeriodicInterval(Interval):
    """
    A periodic interval is an interval that starts every period.
    """
    is_periodic = True

    occurrences = None  # forever, or a positive int
    period = None  # timedelta

    @property
    def is_bounded(self):
        """
        Is self a bounded PeriodicInterval?
        """
        self._invariants()
        return self.occurrences is not forever

    @property
    def is_unbounded(self):
        """
        Is self an unbounded PeriodicInterval?
        """
        self._invariants()
        return not self.is_bounded

    def _invariants(self):
        """
        some assertions
        """
        super(PeriodicInterval, self)._invariants()
        assert self.is_periodic
        assert isinstance(self.occurrences, int) or self.occurrences is forever
        assert self.occurrences >= 0
        assert isinstance(self.period, timedelta)
        assert self._timedelta_is_positive(self.period)
