import testutils
from unittest import TestCase


class Test(TestCase):

    @classmethod
    def setup_class(cls):
        print('\r\nSetting up the class')
        testutils.create_lambda('lambda')
        testutils.create_bucket('a-bucket')

    @classmethod
    def teardown_class(cls):
        print('\r\nTearing down the class')
        testutils.delete_lambda('lambda')
        testutils.delete_bucket('a-bucket')

    def test_that_two_objects_in_s3_after_two_invocations(self):
        _ = testutils.invoke_function_and_get_message('lambda')
        _ = testutils.invoke_function_and_get_message('lambda')
        bucket_objects = testutils.list_s3_bucket_objects('a-bucket')
        self.assertEqual(len(bucket_objects), 2)
