#!/usr/bin/env python3
"""1st Optional Task"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) \
        -> typing.Union[typing.Any, None]:
    """Return the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
