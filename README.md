# selenium-nanowait

State-based adaptive synchronization for Selenium — powered by the NanoWait engine.

## 🚀 What is `selenium-nanowait`?

`selenium-nanowait` is a support library for Selenium that **eliminates fragile time-based waits**, synchronizing browser actions with the actual page state, not with arbitrary *timeouts*.

Instead of guessing how long to wait (`time.sleep(5)` or `WebDriverWait(10)`), `selenium-nanowait` waits for what really matters:

* **Element visibility**
* **Layout stability** (constant position and size)
* **DOM readiness** (`document.readyState === "complete"`)

Furthermore, `selenium-nanowait` is designed for direct and transparent integration with testing frameworks, allowing for immediate adoption in QA, GUI automation, and teaching environments.

It's not a replacement for Selenium, but rather a direct enhancement that works alongside your existing code. You continue using Selenium as you always have — `selenium-nanowait` simply makes the wait deterministic, adaptive, and reliable.

---

## 🧠 Design Philosophy

`selenium-nanowait` follows three strict rules:

1. **Complementary**, never replace Selenium.

2. **Wait for states**, not for time.

3. **Remain explicit**, predictable, and *opt-in*.

There is no *monkey-patching*, hidden globals, or custom *drivers*. Integration with testing *frameworks* is *plug-and-play*, non-invasive.

---

## 🛠️ Installation

```bash
pip install selenium-nanowait
```

### Requirements

* Python ≥ 3.8
* Selenium ≥ 4.x
* NanoWait ≥ 4.0.0

---

## 💡 Quick Start: The `wait_for` Function

The `wait_for` function is the main entry point of the library. It encapsulates all the adaptive synchronization logic and returns an element ready for interaction.

### Before (Fragile, Time-Based)

```python
import time
from selenium.webdriver.common.by import By

time.sleep(3)
driver.find_element(By.ID, "submit").click()

```

### After (State-Aware, Deterministic)

```python
from selenium_nanowait import wait_for

wait_for(driver, "#submit").click()

```

---

## ⚙️ Main API

### `wait_for()`

```python
wait_for(
driver,
selector: str,

*,
timeout: float | None = None,
**nano_kwargs

```

Returns an `AdaptiveElement`, a lightweight wrapper that extends Selenium's behavior without Replace it.

### `AdaptiveElement` Methods

| Method | Description | Example |

| ------------------------- | ----------------------------------------- | --------------------------------------------------- |

| `.click()` | Waits for stability and executes the click | `wait_for(driver, "#login").click()` |

| `.type(text, clear=True)` | Waits for readiness and types text | `wait_for(driver, "#email").type("user@email.com")` |

| `.raw()` | Returns the native Selenium `WebElement` | `el = wait_for(driver, "#submit").raw()` |

---

## 🔎 Visual Stability Check

An element is only considered ready when:

* It is visible (`is_displayed`)
* The DOM is fully loaded
* Its position and size remain constant between consecutive checks

This approach eliminates intermittent failures caused by layout shifts, animations, or late reflows.

--

## 🧪 Plug-and-Play Integration with Testing Frameworks

`selenium-nanowait` is designed for immediate adoption in testing environments, without requiring manual configuration or structural changes to the project.

### ✅ Pytest (Automatic)

```python
def test_login(driver):

wait_for(driver, "#login").click()

```

The Pytest plugin is automatically loaded via entrypoint, allowing future extensions such as:

* automatic screenshots on failures
* logs per test
* integration with reports

### ✅ unittest (Optional Mixin)

```python
from selenium_nanowait.unittest_adapter import NanoWaitTestCaseMixin

class TestUI(NanoWaitTestCaseMixin, unittest.TestCase):

...
```

### ✅ Robot Framework

```robotframework
Wait For css:#submit
```

---

## ⚙️ Global Configuration (Optional)

```python
from selenium_nanowait import configure

configure(
default_timeout=10,
nano_kwargs={"smart": True, "verbose": False}

```

The configuration is applied globally, respecting the *opt-in* philosophy.

---

## 🔬 NEW: Stateful Deterministic Diagnostics

`selenium-nanowait` can generate **deterministic diagnostic reports** when a wait fails, explaining *why* the element did not become ready.

### Enabling Diagnostics

```python
from selenium_nanowait import configure

configure(diagnostic=True)

```

When enabled, the library logs a **state timeline** during the wait.

### Example of error generated

```text
[selenium-nanowait] Timeout waiting for element '#submit'
Timeout: 5.00s

Timeline: 
- INIT @ 0ms 
- DOM_LOADING @ 140ms 
-NOT_VISIBLE @ 780ms

- UNSTABLE_LAYOUT @ 2200ms

- UNSTABLE_LAYOUT @ 4100ms

This report makes UI crashes:

* **explainable**
* **reproducible**
* **diagnosable in CI**

No generic *logs* or blind *timeouts*.

> 💡 Diagnostics are fully *opt-in* and do not affect performance when disabled.

---

## ⏱️ Adaptive Waiting (NanoWait)

The NanoWait engine:

* dynamically adjusts the *polling* frequency
* avoids *busy-waiting*
* adapts to system performance

---

## 🧠 Why is `selenium-nanowait` different?

| Feature | ❌ Traditional Waits | ✅ `selenium-nanowait` |

| -------------- | -------------------- | ---------------------- |

| Base | Fixed time | Actual page state |

| Scope | Global/conditional | Adaptive element |

| Wait | Estimate | Adaptive backoff |

| Robustness | Fragile | Layout-aware |

| Diagnostic | Non-existent | Deterministic |

| QA Integration | Manual | Plug-and-play |

---

## 📦 Project Metadata

* **License**: MIT
* **Author**: Luiz Filipe Seabra de Marco
* **Status**: Production ready (v0.4)
* **Summary**: `selenium-nanowait` makes Selenium wait for reality — and now explains when it doesn't happen.