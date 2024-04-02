from abc import ABC, abstractmethod
from typing import Any


class PolicyBase(ABC):
    def __init__(self, args: Any):
        self.args: Any = args
        self.validate_args()

    def validate_args(self) -> None:  # noqa: B027
        """Check that the policy arguments are valid, raise an exception if not."""
        pass

    @abstractmethod
    def process(self, input_url: str) -> str:
        """Return the input URL, modified according to the rules."""
