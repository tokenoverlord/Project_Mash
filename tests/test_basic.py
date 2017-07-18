import unittest

from app import create_app

class Home_Test_Cases(unittest.TestCase):
    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    def setUp(self):
        pass

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    def tearDown(self):
        pass

    # initialization logic
    # code that is executed before each test
    def setUp(self):
        self.app = create_app('test').test_client()
        pass

    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        pass

    def test_http_get_request_success(self):
        # send http get request to the application
        # on the specific path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200, "[Home_Test_Cases::test_home_status_code]")

# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
