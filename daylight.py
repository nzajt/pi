from datetime import datetime

class Daylight:

    def __init__(self):
        self._now = datetime.now().time()

    @property
    def now(self):
        time = self._now
        percentage_of_day = time.hour / 24.0 + time.minute / (24.0*60.0) + time.second / (24.0*60.0*60.0) + time.microsecond / (24.0*60.0*60.0*1000000.0)
        return 1.00 - abs(.50 - percentage_of_day)
