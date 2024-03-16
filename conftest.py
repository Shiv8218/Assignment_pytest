import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.loginPage import Login
from Pages.exceptionsPage import Exceptions
from Pages.apiMethodsPage import ApiMethods
from Utilities import ReadConfigurations


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


@pytest.fixture
def setup_and_teardown(request, endpoint):
    browser = ReadConfigurations.readconfig("basic info","browser")
    global driver
    if browser.capitalize() == "Chrome":
        driver = webdriver.Chrome()
    elif browser.capitalize() == "Firefox":
        driver = webdriver.Firefox()
    elif browser.capitalize() == "Edge":
        driver = webdriver.Edge()
    else:
        print("This is not a valid Browser.")
    driver.maximize_window()

    base_url = ReadConfigurations.readconfig("basic info","base_url")
    uri = base_url+endpoint

    driver.get(uri)
    driver.implicitly_wait(10)
    if "login" in uri:
        page_object = Login(driver=driver)
    elif "exceptions" in uri:
        page_object = Exceptions(driver=driver)
    else:
        pass
    request.cls.page_object = page_object
    driver.implicitly_wait(10)
    yield
    driver.quit()


@pytest.fixture
def api_fixture(request):
    page_object = ApiMethods()
    request.cls.page_object = page_object