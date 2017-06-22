from datetime import datetime

class Daylight:

    def __init__(self):
        self._now = datetime.now().time()

    @property
    def now(self):
        return self._now

