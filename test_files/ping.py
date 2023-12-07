from util_files.methods import Methods
import unittest, config

class Ping(unittest.TestCase):

    # ping endpoint test case
    def test_response(self):
        request = Methods(config.BASE_URL)
        response = request.get_method(config.ENDPOINTS['ping'])

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertIn('Created', str(response.content))
            
if __name__ == '__main__':
    unittest.main()
