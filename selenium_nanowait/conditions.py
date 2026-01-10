def dom_ready(driver):
    """
    Checks if the DOM is fully loaded.
    """
    try:
        return driver.execute_script(
            "return document.readyState"
        ) == "complete"
    except Exception:
        return False


def is_visible(element):
    """
    Checks if an element is visible to the user.
    """
    try:
        return element.is_displayed()
    except Exception:
        return False
