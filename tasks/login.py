from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    @staticmethod
    def as_admin():
        return Login("Admin", "admin123")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser
        wait = WebDriverWait(browser, 10)

        # Iniciar sesión
        wait.until(EC.presence_of_element_located(
            (By.NAME, 'username'))).send_keys(self.username)
        browser.find_element(By.NAME, 'password').send_keys(self.password)
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
