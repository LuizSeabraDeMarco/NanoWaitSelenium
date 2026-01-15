from .element import AdaptiveElement
from .config import get_config


def wait_for(driver, selector, *, timeout=None, **nano_kwargs):
    """
    Entry point for selenium-nanowait.
    """
    config = get_config()

    return AdaptiveElement(
        driver=driver,
        selector=selector,
        timeout=timeout or config.default_timeout,
        nano_kwargs={**config.nano_kwargs, **nano_kwargs},
        test_context=config.test_context
    )
