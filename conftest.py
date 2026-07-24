# conftest.py

import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture()
def driver():
    drv = DriverFactory.get_driver()
    yield drv
    drv.quit()