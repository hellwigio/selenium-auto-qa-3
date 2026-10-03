import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_button_text(driver):
    driver.get("http://uitestingplayground.com/textinput")
    driver.find_element(By.ID, "newButtonName").send_keys("ITCH")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    assert button.text == "ITCH"


def test_loading_images(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    images = WebDriverWait(driver, 10).until(
        lambda d: (images if len(images := d.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 3
                   and all(i.get_attribute("complete") == "true" for i in images) else False)
    )
    assert images[2].get_attribute("alt") == "award"
