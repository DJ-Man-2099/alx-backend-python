#!/usr/bin/env python3
"""2nd Optional Task"""

import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any, default=None):
    if key in dct:
        return dct[key]
    else:
        return default
