import pytest
import os
import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',default=None,
                     help='Choose browser:chrome of firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--window-size=1600,800")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--window-size=1900,1920")
        browser = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nStopping test")
    browser.quit()



@pytest.fixture()
def test_driver_1900():
    print ("\nStart for test driver 1920x1080")
    options_1 = Options()
    service_1 = Service(executable_path=ChromeDriverManager().install())
    options_1.add_argument("--incognito")
    options_1.page_load_strategy = 'eager'
    options_1.add_argument("--window-size=1920,1080")
    driver= webdriver.Chrome(options=options_1, service=service_1)
    yield driver
    print("\nStop for test driver 1920x1080")
    driver.quit()


@pytest.fixture(scope="function")
def test_driver_1600():
    print("\nStarting for test driver 1600x800")
    options = Options()
    service = Service(executable_path=GeckoDriverManager().install())
    options.add_argument("--window-size=1600,800")
    options.page_load_strategy = 'eager'
    driver = webdriver.Firefox(options=options, service=service)
    yield driver
    print("\nStopping for test driver 1600x800")
    driver.quit()
