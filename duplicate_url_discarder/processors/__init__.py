from typing import Dict, Type

from .._rule import UrlRule
from .base import UrlProcessorBase
from .query_removal import QueryRemovalProcessor

_PROCESSOR_CLASSES: Dict[str, Type[UrlProcessorBase]] = {
    "queryRemoval": QueryRemovalProcessor,
}


def get_processor(rule: UrlRule) -> UrlProcessorBase:
    processor_cls: Type[UrlProcessorBase]
    if rule.processor not in _PROCESSOR_CLASSES:
        raise ValueError(f"No URL processor named {rule.processor}")
    processor_cls = _PROCESSOR_CLASSES[rule.processor]
    return processor_cls(rule.args)
