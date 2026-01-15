import pytest
from .config import configure


@pytest.fixture(autouse=True)
def nanowait_pytest_integration(request):
    """
    Automatically injects test context into selenium-nanowait.
    Enables future features like screenshots on failure.
    """
    configure(test_context=request.node)
    yield
