import requests, json, config
    
# token generation
def generate_token(base_url):

    url = base_url + config.ENDPOINTS['authentication']

    payload = json.dumps({
        "username": str(config.USERNAME),
        "password": str(config.PASSWORD)
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return(response.json()['token'])

# post method
def post_method(base_url, endpoint, payload):
    token = generate_token(base_url)
    url = base_url + endpoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return(response)

# put method
def put_method(base_url, endpoint, payload):
    url = base_url + endpoint

    # in this case, we are using a hardcoded token because the put request of restful booker is designed this way. Ideally, we should use the token generation method.
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=' 
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return(response)

# patch method
def patch_method(base_url, endpoint, payload):
    token = generate_token(base_url)
    url = base_url + endpoint

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + token
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    return(response)

# get method
def get_method(base_url, endpoint):
    token = generate_token(base_url)
    url = base_url + endpoint
    payload = {}
    headers = {
        'Authorization': 'Basic ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return(response)

# delete method
def delete_method(base_url, endpoint):
    token = generate_token(base_url)
    url = base_url + endpoint
    payload = {}
    headers = {
        'Authorization': 'Basic ' + token
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    return(response)

# read json file
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in file '{file_path}'.")
        return None
