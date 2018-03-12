"""test unit"""
from unittest import TestCase

import task6


class TestPrime(TestCase):
    """Test class"""

    def setUp(self):
        """init"""

    def test_get_ver(self):
        """func test"""
        self.assertEqual(task6.get_ver(), "3.6.4")

    def test_get_env(self):
        """test env"""
        self.assertTrue(task6.get_pip())

    def test_get_path(self):
        """test path"""
        self.assertIsNot(task6.get_pythpath(), "/home/root/")

    def tearDown(self):
        """Finish"""
