import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.loginPage import Login
from Pages.exceptions import Exceptions


# This is for taking the failure Screenshot

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)



@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.implicitly_wait(10)
    lp = Login(driver=driver)
    request.cls.lp = lp
    yield
    driver.quit()


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    driver.implicitly_wait(10)
    ex = Exceptions(driver=driver)
    request.cls.ex = ex
    yield
    driver.quit()