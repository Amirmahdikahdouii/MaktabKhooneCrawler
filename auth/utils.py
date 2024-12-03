from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MAKTABKHOONE_URL = "https://maktabkhooneh.org/"
MAKTABKHOONE_LOGIN_URL = MAKTABKHOONE_URL + "signin/"


def authentication(driver: WebDriver, email: str, password: str) -> bool:
    driver.get(MAKTABKHOONE_LOGIN_URL)
    time.sleep(10)
    fill_email(driver, email)
    time.sleep(10)
    fill_password(driver, password)
    time.sleep(10)
    WebDriverWait(driver, 10).until(EC.url_changes(MAKTABKHOONE_LOGIN_URL))
    return True


def fill_email(driver: WebDriver, email: str):
    email_input = driver.find_element(By.ID, "tessera")
    email_input.send_keys(email)
    next_button = driver.find_element(By.CSS_SELECTOR, '[data-tag="ga-email-phone-login"]')
    next_button.click()


def fill_password(driver: WebDriver, password: str):
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    password_submit = driver.find_element(By.CSS_SELECTOR, '[data-tag="ga-password-submit"]')
    password_submit.click()
