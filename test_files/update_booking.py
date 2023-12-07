from util_files.methods import Methods
import unittest, config, json

class Update_Booking(unittest.TestCase):

    # update booking endpoint test case
    def test_response(self):
        # reading json file for booking id
        with open('data/booking_data.json') as f:
            data = json.load(f)

        request = Methods(config.BASE_URL)

        # reading the json file - request body
        with open('data/create_booking.json') as f:
            data2 = json.load(f)

        payload = json.dumps(data2)
        response = request.put_method(config.ENDPOINTS['get_booking'] + str(data['new_booking_id']), payload)
        payload_dict = json.loads(payload)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload_dict, response.json())
            
if __name__ == '__main__':
    unittest.main()