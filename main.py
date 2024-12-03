from core import settings
from core import kill_process
from auth import authentication
from collector import open_target_url, get_videos_href, extract_download_videos_in_file

if __name__ == "__main__":
    TARGET_URL = input("Please Enter your course URL: ")
    driver = settings.create_driver()
    driver, is_authenticated = authentication(driver, settings.MAKTABKHOONE_EMAIL, settings.MAKTABKHOONE_PASSWORD)
    if not is_authenticated:
        kill_process("Failed to login MaktabKhoone.org")

    driver, is_redirected_to_course_url = open_target_url(driver, TARGET_URL)
    if not is_redirected_to_course_url:
        kill_process("Failed to redirect to course URL")

    driver, video_pages_href = get_videos_href(driver)
    extract_download_videos_in_file(driver, video_pages_href)
    driver.quit()
