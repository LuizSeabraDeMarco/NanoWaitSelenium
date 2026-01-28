class NanoWaitConfig:
    """
    Global configuration for selenium-nanowait.
    Explicit, opt-in and deterministic by design.
    """

    def __init__(self):
        # ---------- Core behavior ----------
        self.default_timeout = 5.0
        self.nano_kwargs = {}
        self.test_context = None

        # ---------- Diagnostics ----------
        # Enables state timeline collection
        self.diagnostic = False

        # Max number of state events kept in memory
        # Prevents unbounded growth in long waits
        self.max_timeline_events = 50

        # ---------- Global hooks ----------
        # Called on state transitions
        self.on_state_change = None

        # Called when element becomes READY
        self.on_ready = None

        # Called on TIMEOUT
        self.on_timeout = None

        # Called on ERROR state
        self.on_error = None


# Global singleton config (explicit by design)
_global_config = NanoWaitConfig()


def configure(**kwargs):
    """
    Global configuration for selenium-nanowait.

    Example:
        configure(
            default_timeout=10,
            diagnostic=True,
            nano_kwargs={"smart": True}
        )
    """
    for key, value in kwargs.items():
        if not hasattr(_global_config, key):
            raise AttributeError(
                f"[selenium-nanowait] Invalid config option: '{key}'"
            )
        setattr(_global_config, key, value)


def get_config():
    """
    Returns the global NanoWait configuration.
    """
    return _global_config
