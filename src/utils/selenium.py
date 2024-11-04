from selenium.webdriver.chrome.options import Options
from selenium import webdriver


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
