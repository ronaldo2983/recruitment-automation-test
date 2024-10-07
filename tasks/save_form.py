from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Save:
    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser

        # Enter the other step
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        print(f"Saved")
