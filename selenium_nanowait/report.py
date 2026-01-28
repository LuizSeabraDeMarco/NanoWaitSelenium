from dataclasses import dataclass
from typing import Any, List, Tuple
import time


@dataclass
class StateEvent:
    timestamp: float
    state: Any
    payload: Any = None


class NanoWaitTimeoutReport(Exception):
    """
    Deterministic diagnostic report for selenium-nanowait timeouts.
    """

    def __init__(
        self,
        selector: str,
        timeout: float,
        timeline: List[StateEvent],
    ):
        self.selector = selector
        self.timeout = timeout
        self.timeline = timeline

        super().__init__(self._format())

    def _format(self) -> str:
        lines = [
            f"[selenium-nanowait] Timeout waiting for element '{self.selector}'",
            f"Timeout: {self.timeout:.2f}s",
            "",
            "Timeline:",
        ]

        t0 = self.timeline[0].timestamp if self.timeline else time.time()

        for event in self.timeline:
            delta = (event.timestamp - t0) * 1000
            payload = (
                f" | payload={event.payload}"
                if event.payload is not None
                else ""
            )
            lines.append(
                f"  - {event.state.name} @ {delta:.0f}ms{payload}"
            )

        return "\n".join(lines)
