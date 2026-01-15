class NanoWaitConfig:
    def __init__(self):
        self.default_timeout = 5.0
        self.nano_kwargs = {}
        self.test_context = None


_global_config = NanoWaitConfig()


def configure(**kwargs):
    """
    Global configuration for selenium-nanowait.
    """
    for key, value in kwargs.items():
        setattr(_global_config, key, value)


def get_config():
    return _global_config
