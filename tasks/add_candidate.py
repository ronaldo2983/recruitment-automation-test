import time
from selenium.webdriver.common.by import By
import os


class AddCandidate:
    def __init__(self, first_name, middle_name, last_name, email, contact):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.contact = contact

    def perform_as(self, actor):
        browser = actor.ability_to_use_browser().browser
        time.sleep(5)

        # Click en el botón de agregar candidato
        browser.find_element(
            By.XPATH, "//div[@class='orangehrm-header-container']/button[@type='button']").click()

        time.sleep(3)

        # Llenar el formulario
        first_name = browser.find_element(
            By.XPATH, "//input[@name='firstName']")
        first_name.send_keys("Ronaldo")

        middle_name = browser.find_element(
            By.XPATH, "//input[@name='middleName']")
        middle_name.send_keys("Jose")

        last_name = browser.find_element(By.XPATH, "//input[@name='lastName']")
        last_name.send_keys("Rodríguez")

        select_element = browser.find_element(
            By.CLASS_NAME, 'oxd-select-wrapper')
        select_element.click()

        time.sleep(1)  # ESPERAR PARA QUE SE CARGE EL HTML COMPLETAMENTE
        # seleccionar opcion del select
        option = browser.find_element(
            By.XPATH, "//div[@role='listbox']/div[@class='oxd-select-option'][2]")
        option.click()

        other_inputs = browser.find_elements(
            By.XPATH, "//input[@placeholder='Type here']")
        print("Finded inputs: ", len(other_inputs))
        email = other_inputs[0]
        email.send_keys("ronaldojose@gmail.com")

        contact_number = other_inputs[1]
        contact_number.send_keys("60000000")

        up_file = browser.find_element(By.XPATH, "//input[@type='file']")
        file_path = os.path.abspath("test.txt")
        up_file.send_keys(file_path)

        browser.find_element(
            By.XPATH, "//input[@placeholder='Enter comma seperated words...']").send_keys("automation, selenium, testing, python, webdriver")

        browser.find_element(
            By.XPATH, "//textarea[@placeholder='Type here']").send_keys("My keywords are: automation, selenium, testing, python, webdriver")

        checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
        browser.execute_script("arguments[0].scrollIntoView();", checkbox)
        browser.execute_script("arguments[0].click();", checkbox)

        browser.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)
