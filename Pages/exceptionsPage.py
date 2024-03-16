import time

from selenium.webdriver.common.by import By
from time import sleep


class Exceptions:
    landingPageText = '.main-container h2'
    inputArea = '.input-field'
    editButton = '[name="Edit"]'
    addButton = '[name="Add"]'
    saveButton = '[name="Save"]'
    successSave = '#confirmation'

    def __init__(self, driver):
        self.driver = driver

    # def exceptions_page_load(self):
    #     self.driver.get('https://practicetestautomation.com/practice-test-exceptions/')

    def verify_exception_page(self, text):
        assert text in self.driver.find_element(By.CSS_SELECTOR, self.landingPageText).text

    def verify_input_disabled_by_default(self):
        assert self.driver.find_element(By.CSS_SELECTOR, self.inputArea).get_attribute('disabled')

    def add_new_row_and_verify_two_input(self, text):
        self.driver.find_element(By.CSS_SELECTOR, self.editButton).click()
        self.driver.find_element(By.CSS_SELECTOR, self.inputArea).send_keys(text)
        self.driver.find_element(By.CSS_SELECTOR, self.addButton).click()
        time.sleep(5)  # Add appropriate wait
        assert len(self.driver.find_elements(By.CSS_SELECTOR, self.inputArea)) == 2

    def click_add_and_verify_two_input_rows(self):
        self.driver.find_element(By.CSS_SELECTOR, self.addButton).click()
        time.sleep(5)  # Add appropriate wait
        assert len(self.driver.find_elements(By.CSS_SELECTOR, self.inputArea)) == 2

    def add_data_in_row_2(self, text):
        self.driver.find_elements(By.CSS_SELECTOR, self.inputArea)[1].send_keys(text)
        self.driver.find_elements(By.CSS_SELECTOR, self.saveButton)[1].click()

    def verify_save_success(self, text):
        assert text in self.driver.find_element(By.CSS_SELECTOR, self.successSave).text

    def click_add_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.addButton).click()
        time.sleep(5)

    def verify_add_button_not_visible(self):
        assert not self.driver.find_element(By.CSS_SELECTOR, self.addButton).is_displayed()

    # def verify_add_button_not_visible(self):
    #     add_buttons = self.driver.find_elements(By.CSS_SELECTOR, self.addButton)
    #     for button in add_buttons:
    #         assert not button.is_displayed(), f"Button '{button.text}' is visible"


