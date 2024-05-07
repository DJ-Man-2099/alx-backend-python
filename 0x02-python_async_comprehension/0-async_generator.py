#!/usr/bin/env python3
"""first task"""

import random
import asyncio
import typing


async def async_generator() -> typing.AsyncGenerator[int, None]:
    """coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
