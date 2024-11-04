import time

from utils.exceptions import FeedbackFormNotAvailableError
from utils.helpers import fetch_environment, create_selenium_instance
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UIT_PORTAL_URL, UIT_PORTAL_USERNAME, UIT_PORTAL_PASSWORD = fetch_environment()

if __name__ == "__main__":
    driver = create_selenium_instance()

    driver.get(UIT_PORTAL_URL)

    # Enter the username & password values

    username_input = driver.find_elements(
        By.CSS_SELECTOR, "#updatepanel > div.form-group > input"
    )[0]
    username_input.send_keys(UIT_PORTAL_USERNAME)

    password_input = driver.find_elements(
        By.CSS_SELECTOR, "#updatepanel > div.form-group > input"
    )[1]
    password_input.send_keys(UIT_PORTAL_PASSWORD)

    # Press login

    login_button = driver.find_element(By.CSS_SELECTOR, "#btnlgn")
    login_button.click()

    # Click on the feedback button from the sidebar

    general_list = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#ctl00_leftAccordion li:nth-child(2)")
        )
    )
    li_elements = general_list.find_elements(By.CSS_SELECTOR, "div > ul > li")

    time.sleep(2)

    feedback_form_not_available = True

    for li in li_elements:
        try:
            li_anchor_element = li.find_element(By.CSS_SELECTOR, "a")
            li_anchor_element_text = li_anchor_element.get_attribute(
                "innerText"
            ).lower()
            li_anchor_element_href = li_anchor_element.get_attribute("href")

            if (
                "feedback" in li_anchor_element_text
                and li_anchor_element_href
                and li_anchor_element_href != "#"
            ):
                feedback_form_not_available = False
                driver.get(li_anchor_element_href)

        except Exception as err:
            pass

    if feedback_form_not_available:
        raise FeedbackFormNotAvailableError("No feedback form found :(")

    time.sleep(5)
