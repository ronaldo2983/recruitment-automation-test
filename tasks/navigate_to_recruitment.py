from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigateToRecruitment:
    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser
        wait = WebDriverWait(browser, 10)

        # Enter the Recruitment module
        options = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//ul[@class='oxd-main-menu']/li[5]")))
        options.click()
        print("Entered the Recruitment module")
