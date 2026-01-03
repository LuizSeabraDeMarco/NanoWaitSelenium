import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from nano_wait import wait

from .conditions import is_visible, dom_ready


class AdaptiveElement:
    def __init__(self, driver, selector, timeout, nano_kwargs):
        self.driver = driver
        self.selector = selector
        self.timeout = timeout or 5.0
        self.nano_kwargs = nano_kwargs or {}

    def _find(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.selector)

    def _is_ready(self, last_box):
        try:
            el = self._find()

            if not is_visible(el):
                return False, last_box

            if not dom_ready(self.driver):
                return False, last_box

            box = el.rect
            if last_box is None or box != last_box:
                return False, box

            return True, box

        except StaleElementReferenceException:
            return False, last_box
        except Exception:
            return False, last_box

    def _wait_until_ready(self):
        start = time.time()
        last_box = None

        while time.time() - start < self.timeout:
            ready, last_box = self._is_ready(last_box)

            if ready:
                return

            # 🔑 Aqui está a integração REAL com nano-wait
            wait(
                0.1,              # base time (curto)
                **self.nano_kwargs
            )

        raise TimeoutError(
            f"Element '{self.selector}' did not reach a stable, visible DOM-ready state."
        )

    def click(self):
        self._wait_until_ready()
        self._find().click()
        return self

    def type(self, text, clear=True):
        self._wait_until_ready()
        el = self._find()
        if clear:
            el.clear()
        el.send_keys(text)
        return self

    def raw(self):
        self._wait_until_ready()
        return self._find()
