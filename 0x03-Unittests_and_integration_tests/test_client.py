#!/usr/bin/env python3
"""Testing Utils for Github ORG"""

import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient, get_json
import client


class TestGithubOrgClient(unittest.TestCase):
    """Testing Github Client"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch.object(client, "get_json")
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """This method should test that GithubOrgClient.org
        returns the correct value"""
        correct_result = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = correct_result
        test_object = GithubOrgClient(org_name)
        self.assertEqual(test_object.org, correct_result)
        self.assertTrue(mock_get_json.called)

    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_repos_url"""
        test_object = GithubOrgClient(org_name="Test")
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as property_mock:
            property_mock.return_value = {"repos_url": "Test"}
            self.assertEqual(test_object._public_repos_url, "Test")
