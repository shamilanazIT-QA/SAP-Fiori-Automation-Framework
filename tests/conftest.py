import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = "function")
def driver():
    options = Options()
    options.binary_location = r"C:\Users\shamila\AppData\Local\chrome\chrome.exe"
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(r"C:\Users\shamila\AppData\Local\chromedriver\chromedriver.exe")

    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


