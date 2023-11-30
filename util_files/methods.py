import requests

class Methods:

    # instantiate the methods class and set the base url
    def __init__(self, base_url):
        self.base_url = base_url

    # post method

    # put method

    # patch method

    # get method
    def get_method(self, endpoint):
        url = self.base_url + endpoint
        payload = {}
        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return(response)

    # delete method
