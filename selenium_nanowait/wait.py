from .element import AdaptiveElement


def wait_for(driver, selector, *, timeout=None, **nano_kwargs):
    """
    Entry point for selenium-nanowait.

    Parameters
    ----------
    driver : selenium.webdriver
        Active Selenium WebDriver instance

    selector : str
        CSS selector of the element

    timeout : float, optional
        Maximum wait time (seconds)

    nano_kwargs :
        Forwarded directly to nano_wait.wait()
        (smart, speed, verbose, log, adaptive_factor, etc.)

    Returns
    -------
    AdaptiveElement
        A stabilized, adaptive Selenium element
    """
    return AdaptiveElement(
        driver=driver,
        selector=selector,
        timeout=timeout,
        nano_kwargs=nano_kwargs
    )
