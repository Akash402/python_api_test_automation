import requests, json, config

class Methods:

    # instantiate the methods class and set the base url
    def __init__(self, base_url):
        self.base_url = base_url
    
    # token generation
    def generate_token(self):

        url = self.base_url + config.ENDPOINTS['authentication']

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
    def post_method(self, endpoint, payload):
        token = self.generate_token()
        url = self.base_url + endpoint

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + token
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return(response)

    # put method
    def put_method(self, endpoint, payload):
        url = self.base_url + endpoint

        # in this case, we are using a hardcoded token because the put request of restful booker is designed this way. Ideally, we should use the token generation method.
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=' 
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        return(response)

    # patch method
    def patch_method(self, endpoint, payload):
        token = self.generate_token()
        url = self.base_url + endpoint

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + token
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        return(response)

    # get method
    def get_method(self, endpoint):
        token = self.generate_token()
        url = self.base_url + endpoint
        payload = {}
        headers = {
            'Authorization': 'Basic ' + token
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return(response)

    # delete method
    def delete_method(self, endpoint):
        token = self.generate_token()
        url = self.base_url + endpoint
        payload = {}
        headers = {
            'Authorization': 'Basic ' + token
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        return(response)
