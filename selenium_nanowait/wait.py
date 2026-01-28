from .element import AdaptiveElement
from .config import get_config


def wait_for(
    driver,
    selector,
    *,
    timeout=None,
    on_state_change=None,
    on_ready=None,
    on_timeout=None,
    on_error=None,
    **nano_kwargs,
):
    """
    Entry point for selenium-nanowait.
    """
    config = get_config()

    hooks = {
        "on_state_change": on_state_change,
        "on_ready": on_ready,
        "on_timeout": on_timeout,
        "on_error": on_error,
    }

    return AdaptiveElement(
        driver=driver,
        selector=selector,
        timeout=timeout or config.default_timeout,
        nano_kwargs={**config.nano_kwargs, **nano_kwargs},
        test_context=config.test_context,
        hooks=hooks,
    )
