#!/usr/bin/env python3
"""2nd Optional Task"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """Return the value of a key in a dictionary or the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
