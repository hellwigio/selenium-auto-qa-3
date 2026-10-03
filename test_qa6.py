import pytest
from selenium import webdriver

from pages.saucedemo import CartPage, CheckoutPage, InventoryPage, LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1440,1000")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_checkout_total(driver):
    LoginPage(driver).login()
    inventory = InventoryPage(driver)
    inventory.add_products()
    inventory.open_cart()
    CartPage(driver).checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_details()
    assert checkout.total() == "Total: $58.29"
