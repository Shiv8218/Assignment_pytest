import pytest
import json

json_file = open('./StaticData/testData.json')
json_data = json.load(json_file)


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestSearch:
    def test_login_with_valid_credential(self):
        credentials = json_data['validCredentials']
        assertions = json_data['assertionTexts']
        self.lp.input_username(credentials['username'])
        self.lp.input_password(credentials['password'])
        self.lp.click_submit()
        self.lp.verify_success_login(assertions['successLoginText'])

    def test_logout_functionality(self):
        credentials = json_data['validCredentials']
        assertions = json_data['assertionTexts']
        self.lp.input_username(credentials['username'])
        self.lp.input_password(credentials['password'])
        self.lp.click_submit()
        self.lp.verify_success_login(assertions['successLoginText'])
        self.lp.logout()
        self.lp.verify_correct_page_loaded(assertions['successLoginPageLoad'])

    def test_verify_error_notification_with_invalid_username(self):
        credentials = json_data['invalidCredentialsUsername']
        assertions = json_data['assertionTexts']
        self.lp.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.lp.input_username(credentials['username'])
        self.lp.input_password(credentials['password'])
        self.lp.click_submit()
        self.lp.verify_invalid_credentials_notification(assertions['invalidUserName'])

    def test_verify_error_notification_with_invalid_password(self):
        credentials = json_data['invalidCredentialsPassword']
        assertions = json_data['assertionTexts']
        self.lp.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.lp.input_username(credentials['username'])
        self.lp.input_password(credentials['password'])
        self.lp.click_submit()
        self.lp.verify_invalid_credentials_notification(assertions['InvalidPassword'])

    def test_fetch_id_and_password_from_page_then_login(self):
        assertions = json_data['assertionTexts']
        self.lp.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.lp.fetch_data_and_login()
        self.lp.verify_success_login(assertions['successLoginText'])

    def test_verify_error_notification_without_credentials(self):
        assertions = json_data['assertionTexts']
        self.lp.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.lp.click_submit()
        self.lp.verify_invalid_credentials_notification(assertions['invalidUserName'])