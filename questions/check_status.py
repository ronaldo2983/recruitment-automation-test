from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckCandidateStatus:
    def __init__(self, candidate_name):
        self.candidate_name = candidate_name

    def answered_by(self, actor):
        browser = actor.ability_to_use_browser().browser
        wait = WebDriverWait(browser, 10)

        # Buscar al candidato por nombre
        row = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[@role='row']//div[@role='cell'][3]//div[normalize-space(text()) = '{self.candidate_name}']/ancestor::div[@role='row']")))

        # Obtener el estado
        status = row.find_element(
            By.XPATH, ".//div[@role='cell'][last()-1]/div").text
        return status
