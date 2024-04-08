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
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method return output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


if __name__ == "__main__":
    unittest.main()
