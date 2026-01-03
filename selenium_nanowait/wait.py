from .element import AdaptiveElement

def wait_for(driver, selector, *, timeout=None, **nano_kwargs):
    """
    Entry point for selenium-nanowait.

    nano_kwargs are forwarded directly to nano_wait.wait()
    (smart, speed, verbose, log, etc).
    """
    return AdaptiveElement(
        driver,
        selector,
        timeout=timeout,
        nano_kwargs=nano_kwargs
    )
