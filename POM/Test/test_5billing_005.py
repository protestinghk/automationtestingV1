#@pytest.mark.skip
import allure
import pytest
import time
import sys
sys.path.append("D:/automationtestingV1")

from POM.Pages.test_billingpage import Testbilling
from POM.Pages.test_launchpage import TestLaunchPage
from POM.Pages.test_orderpage import Testorder
from POM.Pages.test_practsite import Testpract
from POM.Pages.test_signuppage import Testsignuppage
from Utils import Utils as utils

@pytest.mark.usefixtures("test_setup")
class TestBilling():

    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.NORMAL)
    def test_billing(self):
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
        time.sleep(5)
        pp = Testpract(self.driver)
        pp.test_clickpractlink()
        op = Testorder(self.driver)
        op.test_scroll()
        op.test_addtobskt()
        op.test_checkkart()
        op.test_checkout()

        bp = Testbilling(self.driver)
        bp.test_enterfirstname("john")
        bp.test_enterlastname("john")
        bp.test_entercompany("smart company")
        bp.test_enteremail(utils.EMAIL)
        bp.test_enterphone("4178444719")
        bp.test_enteraddress("ontario")
        bp.test_entertown("toronto")
        bp.test_dropdownprovience()
        bp.test_enterzipcode("m4h5g5")
        bp.test_selectcash()
        bp.test_clickplaceorder()
        ss =Testscreenshot(self.driver)
        ss.test_takescreenshot()