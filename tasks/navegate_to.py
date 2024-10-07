from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class NavigateTo:
    def __init__(self, button_name):  # Constructor para recibir el nombre del botón
        self.button_name = button_name

    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser

        # Enter the other step
        browser.find_element(
            By.XPATH, f"//button[text()=' {self.button_name} ']").click()
        time.sleep(3)

        # Print the entered button name
        print(f"Entered the {self.button_name}")
