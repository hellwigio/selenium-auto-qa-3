import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1440,1000")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_text_in_iframe(driver):
    text = "semper posuere integer et senectus justo curabitur."
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))

    element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    assert text in element.text


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 10)
    frame = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "iframe.demo-frame"))
    driver.switch_to.frame(frame)

    photo = wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, "#gallery li")[0])
    trash = driver.find_element(By.ID, "trash")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", photo)
    ActionChains(driver).move_to_element(photo).click_and_hold().move_to_element(trash).release().perform()

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3
