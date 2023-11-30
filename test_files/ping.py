from util_files.methods import Methods
import unittest

class Ping(unittest.TestCase):

    # ping endpoint test case
    def test_response(self):
        request = Methods("https://restful-booker.herokuapp.com/")
        response = request.get_method("ping")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Created', str(response.content))
            
if __name__ == '__main__':
    unittest.main()
