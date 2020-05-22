import pytest
import allure
import time
from selenium import webdriver
import sys
import moment

sys.path.append("D:/automationtestingV1")
from POM.Pages.test_launchpage import TestLaunchPage
from Utils import Utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_launch(self):
        print("test started")

        lp = TestLaunchPage(self.driver)
        try:
            lp.test_entermailid(utils.EMAIL)
            lp.test_clickenter()
            links = self.driver.find_elements_by_tag_name("a")
            actual_links = len(links)
            #actual number of links 43
            expected_links = 42
            assert actual_links==expected_links
        except:

            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot = test_name+"-"+current_time
            print("There was an exception: not able to move next page")
            allure.attach(self.driver.get_screenshot_as_png(),name = screenshot,attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("D:/automationtestingV1/Screenshot/"+screenshot+".png")
            raise