#!/usr/bin/env python3
"""2nd Task"""

import asyncio
import time
import typing
wait_random = __import__('0-basic_async_syntax').wait_random

Task = typing.TypeVar('Task')


def task_wait_random(max_delay: int = 10) -> Task:
    """ You will spawn wait_random n times with the specified max_delay """
    return asyncio.create_task(wait_random(max_delay))
