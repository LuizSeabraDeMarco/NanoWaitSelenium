def dom_ready(driver):
    try:
        return driver.execute_script(
            "return document.readyState"
        ) == "complete"
    except Exception:
        return False


def is_visible(element):
    try:
        return element.is_displayed()
    except Exception:
        return False
