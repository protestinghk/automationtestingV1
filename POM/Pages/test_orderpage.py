from POM.Pages.test_basepage import Testbasepage
class Testorder(Testbasepage):

    button_addbskt_xpath = "//li[@class='post-160 product type-product status-publish has-post-thumbnail product_cat-selenium product_tag-ruby product_tag-selenium has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock downloadable taxable shipping-taxable purchasable product-type-simple']//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart'][contains(text(),'Add to basket')]"
    button_kart_xpath = "//span[@class='cartcontents']"
    button_chkout_xpath = "//a[@class='checkout-button button alt wc-forward']"

    def test_scroll(self):
        self.driver.execute_script("window.scrollBy(0,600)","")
    def test_addtobskt(self):
        self.driver.find_element_by_xpath(self.button_addbskt_xpath).click()
    def test_checkkart(self):
        self.driver.find_element_by_xpath(self.button_kart_xpath).click()
    def test_checkout(self):
        self.driver.find_element_by_xpath(self.button_chkout_xpath).click()