#!/usr/bin/env python3
'''
Write the unit test for utils.access_nested_map.
Create a TestAccessNestedMap class
that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map
method to test that the method returns what it is supposed to.
Decorate the method with @parameterized.expand
to test the function for following inputs
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
