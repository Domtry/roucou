import unittest
import requests


class TestLogin(unittest.TestCase):
    def test_endpoint(self):
        query_body = {
            "username": "domtry",
            "password": "password"
        }

        r = requests.post("http://127.0.0.1:8000/api/v1/login/access-token", data=query_body)

        assert r.status_code == 200

    def test_auth_by_super_user(self):
        query_body = {
            "username": "admin",
            "password": "admin"
        }

        r = requests.post("http://127.0.0.1:8000/api/v1/login/access-token", data=query_body)
        auth_resp = r.json()

        assert "role" in auth_resp
        assert "username" in auth_resp
        assert "token" in auth_resp

        assert auth_resp["username"] == "admin"
        assert auth_resp["role"] == "admin"
        assert auth_resp["token"]["access_token"]
        assert auth_resp["token"]["refresh_token"]

    def test_auth_by_client(self):
        query_body = {
            "username": "brice",
            "password": "auth"
        }

        r = requests.post("http://127.0.0.1:8000/api/v1/login/access-token", data = query_body)
        auth_resp = r.json()

        assert "role" in auth_resp
        assert "username" in auth_resp
        assert "token" in auth_resp

        assert auth_resp["username"] == "brice"
        assert auth_resp["role"] == "client"
        assert auth_resp["token"]["access_token"]
        assert auth_resp["token"]["refresh_token"]

