#!/usr/bin/env python3
"""Testing Utils for Github ORG"""

import json
from typing import Any, Dict, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Testing access nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               result: Any) -> None:
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         exception: KeyError) -> None:
        """ test that a KeyError is raised for the following inputs"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Testing get jeson function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """test that utils.get_json returns the expected result"""
        with patch.object(requests, 'get') as mock_method:
            mock_method.return_value = Mock()
            mock_method.return_value.json = Mock(return_value=test_payload)
            result = get_json(test_url)
            mock_method.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Testing memoize"""

    def test_memoize(self):
        """Inside test_memoize, define following class"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 45
            test_object = TestClass()
            self.assertEqual(test_object.a_property,
                             mock_a_method.return_value)
            self.assertEqual(test_object.a_property,
                             mock_a_method.return_value)
            mock_a_method.assert_called_once()
