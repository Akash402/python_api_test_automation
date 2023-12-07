from util_files.methods import Methods
import unittest, config

class Get_All_Bookings(unittest.TestCase):

    # get all bookings test case
    def test_response(self):
        request = Methods(config.BASE_URL)
        response = request.get_method(config.ENDPOINTS['all_bookings'])

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)
 