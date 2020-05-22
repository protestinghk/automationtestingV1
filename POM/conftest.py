import pytest
from Utils import Utils as utils
import sys
sys.path.append("D:/automationtestingV1")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name ex:- chrome or firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="D:/automationtestingV1/POM/Drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="D:/automationtestingV1/POM/Drivers/geckodriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(utils.URL)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed Successfully")