from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ScheduleInterview:
    def __init__(self, title, interviewer, date):
        self.title = title
        self.interviewer = interviewer
        self.date = date

    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser
        wait = WebDriverWait(browser, 10)

        # Hacer clic en "Schedule Interview"
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()=' Schedule Interview ']"))).click()

        # Rellenar formulario de entrevista
        browser.find_element(
            By.XPATH, "//label[contains(text(), 'Interview Title')]/following::input[1]").send_keys(self.title)

        # Autocompletar entrevistador
        browser.find_element(
            By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(self.interviewer)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[@role='option']//span[text()='{self.interviewer}']"))).click()

        # Fecha de entrevista
        browser.find_element(
            By.XPATH, "//input[@placeholder='yyyy-mm-dd']").send_keys(self.date)

        # Guardar
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
