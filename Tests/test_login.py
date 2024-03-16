import pytest
import json

json_file = open('./StaticData/testData.json')
json_data = json.load(json_file)


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestLogin:

    @pytest.fixture
    def endpoint(self):
        return "practice-test-login/"

    def test1_login_with_valid_credential(self):
        credentials = json_data['validCredentials']
        assertions = json_data['assertionTexts']
        self.page_object.input_username(credentials['username'])
        self.page_object.input_password(credentials['password'])
        self.page_object.click_submit()
        self.page_object.verify_success_login(assertions['successLoginText'])

    def test2_logout_functionality(self):
        credentials = json_data['validCredentials']
        assertions = json_data['assertionTexts']
        self.page_object.input_username(credentials['username'])
        self.page_object.input_password(credentials['password'])
        self.page_object.click_submit()
        self.page_object.verify_success_login(assertions['successLoginText'])
        self.page_object.logout()
        self.page_object.verify_correct_page_loaded(assertions['successLoginPageLoad'])

    def test3_verify_error_notification_with_invalid_username(self):
        credentials = json_data['invalidCredentialsUsername']
        assertions = json_data['assertionTexts']
        self.page_object.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.page_object.input_username(credentials['username'])
        self.page_object.input_password(credentials['password'])
        self.page_object.click_submit()
        self.page_object.verify_invalid_credentials_notification(assertions['invalidUserName'])

    def test4_verify_error_notification_with_invalid_password(self):
        credentials = json_data['invalidCredentialsPassword']
        assertions = json_data['assertionTexts']
        self.page_object.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.page_object.input_username(credentials['username'])
        self.page_object.input_password(credentials['password'])
        self.page_object.click_submit()
        self.page_object.verify_invalid_credentials_notification(assertions['InvalidPassword'])

    def test5_fetch_id_and_password_from_page_then_login(self):
        assertions = json_data['assertionTexts']
        self.page_object.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.page_object.fetch_data_and_login()
        self.page_object.verify_success_login(assertions['successLoginText'])

    def test6_verify_error_notification_without_credentials(self):
        assertions = json_data['assertionTexts']
        self.page_object.verify_correct_page_loaded(assertions['successLoginPageLoad'])
        self.page_object.click_submit()
        self.page_object.verify_invalid_credentials_notification(assertions['invalidUserName'])