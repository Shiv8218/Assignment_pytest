import pytest
import json

json_file = open('./StaticData/testData.json')
json_data = json.load(json_file)


@pytest.mark.usefixtures("api_fixture")
class TestAPI:

    def test_1_get_list_users_page_2(self):
        api = json_data['api']
        page = api["pageID"]

        response = self.page_object.list_users_by_page(page)
        assert response.status_code == 200
        assert response.json()["page"] == page

    def test_2_get_user_by_id(self):
        api = json_data['api']
        user_id = api["pageID"]
        response = self.page_object.get_user_by_id(user_id)
        assert response.status_code == 200
        assert response.json()["data"]["id"] == user_id

    def test_3_get_user_by_id_not_present(self):
        api = json_data['api']
        user_id = api["invalidID"]
        response = self.page_object.get_user_by_id(user_id)
        assert response.status_code == 404

    def test_4_get_unknown_data(self):
        response = self.page_object.get_unknown_data()
        assert response.status_code == 200
        assert len(response.json()["data"]) > 0

    def test_5_get_unknown_by_id(self):
        api = json_data['api']
        unknown_id = api["unknownValidID"]
        response = self.page_object.get_unknown_by_id(unknown_id)
        assert response.status_code == 200
        assert response.json()["data"]["id"] == unknown_id

    def test_6_get_unknown_by_id_not_found(self):
        api = json_data['api']
        unknown_id = api["unknownInValidID"]
        response = self.page_object.get_unknown_by_id(unknown_id)
        assert response.status_code == 404

    def test_7_post_create_user(self):
        api = json_data['api']
        new_user = {"name": api["name"], "job": api["job"]}
        response = self.page_object.create_user(new_user)
        assert response.status_code == 201
        assert response.json()["name"] == new_user["name"]
        assert response.json()["job"] == new_user["job"]
        created_user_id = response.json()["id"]
        # Storing the user_id
        with open('created_user_id.txt', 'w') as f:
            f.write(str(created_user_id))

    def test_8_put_update_user(self):
        api = json_data['api']

        # Reading the created user_id
        with open('created_user_id.txt', 'r') as f:
            user_id = f.read().strip()

        updated_user_data = {"name": api["newName"], "job": api["newJob"]}
        response = self.page_object.update_user(user_id, updated_user_data)
        assert response.status_code == 200
        assert response.json()["name"] == updated_user_data["name"]
        assert response.json()["job"] == updated_user_data["job"]

    def test_9_patch_user(self):
        # Reading the created user_id
        with open('created_user_id.txt', 'r') as f:
            user_id = f.read().strip()

        api = json_data['api']
        patched_user_data = {"job": api["updatedJob"]}
        response = self.page_object.patch_user(user_id, patched_user_data)
        assert response.status_code == 200
        assert response.json()["job"] == patched_user_data["job"]
        assert "updatedAt" in response.json()

    def test_10_delete_user(self):
        # Reading the created user_id
        with open('created_user_id.txt', 'r') as f:
            user_id_to_delete = f.read().strip()

        response = self.page_object.delete_user(user_id_to_delete)
        assert response.status_code == 204

    def test_11_post_register_user_successful(self):
        api = json_data['api']
        new_user = {"email": api["email"], "password": api["password"]}
        response = self.page_object.register_user(new_user)
        assert response.status_code == 200
        assert "id" in response.json()
        assert "token" in response.json()

    def test_12_post_register_user_unsuccessful(self):
        api = json_data['api']
        new_user = {"email": api["email"]}
        response = self.page_object.register_user(new_user)
        assert response.status_code == 400
        assert "error" in response.json()

    def test_13_post_login_user_success(self):
        api = json_data['api']
        user_to_login = {"email": api["email"], "password": api["password"]}
        response = self.page_object.login_user(user_to_login)
        assert response.status_code == 200

    def test_14_post_login_user_rejected(self):
        api = json_data['api']
        user_to_login = {"email": api["email"]}
        response = self.page_object.login_user(user_to_login)
        assert response.status_code == 400
        assert "error" in response.json()

    def test_15_get_users_with_delay(self):
        delay_seconds = 3
        response = self.page_object.get_users_with_delay(delay_seconds)
        assert response.status_code == 200
