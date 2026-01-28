import pytest
from .config import configure


@pytest.fixture(autouse=True)
def nanowait_pytest_integration(request):
    """
    Injects test context for diagnostics and reporting.
    """
    configure(test_context=request.node)
    yield
