import requests


class ApiMethods:
    def list_users_by_page(self,page):
        return requests.get(f"https://reqres.in/api/users?page={page}")

    def get_user_by_id(self,user_id):
        return requests.get(f"https://reqres.in/api/users/{user_id}")

    def get_unknown_data(self):
        return requests.get("https://reqres.in/api/unknown")

    def get_unknown_by_id(self,unknown_id):
        return requests.get(f"https://reqres.in/api/unknown/{unknown_id}")

    def create_user(self,user):
        return requests.post("https://reqres.in/api/users", json=user)

    def update_user(self,user_id, updated_user_data):
        return requests.put(f"https://reqres.in/api/users/{user_id}", json=updated_user_data)

    def patch_user(self,user_id, patched_user_data):
        return requests.patch(f"https://reqres.in/api/users/{user_id}", json=patched_user_data)

    def delete_user(self,user_id):
        return requests.delete(f"https://reqres.in/api/users/{user_id}")

    def register_user(self,user):
        return requests.post("https://reqres.in/api/register", json=user)

    def login_user(self,user):
        return requests.post("https://reqres.in/api/login", json=user)

    def get_users_with_delay(self,delay_seconds):
        return requests.get(f"https://reqres.in/api/users?delay={delay_seconds}")

