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
from unittest.mock import patch, Mock
import requests


def access_nested_map(nested_map, path):
    try:
        for key in path:
            nested_map = nested_map[key]
        return nested_map
    except KeyError as e:
        raise KeyError(f"Key '{e.args[0]}' not found in nested map")

def get_json(url):
    response = requests.get(url)
    return response.json()

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": {}}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exp_err):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), exp_err)

if __name__ == "__main__":
    unittest.main()
