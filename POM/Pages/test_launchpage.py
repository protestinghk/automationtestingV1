from POM.Pages.test_basepage import Testbasepage

class TestLaunchPage(Testbasepage):
    textbox_email_xpath = "//input[@id='email']"
    image_button_id = "enterimg"

    def test_entermailid(self,mail):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(mail)

    def test_clickenter(self):
        self.driver.find_element_by_id(self.image_button_id).click()

