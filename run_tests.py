import unittest
import xmlrunner

# Import your test suite or test cases
from test_files.ping import Ping

if __name__ == '__main__':

    # Create a test suite
    suite = unittest.TestSuite()

    # Add tests to be run to the suite
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Ping))

    # Specify the XMLTestRunner and output directory
    runner = xmlrunner.XMLTestRunner(output='test-reports')

    # Run the tests with the XMLTestRunner
    result = runner.run(suite)
