#!/usr/bin/env python3
"""1st Task"""

from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ takes in an integer argument (max_delay, with a default value of 10)
    named wait_random
    that waits for a random delay
    between 0 and max_delay (included and float value) seconds
    and eventually returns it"""
    wait_interval = uniform(0, max_delay)
    await sleep(wait_interval)
    return wait_interval
