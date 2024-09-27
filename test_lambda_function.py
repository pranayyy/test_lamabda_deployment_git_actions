import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        response = lambda_handler({}, {})
        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
