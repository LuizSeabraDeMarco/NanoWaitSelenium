class NanoWaitLibrary:
    """
    Robot Framework adapter.
    """

    def wait_for(self, driver, selector, timeout=None):
        from selenium_nanowait import wait_for
        return wait_for(driver, selector, timeout=timeout)
