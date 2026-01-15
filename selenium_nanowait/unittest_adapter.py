from .config import configure


class NanoWaitTestCaseMixin:
    """
    Mixin for unittest.TestCase integration.
    """

    def setUp(self):
        super().setUp()
        configure(test_context=self)
