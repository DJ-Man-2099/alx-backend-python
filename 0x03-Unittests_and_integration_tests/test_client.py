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

    @patch('client.get_json', return_value=[
        {"name": "Test 1"},
        {"name": "Test 2"}
    ])
    def test_public_repos(self, mock_get_json):
        expected_repo_names = ["Test 1", "Test 2"]

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "mock_url"
            test_client = GithubOrgClient("my_org")

            # Test that the list of repos is what you expect
            # from the chosen payload
            self.assertListEqual(
                test_client.public_repos(), expected_repo_names)

            # Test that the mocked property and the mocked get_json
            # was called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("mock_url")
