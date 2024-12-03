from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

MAKTABKHOONE_URL = "https://maktabkhooneh.org/"
MAKTABKHOONE_LOGIN_URL = MAKTABKHOONE_URL + "signin/"


def authentication(driver: WebDriver, email: str, password: str) -> [WebDriver, bool]:
    driver.get(MAKTABKHOONE_LOGIN_URL)
    driver, is_email_filled = fill_email(driver, email)
    if not is_email_filled:
        return driver, False
    driver, is_password_filled = fill_password(driver, password)
    if not is_email_filled:
        return driver, False
    WebDriverWait(driver, 10).until(EC.url_changes(MAKTABKHOONE_LOGIN_URL))
    return driver, True


def fill_email(driver: WebDriver, email: str) -> [WebDriver, bool]:
    try:
        email_input = WebDriverWait(driver, 10, ignored_exceptions=(NoSuchElementException,)) \
            .until(EC.presence_of_element_located((By.ID, "tessera")))
        email_input.send_keys(email)
        next_button = WebDriverWait(driver, 10, ignored_exceptions=(NoSuchElementException,)) \
            .until((EC.presence_of_element_located((By.CSS_SELECTOR, '[data-tag="ga-email-phone-login"]'))))
        next_button.click()
        return driver, True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return driver, False


def fill_password(driver: WebDriver, password: str) -> [WebDriver, bool]:
    try:
        password_input = WebDriverWait(driver, 10, ignored_exceptions=(NoSuchElementException,)) \
            .until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys(password)

        password_submit = WebDriverWait(driver, 10, ignored_exceptions=(NoSuchElementException,)) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-tag="ga-password-submit"]')))
        password_submit.click()
        return driver, True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return driver, False
