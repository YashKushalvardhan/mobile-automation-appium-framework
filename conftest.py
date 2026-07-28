import pytest
import json
from utils.driver_factory import DriverFactory
from utils.browserstack_driver_factory import BrowserStackDriverFactory

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture()
def driver():
    drv = DriverFactory.get_driver()
    yield drv
    drv.quit()


@pytest.fixture()
def browserstack_driver(request):
    drv = BrowserStackDriverFactory.get_driver()
    yield drv

    # Report the actual pass/fail status back to BrowserStack.
    # Without this, BrowserStack has no way to know whether our
    # Pytest assertions passed or failed — it only sees that the
    # session ran without crashing, hence "Unknown" status.
    test_failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    status = "failed" if test_failed else "passed"
    reason = "Test failed" if test_failed else "Test passed successfully"

    drv.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "%s", "reason": "%s"}}' % (status, reason))

    drv.quit()