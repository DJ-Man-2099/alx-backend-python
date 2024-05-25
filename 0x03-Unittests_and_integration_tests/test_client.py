#!/usr/bin/env python3
"""Testing Utils for Github ORG"""

from typing import Dict
import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
import requests
from client import GithubOrgClient, get_json
import client
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
        """unit-test GithubOrgClient.public_repos"""
        mock_get_json.return_value = [
            {"name": "Test 1"},
            {"name": "Test 2"}
        ]
        names = list(
            map(lambda r: r["name"], mock_get_json.return_value))
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "test"
            test_object = GithubOrgClient("Testing")

            self.assertListEqual(test_object.public_repos(), names)

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("test")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str, result: bool):
        """unit-test GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), result)


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test the GithubOrgClient.public_repos method in an integration test"""

    @classmethod
    def setUpClass(cls):
        """mock requests.get to
         return example payloads found in the fixtures"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """the tearDownClass class method to stop the patcher"""
        cls.get_patcher.stop()
