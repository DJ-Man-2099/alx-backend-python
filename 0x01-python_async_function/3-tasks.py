#!/usr/bin/env python3
"""2nd Task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ You will spawn wait_random n times with the specified max_delay """
    return asyncio.create_task(wait_random(max_delay))
