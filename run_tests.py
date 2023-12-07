import unittest, xmlrunner
from datetime import datetime

# Import your test suite or test cases
from test_files.ping import Ping
from test_files.get_all_bookings import Get_All_Bookings
from test_files.create_booking import Create_Booking

if __name__ == '__main__':

    # Create a test suite
    suite = unittest.TestSuite()

    # Add tests to be run to the suite
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Ping))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Get_All_Bookings))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Create_Booking))

    # Getting current date and time for results directory
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")

    # Specify the XMLTestRunner and output directory
    runner = xmlrunner.XMLTestRunner(output='results/' + dt_string)

    # Run the tests with the XMLTestRunner
    result = runner.run(suite)
