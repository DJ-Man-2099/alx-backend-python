#!/usr/bin/env python3
"""1st Optional Task"""

import typing
# The types of the elements of the input are not know


def safe_first_element(lst: typing.Sequence[typing.Any]) \
        -> typing.Union[typing.Any, typing.Type[None]]:
    if lst:
        return lst[0]
    else:
        return None
