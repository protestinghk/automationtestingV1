from selenium.webdriver.support.ui import Select
from POM.Pages.test_basepage import Testbasepage
class Testsignuppage(Testbasepage):
    textbox_firstname_xpath = "//input[@placeholder='First Name']"
    textbox_lastname_xpath = "//input[@placeholder='Last Name']"
    textbox_address_xpath = "//textarea[@class='form-control ng-pristine ng-valid ng-touched']"
    textbox_mail_xpath = "//input[@class='form-control ng-pristine ng-untouched ng-valid-email ng-invalid ng-invalid-required']"
    textbox_phone_xpath = "//input[@class='form-control ng-pristine ng-untouched ng-invalid ng-invalid-required ng-valid-pattern']"
    radiobutton_male_xpath = "//label[1]//input[1]"
    checkbox_movies_id = "checkbox2"
    dropdown_countries_id = "countries"
    textbox_firstpassword_id = "firstpassword"
    textbox_secondpassword_id = "secondpassword"
    button_submit_id = "submitbtn"
    dropdown_languages_xpath = "//div[@id='msdd']"
    dropdown_english_xpath = "//a[contains(text(),'English')]"
    dropdown_skills_xpath = "//select[@id='Skills']"
    dropdown_year_xpath = "//select[@id='yearbox']"
    dropdown_month_xpath = "//select[@placeholder='Month']"
    dropdown_date_xpath = "//select[@id='daybox']"


    def test_firstname(self,firstname):
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)
    def test_lastname(self,lastname):
        self.driver.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(lastname)
    def test_address(self,address):
        self.driver.find_element_by_xpath(self.textbox_address_xpath).send_keys(address)
    def test_email(self,email):
        self.driver.find_element_by_xpath(self.textbox_mail_xpath).send_keys(email)
    def test_phone(self,phone):
        self.driver.find_element_by_xpath(self.textbox_phone_xpath).send_keys(phone)
    def test_radiobutton(self):
        self.driver.find_element_by_xpath(self.radiobutton_male_xpath).click()
    def test_checkbox(self):
        self.driver.find_element_by_id(self.checkbox_movies_id).click()

    def test_languages(self):
        self.driver.find_element_by_xpath(self.dropdown_languages_xpath).click()
        self.driver.find_element_by_xpath(self.dropdown_english_xpath).click()

    def test_dropdowncountries(self):
        element = self.driver.find_element_by_id(self.dropdown_countries_id)
        drp = Select(element)
        drp.select_by_visible_text("Canada")

    def test_dropdownskills(self):
        elem = self.driver.find_element_by_xpath(self.dropdown_skills_xpath)
        drps = Select(elem)
        drps.select_by_visible_text("Android")

    def test_dropdownyear(self):
        eleme = self.driver.find_element_by_xpath(self.dropdown_year_xpath)
        drpy = Select(eleme)
        drpy.select_by_visible_text("1933")

    def test_dropdownmonth(self):
        elemen = self.driver.find_element_by_xpath(self.dropdown_month_xpath)
        drpm = Select(elemen)
        drpm.select_by_visible_text("May")

    def test_dropdowndate(self):
        el = self.driver.find_element_by_xpath(self.dropdown_date_xpath)
        drpd = Select(el)
        drpd.select_by_visible_text("7")

    def test_firstpassword(self,password1):
        self.driver.find_element_by_id(self.textbox_firstpassword_id).send_keys(password1)
    def test_secondpassword(self,password2):
        self.driver.find_element_by_id(self.textbox_secondpassword_id).send_keys(password2)
    def test_submit(self):
        self.driver.find_element_by_id(self.button_submit_id).click()