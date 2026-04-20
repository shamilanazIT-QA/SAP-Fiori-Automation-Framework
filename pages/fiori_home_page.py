from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class FioriHomePage(BasePage):
    ACCESSORIES_CAT = (By.XPATH, "//div[text()='Accessories']")
    BEAM_BREAKER = (By.XPATH, "//span[contains(text(), 'Beam Breaker B-1')]")

    # Use 'contains' to be safer against small text changes
    ADD_TO_CART_BTN = (By.XPATH, "//button//bdi[contains(text(), 'Cart')]")

    # Fixed syntax: contains(text(), 'Text')
    # Change your popup buttons to be just as flexible
    OK_BUTTON = (By.XPATH, "//*[contains(text(), 'OK')]")
    CANCEL_BUTTON = (By.XPATH, "//*[contains(text(), 'Cancel')]")
    CART_BUTTON = (By.XPATH, "//button[contains(@id, 'cart')]")

    # The product name inside the cart list
    PRODUCT_IN_CART = (By.XPATH, "//ul//*[contains(text(), 'Beam Breaker B-1')]")


    def select_accessories(self):
        self.click_element(self.ACCESSORIES_CAT)

    def select_beam_breaker(self):
        self.click_element(self.BEAM_BREAKER)

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BTN)

    def handle_popup(self):
        """Wait for the popup to appear and click OK."""
        try:
            # We use our BasePage click_element which has the wait built-in
            self.click_element(self.OK_BUTTON)
            print("Popup handled by clicking OK.")
        except Exception as e:
            print(f"Could not handle popup: {e}")

    def open_cart(self):
        self.click_element(self.CART_BUTTON)

    def verify_product_in_cart(self):
        return self.is_element_displayed(self.PRODUCT_IN_CART)