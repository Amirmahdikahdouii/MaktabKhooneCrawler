from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from dotenv import load_dotenv
import os
import time
from auth import authentication

load_dotenv()
MAKTABKHOONE_EMAIL = os.getenv("MAKTABKHOONE_EMAIL")
MAKTABKHOONE_PASSWORD = os.getenv("MAKTABKHOONE_PASSWORD")
TARGET_URL = ""

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
if authentication(driver, MAKTABKHOONE_EMAIL, MAKTABKHOONE_PASSWORD):
    driver.get(TARGET_URL)

    ...

driver.quit()
