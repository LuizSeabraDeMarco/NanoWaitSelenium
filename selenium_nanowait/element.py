import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from nano_wait import wait

from .conditions import is_visible, dom_ready
from .states import WaitState
from .config import get_config


class AdaptiveElement:
    """
    Adaptive Selenium element driven by explicit state transitions.
    """

    def __init__(
        self,
        driver,
        selector,
        timeout,
        nano_kwargs,
        test_context=None,
        hooks=None,
    ):
        self.driver = driver
        self.selector = selector
        self.timeout = timeout
        self.nano_kwargs = nano_kwargs
        self.test_context = test_context

        self._cached_element = None
        self._last_state = None

        self.hooks = hooks or {}
        self.config = get_config()

    # ---------- Internal helpers ----------

    def _emit_state(self, state, payload=None):
        if state != self._last_state:
            if self.hooks.get("on_state_change"):
                self.hooks["on_state_change"](state, payload)

            if self.config.on_state_change:
                self.config.on_state_change(state, payload)

            self._last_state = state

    def _find(self):
        if self._cached_element is not None:
            return self._cached_element

        return self.driver.find_element(By.CSS_SELECTOR, self.selector)

    def _evaluate_state(self, last_box):
        try:
            el = self.driver.find_element(By.CSS_SELECTOR, self.selector)

            if not dom_ready(self.driver):
                return WaitState.DOM_LOADING, last_box

            if not is_visible(el):
                return WaitState.NOT_VISIBLE, last_box

            box = el.rect
            if last_box is None or box != last_box:
                return WaitState.UNSTABLE_LAYOUT, box

            self._cached_element = el
            return WaitState.READY, box

        except StaleElementReferenceException:
            return WaitState.UNSTABLE_LAYOUT, last_box
        except Exception as e:
            return WaitState.ERROR, e

    # ---------- Core wait loop ----------

    def _wait_until_ready(self):
        start = time.time()
        last_box = None

        self._emit_state(WaitState.INIT)

        while time.time() - start < self.timeout:
            state, data = self._evaluate_state(last_box)
            self._emit_state(state, data)

            if state == WaitState.READY:
                if self.hooks.get("on_ready"):
                    self.hooks["on_ready"](self)

                if self.config.on_ready:
                    self.config.on_ready(self)

                return

            last_box = data
            wait(0.1, **self.nano_kwargs)

        self._emit_state(WaitState.TIMEOUT)

        if self.hooks.get("on_timeout"):
            self.hooks["on_timeout"](self)

        if self.config.on_timeout:
            self.config.on_timeout(self)

        raise TimeoutError(
            f"[selenium-nanowait] Element '{self.selector}' "
            f"not ready after {self.timeout}s"
        )

    # ---------- Public API ----------

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
