#!/usr/bin/env python3
"""Testing Utils for Github ORG"""

import json
from typing import Any, Dict, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json


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
