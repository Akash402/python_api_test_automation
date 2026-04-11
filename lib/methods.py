import requests, json
import auth


def post_method(base_url, endpoint, payload):
    url = base_url + endpoint
    headers = {"Content-Type": "application/json", **auth.get_auth_headers()}
    return requests.request("POST", url, headers=headers, data=payload)


def put_method(base_url, endpoint, payload):
    url = base_url + endpoint
    headers = {"Content-Type": "application/json", **auth.get_auth_headers()}
    return requests.request("PUT", url, headers=headers, data=payload)


def patch_method(base_url, endpoint, payload):
    url = base_url + endpoint
    headers = {"Content-Type": "application/json", **auth.get_auth_headers()}
    return requests.request("PATCH", url, headers=headers, data=payload)


def get_method(base_url, endpoint):
    url = base_url + endpoint
    headers = auth.get_auth_headers()
    return requests.request("GET", url, headers=headers)


def delete_method(base_url, endpoint):
    url = base_url + endpoint
    headers = auth.get_auth_headers()
    return requests.request("DELETE", url, headers=headers)


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in file '{file_path}'.")
        return None
