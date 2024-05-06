#!/usr/bin/env python3
"""2nd Task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list[float]:
    """ You will spawn wait_random n times with the specified max_delay """
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_interval_list = []
    # wait for coroutines to complete
    for future in asyncio.as_completed(tasks):
        result = await future
        wait_interval_list.append(result)
    return wait_interval_list
