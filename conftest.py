# conftest.py

import pytest
from utils.driver_factory import DriverFactory
from utils.browserstack_driver_factory import BrowserStackDriverFactory

@pytest.fixture()
def driver():
    drv = DriverFactory.get_driver()
    yield drv
    drv.quit()

@pytest.fixture()
def browserstack_driver():
    drv = BrowserStackDriverFactory.get_driver()
    yield drv
    drv.quit()