import time


class TimerError(Exception):
    'Exception'


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """ Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f'Timer is running.')

        self._start_time = time.perf_counter()

    def finish(self):
        """  Stop tne timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f'Time is not running.')

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f'Elapsed time: {elapsed_time:.4f} seconds')
