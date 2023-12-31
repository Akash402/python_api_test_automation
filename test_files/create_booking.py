from util_files.methods import Methods
import unittest, config, json

class Create_Booking(unittest.TestCase):

    # create endpoint test case
    def test_response(self):
        request = Methods(config.BASE_URL)

        # reading the json file - request body
        with open('data/create_booking.json') as f:
            data = json.load(f)

        payload = json.dumps(data)
        response = request.post_method(config.ENDPOINTS['all_bookings'], payload)
        payload_dict = json.loads(payload)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload_dict, response.json().get('booking', {}))

        with open('data/booking_data.json', 'w') as outfile:
            json.dump({"new_booking_id": response.json().get('bookingid', {})}, outfile)
            
if __name__ == '__main__':
    unittest.main()