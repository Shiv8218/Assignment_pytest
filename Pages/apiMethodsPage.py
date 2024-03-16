import requests

from Utilities.ReadConfigurations import readconfig

base_url = readconfig('basic info','api_url')


class ApiMethods:
    def list_users_by_page(self,page):
        return requests.get(f"{base_url}/users?page={page}")

    def get_user_by_id(self,user_id):
        return requests.get(f"{base_url}/users/{user_id}")

    def get_unknown_data(self):
        return requests.get(f"{base_url}/unknown")

    def get_unknown_by_id(self,unknown_id):
        return requests.get(f"{base_url}/unknown/{unknown_id}")

    def create_user(self,user):
        return requests.post(f"{base_url}/users", json=user)

    def update_user(self,user_id, updated_user_data):
        return requests.put(f"{base_url}/users/{user_id}", json=updated_user_data)

    def patch_user(self,user_id, patched_user_data):
        return requests.patch(f"{base_url}/users/{user_id}", json=patched_user_data)

    def delete_user(self,user_id):
        return requests.delete(f"{base_url}/users/{user_id}")

    def register_user(self,user):
        return requests.post(f"{base_url}/register", json=user)

    def login_user(self,user):
        return requests.post(f"{base_url}/login", json=user)

    def get_users_with_delay(self,delay_seconds):
        return requests.get(f"{base_url}/users?delay={delay_seconds}")

