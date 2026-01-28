from .config import configure


class NanoWaitTestCaseMixin:
    """
    unittest integration for selenium-nanowait.
    """

    def setUp(self):
        super().setUp()
        configure(test_context=self)
