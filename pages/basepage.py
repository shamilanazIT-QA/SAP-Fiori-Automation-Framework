from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # 15 seconds is a good 'sweet spot' for SAP Fiori
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        # Good choice using element_to_be_clickable for Fiori buttons
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)

    def is_element_displayed(self, locator):
        try:
            # We use a fresh, shorter wait so we don't hang for 15s
            # if a popup ISN'T there.
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return