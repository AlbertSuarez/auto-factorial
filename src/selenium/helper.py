from selenium.webdriver import Firefox, DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from src.config import FACTORIAL_WEBSITE_INIT, SELENIUM_EXECUTABLE_PATH, SELENIUM_BINARY_PATH


def init_browser():
    # Set up options
    opts = Options()
    opts.headless = True
    assert opts.headless  # Operating in headless mode
    # Set up capabilities
    capabilities = DesiredCapabilities().FIREFOX
    capabilities['marionette'] = False
    # Create browser instance
    browser = Firefox(
        options=opts,
        firefox_binary=FirefoxBinary(SELENIUM_BINARY_PATH),
        executable_path=SELENIUM_EXECUTABLE_PATH,
        capabilities=capabilities
    )
    browser.get(FACTORIAL_WEBSITE_INIT)
    return browser
