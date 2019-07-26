import testutils
from unittest import TestCase


class Test(TestCase):

    @classmethod
    def setup_class(cls):
        print('\r\nSetting up the class')
        testutils.create_lambda('lambda')

    @classmethod
    def teardown_class(cls):
        print('\r\nTearing down the class')
        testutils.delete_lambda('lambda')

    def test_that_lambda_returns_correct_message(self):
        payload = testutils.invoke_function_and_get_message('lambda')
        self.assertEqual(payload['message'], 'Hello pytest!')

