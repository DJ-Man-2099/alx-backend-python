#!/usr/bin/env python3
"""9th Task"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """length of elements in a list"""
    return [(i, len(i)) for i in lst]
