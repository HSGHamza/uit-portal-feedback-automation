import time

from utils.helpers import fetch_environment, create_selenium_instance

UIT_PORTAL_URL, UIT_PORTAL_USERNAME, UIT_PORTAL_PASSWORD = fetch_environment()

if __name__ == "__main__":
    driver = create_selenium_instance()

    driver.get(UIT_PORTAL_URL)

    time.sleep(5)
