#!/usr/bin/env python3
"""1st Optional Task"""

import typing
# The types of the elements of the input are not know


def safe_first_element(lst: typing.Sequence[typing.Any]) \
        -> typing.Any | None:
    if lst:
        return lst[0]
    else:
        return None


# safe_first_element.__annotations__[
#     'return'] = 'typing.Union[typing.Any, NoneType]'
