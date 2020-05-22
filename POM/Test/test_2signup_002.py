import allure
import pytest
import time
import sys



sys.path.append("D:/automationtestingV1")

from POM.Pages.test_launchpage import TestLaunchPage
from POM.Pages.test_signuppage import Testsignuppage
from Utils import Utils as utils



@pytest.mark.usefixtures("test_setup")
class TestSignup():

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup(self):

        lp = TestLaunchPage(self.driver)
        lp.test_entermailid(utils.EMAIL)
        lp.test_clickenter()
        sg = Testsignuppage(self.driver)
        sg.test_firstname("john")
        sg.test_lastname("john")
        sg.test_email(utils.EMAIL)
        sg.test_phone(4178444719)
        sg.test_radiobutton()
        sg.test_checkbox()
        sg.test_languages()
        sg.test_dropdowncountries()
        sg.test_dropdownskills()
        sg.test_dropdownyear()
        sg.test_dropdownmonth()
        sg.test_dropdowndate()
        sg.test_firstpassword("Qwerty123")
        sg.test_secondpassword("Qwerty123")
        sg.test_submit()

        print("Test run")
