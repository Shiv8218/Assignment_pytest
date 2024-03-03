from selenium.webdriver.common.by import By

userNameField= '#username'
passwordField='#password'
submitButton='#submit'
testLoginTextLocator ='.main-container ul li'
fetchUserName =".main-container ul li b:nth-child(2)" # use index 0 for password and index 1 for password
fetchPassword =".main-container ul li b:nth-child(4)"
successTextLocator ='.post-title'
logout = '.wp-block-button__link'
errorMessageLocator ='.show'


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username = ''
        self.password = ''

    # def navigate_to_login_page(self):
    #     self.driver.get('practice-test-login/')

    def verify_correct_page_loaded(self, text):
        return self.driver.find_element(By.CSS_SELECTOR,testLoginTextLocator).text.__eq__(text)

    def get_username_from_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, fetchUserName).text

    def get_password_from_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, fetchPassword).text

    def fetch_data_and_login(self):
        password = self.get_password_from_page()
        self.input_password(password)

        username = self.get_username_from_page()
        self.input_username(username)

        self.click_submit()

    def input_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, userNameField).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, passwordField).send_keys(password)

    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, submitButton).click()

    def verify_success_login(self, success_login_string):
        success_text = self.driver.find_element(By.CSS_SELECTOR, successTextLocator).text
        assert success_text == success_login_string, "Success login text doesn't match"

    def logout(self):
        logout_element = self.driver.find_element(By.CSS_SELECTOR, logout)
        assert logout_element.is_displayed(), "Logout button not visible"
        logout_element.click()

    def verify_invalid_credentials_notification(self, error_text):
        error_message = self.driver.find_element(By.CSS_SELECTOR, errorMessageLocator).text
        assert error_message.__eq__(error_text), "Error message not found on the page"
