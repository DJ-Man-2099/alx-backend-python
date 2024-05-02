#!/usr/bin/env python3
"""8th Task"""


import math
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v"""
    return (k, math.pow(v, 2))
