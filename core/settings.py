from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from dotenv import load_dotenv
import os

load_dotenv()
MAKTABKHOONE_EMAIL = os.getenv("MAKTABKHOONE_EMAIL")
MAKTABKHOONE_PASSWORD = os.getenv("MAKTABKHOONE_PASSWORD")
MAKTABKHOONE_URL = "https://maktabkhooneh.org"


def create_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver
