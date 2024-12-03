from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from core import settings
import time
import json

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


def open_target_url(driver: WebDriver, target_url: str) -> [WebDriver, bool]:
    try:
        driver.get(target_url)
        return driver, True
    except Exception as e:
        print(f"Exception occurred: {e}")
        return driver, False


def get_videos_href(driver: WebDriver) -> [WebDriver, [str]]:
    video_pages: list = list()
    while not video_pages:
        video_pages = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-v-791a78e2]"))
        )
        time.sleep(1)
    video_pages_href: [str] = [settings.MAKTABKHOONE_URL + page.get_dom_attribute("href") for page in video_pages]
    return driver, video_pages_href


def get_downloaded_file_name(download_link: str) -> str:
    """
    Returns cleaned file name because the download links may have extra information
    """
    download_link = download_link.split("https://cdn.maktabkhooneh.org/videos/")
    download_link = download_link[1]
    download_link = download_link.split("?")
    file_name = download_link[0]
    return file_name


def get_file_name(download_link: str) -> str:
    try:
        download_link = download_link.split("&name=")
        file_name = download_link[-1]
        if file_name.endswith("\n"):
            file_name = file_name.split("\n")[0]
        return file_name
    except Exception as e:
        print(f"Failed to extract file name from download URL: {e}")
        return get_downloaded_file_name(download_link)


def extract_download_link(driver: WebDriver) -> str:
    try:
        video_source = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.CLASS_NAME, "js-player__source"))
        )
        download_link = video_source.get_attribute("src")
        return download_link
    except Exception as e:
        raise ValueError(f"Exception occurred while extracting download link from video page: {e}")


def extract_video_title(driver: WebDriver) -> str:
    try:
        title = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.CLASS_NAME, "unit-container__top-title"))
        )
        return title.text
    except Exception as e:
        raise ValueError(f"Exception occurred while extracting title of video: {e}")


def write_download_link_in_file(download_link: str) -> None:
    with open("links.txt", "a") as f:
        f.write(f"{download_link}\n")


def write_video_info_in_file(download_link: str, number: int) -> None:
    with open("file_names.txt", "a") as f:
        f.write(json.dumps({
            "number": number,
            "file_name": get_file_name(download_link),
            "downloaded_file_name": get_downloaded_file_name(download_link),
            "link": download_link
        }) + "\n")


def extract_download_videos_in_file(driver: WebDriver, video_pages_href: [str]) -> None:
    for i, link in enumerate(video_pages_href, start=1):
        try:
            driver.get(link)
            download_link = extract_download_link(driver)
            write_download_link_in_file(download_link)
            write_video_info_in_file(download_link, i)
        except Exception as e:
            print(e)
