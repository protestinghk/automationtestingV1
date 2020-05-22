from POM.Pages.test_basepage import Testbasepage
class Testpract(Testbasepage):
    link_practise_linktext = "Practice Site"

    def test_clickpractlink(self):
        self.driver.find_element_by_link_text(self.link_practise_linktext).click()
