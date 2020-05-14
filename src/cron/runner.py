from src.helper.timer import Timer
from src.selenium import helper


def run():
    with Timer('Accessing to Log in page'):
        browser = helper.init_browser()
