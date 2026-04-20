import pytest
from selenium.webdriver.common.by import By

from pages.fiori_home_page import FioriHomePage


def test_sap_shopping_flow(driver):
    fiori = FioriHomePage(driver)

    # 1. Open the specific SAP Demo URL
    driver.get("https://sdk.openui5.org/test-resources/sap/m/demokit/cart/webapp/index.html")

    # 2. Navigate Categories
    fiori.select_accessories()

    # 3. Select Product
    fiori.select_beam_breaker()

    # 4. Add to Cart
    fiori.add_to_cart()

    fiori.handle_popup()

    fiori.open_cart()

    # 3. Final Assertion (The Proof!)
    assert fiori.verify_product_in_cart(), "FAILURE: Beam Breaker B-1 was not found in the cart!"

    print("SUCCESS: Product added and verified in cart!")
    print("\n--- TEST COMPLETE ---")
    input("Check the browser! Press Enter here in the terminal to close it...")
