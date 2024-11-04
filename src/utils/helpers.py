import os

from dotenv import load_dotenv
from utils.exceptions import EnvironmentNotConfiguredError
from typing import Tuple
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def fetch_environment() -> Tuple[str, str, str]:
    load_dotenv()

    uit_portal_url = os.getenv("UIT_PORTAL_URL")
    uit_portal_username = os.getenv("UIT_PORTAL_USERNAME")
    uit_portal_password = os.getenv("UIT_PORTAL_PASSWORD")

    if not uit_portal_url or not uit_portal_username or not uit_portal_password:
        raise EnvironmentNotConfiguredError(
            "You have not properly set the environment variables required to run this program! Please refer to the README.md file present in the root of the project."
        )

    return uit_portal_url, uit_portal_username, uit_portal_password


def create_selenium_instance(headless: bool = False):

    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1250,1000")

    if headless:
        options.add_argument("--headless=old")

    driver = webdriver.Chrome(options=options)

    return driver
