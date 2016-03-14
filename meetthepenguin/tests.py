"""Unit tests
"""

import unittest

from pyramid import testing

class SampleTest(unittest.TestCase):
    """Sample test case
    """
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_sample(self):
        """Sample unit test
        """
        pass
