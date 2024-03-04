import pytest
import json

json_file = open('./StaticData/testData.json')
json_data = json.load(json_file)


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestLogin:
    @pytest.fixture
    def url(self):
        return "https://practicetestautomation.com/practice-test-exceptions/"

    def test_1_no_such_element_exception_handling(self):
        inputTexts = json_data['api']
        self.page_object.add_new_row_and_verify_two_input(inputTexts['newName'])

    def test_2_element_not_interactable_exception_handling(self):
        inputTexts = json_data['api']
        self.page_object.add_new_row_and_verify_two_input(inputTexts['newName'])
        self.page_object.add_data_in_row_2(inputTexts['newJob'])
        self.page_object.verify_save_success('Row 2 was saved')

    def test_3_verify_input_field_disabled_by_default(self):
        self.page_object.verify_input_disabled_by_default()

    def test_4_stale_element_reference_exception_handling(self):
        self.page_object.click_add_button()
        self.page_object.verify_save_success('Row 2 was added')
        self.page_object.verify_add_button_not_visible()

    def test_5_timeout_exception_handling(self):
        self.page_object.click_add_and_verify_two_input_rows()