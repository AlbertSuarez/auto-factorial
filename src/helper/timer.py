import time

from src.helper import log


class Timer:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.time = self.end - self.start
        log.info(f'{self.name}: {self.time:.6f}s')
