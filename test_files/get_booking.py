from util_files.methods import Methods
import unittest, config, json

class Get_Booking(unittest.TestCase):

    # get booking with booking_id test case
    def test_response(self):
        # reading json file for booking id
        with open('data/booking_data.json') as f:
            data = json.load(f)
        
        # reading create booking json file for validation
        with open('data/create_booking.json') as f:
            create_booking = json.load(f)

        request = Methods(config.BASE_URL)
        response = request.get_method(config.ENDPOINTS['get_booking'] + str(data['new_booking_id']))

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(create_booking, response.json())
 