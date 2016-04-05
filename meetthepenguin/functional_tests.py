"""Functional test suite
"""

import unittest

class FunctionalTests(unittest.TestCase):
    """General functional tests
    """
    def setUp(self):
        """Cleanup before each test
        """
        settings = {'sqlalchemy.url':'sqlite://'}
        from meetthepenguin import main
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_can_confirm_attendence(self):
        """User can confirm his/her attendence to an event.
        The user data it is persisted.
        """
        # Yarpen enters the root URL and is presented with a page (HTTP 200)

        # The page presents meetthepenguin app

        # The page contains a list of events to which Yarpen is subscribed

        # Yarpen confirms attendence to the first event by pressing ✔
        # next to the event

        # After the page reloads the event becomes green

        # Yarpen reloads the page

        # The confirmed event is still green

        # Yarpen rejects attendence to the second event by pressing ✘
        # next to the event

        # After the page reloads the event becomes red

        # Yarpen reloads the page

        # The confirmed event is still green

        # The rejected event is still red
