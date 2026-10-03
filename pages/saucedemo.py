from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self):
        self.driver.get(self.URL)
        self.wait.until(lambda d: d.find_element(By.ID, "user-name")).send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_products(self):
        for product in ("sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"):
            self.wait.until(lambda d: d.find_element(By.ID, f"add-to-cart-{product}")).click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.driver.execute_script("arguments[0].click()", self.wait.until(lambda d: d.find_element(By.ID, "checkout")))


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_details(self):
        for field, value in (("first-name", "Dmitriy"), ("last-name", "Hellwig"), ("postal-code", "10115")):
            element = self.wait.until(lambda d: d.find_element(By.ID, field))
            self.driver.execute_script(
                "Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(arguments[0], arguments[1]); arguments[0].dispatchEvent(new Event('input', {bubbles: true}))",
                element,
                value,
            )
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, "continue"))

    def total(self):
        return self.wait.until(lambda d: d.find_element(By.CLASS_NAME, "summary_total_label")).text
