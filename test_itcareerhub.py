import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://itcareerhub.de/ru"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1440,1000")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_itcareerhub_page_and_callback(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".t972__reject-btn"))).click()

    assert driver.find_element(By.CSS_SELECTOR, 'img[alt="IT Career Hub"]').is_displayed()

    for text in ("Программы", "Способы оплаты", "О нас", "Контакты", "Отзывы", "Блог"):
        assert driver.find_element(By.XPATH, f"//a[normalize-space()='{text}']")

    assert driver.find_element(By.XPATH, "//a[normalize-space()='ru']")
    assert driver.find_element(By.XPATH, "//a[normalize-space()='de']")

    contact = driver.find_element(By.CSS_SELECTOR, 'a[href="/ru/contact-us"]')
    driver.execute_script("arguments[0].click();", contact)
    wait.until(EC.url_contains("/ru/contact-us"))

    callback = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '#popup:form-tr') and normalize-space()='ОБРАТНЫЙ ЗВОНОК']")
        )
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", callback)
    driver.execute_script("arguments[0].click();", callback)

    assert wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(), 'Запишитесь на бесплатную карьерную консультацию')]")
        )
    )
