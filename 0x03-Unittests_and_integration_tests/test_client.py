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
        def side_effect(url):
            """return correct payload based on url"""
            result = {}
            if "/repos" in url:
                result = cls.repos_payload
            elif "orgs/" in url:
                result = cls.org_payload
            mock = MagicMock()
            mock.json = MagicMock(return_value=result)
            return mock

        cls.get_patcher = patch.object(
            requests, "get", side_effect=side_effect)
        cls.mock = cls.get_patcher.start()

    @ classmethod
    def tearDownClass(cls):
        """the tearDownClass class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test GithubOrgClient.public_repos"""
        test_object = GithubOrgClient("google")
        self.assertDictEqual(test_object.org, self.org_payload)
        self.assertEqual(test_object._public_repos_url,
                         self.org_payload["repos_url"])
        self.assertEqual(test_object.repos_payload,
                         self.repos_payload)
        self.assertListEqual(test_object.public_repos(),
                             self.expected_repos)
        self.assertListEqual(test_object.public_repos("fake_licence"),
                             [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """test the public_repos with the argument license='apache-2.0'"""
        test_object = GithubOrgClient("google")
        self.assertListEqual(test_object.public_repos("apache-2.0"),
                             self.apache2_repos)
        self.mock.assert_called()
