from enum import Enum, auto


class WaitState(Enum):
    INIT = auto()
    DOM_LOADING = auto()
    NOT_VISIBLE = auto()
    UNSTABLE_LAYOUT = auto()
    READY = auto()
    TIMEOUT = auto()
    ERROR = auto()
