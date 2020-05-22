from POM.Pages.test_basepage import Testbasepage
from selenium.webdriver.support.ui import Select

class Testbilling(Testbasepage):
    textbox_first_id = "billing_first_name"
    textbox_last_id = "billing_last_name"
    textbox_company_id = "billing_company"
    textbox_email_id = "billing_email"
    textbox_phone_id = "billing_phone"
    textbox_address_id = "billing_address_1"
    textbox_town_id = "billing_city"
    province_xpath = "//div[@id='s2id_billing_state']//b"
    province_search_xpath = "//input[@id='s2id_autogen2_search']"  # ontario
    ontario_xpath = "//span[@class='select2-match']"
    #dropdown_provience_xpath = "//div[@id='select2-drop-mask']"
    textbox_zipcode_id = "billing_postcode"
    radiobutton_cash_xpath = "//input[@id='payment_method_cod']"
    button_placeorder_xpath = "//input[@id='place_order']"

    def test_enterfirstname(self,firstname):
        self.driver.find_element_by_id(self.textbox_first_id).send_keys(firstname)
    def test_enterlastname(self,lastname):
        self.driver.find_element_by_id(self.textbox_last_id).send_keys(lastname)
    def test_entercompany(self,company):
        self.driver.find_element_by_id(self.textbox_company_id).send_keys(company)
    def test_enteremail(self,email):
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)
    def test_enterphone(self,phone):
        self.driver.find_element_by_id(self.textbox_phone_id).send_keys(phone)
    def test_enteraddress(self,address):
        self.driver.find_element_by_id(self.textbox_address_id).send_keys(address)
    def test_entertown(self,townname):
        self.driver.find_element_by_id(self.textbox_town_id).send_keys(townname)
    def test_dropdownprovience(self):
        #element = self.driver.find_element_by_xpath(self.dropdown_provience_xpath)
        #drpdwn = Select(element)
        #drpdwn.select_by_
        self.driver.find_element_by_xpath(self.province_xpath).click()
        self.driver.find_element_by_xpath(self.province_search_xpath).send_keys("Ontario")
        self.driver.find_element_by_xpath(self.ontario_xpath).click()
    def test_enterzipcode(self,zipcode):
        self.driver.find_element_by_id(self.textbox_zipcode_id).send_keys(zipcode)
    def test_selectcash(self):
        self.driver.find_element_by_xpath(self.radiobutton_cash_xpath).click()
    def test_clickplaceorder(self):
        self.driver.find_element_by_xpath(self.button_placeorder_xpath).click()