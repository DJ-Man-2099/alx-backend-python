#!/usr/bin/env python3
"""first task"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers"""
    start_time = time()
    tasks = []
    for _ in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end_time = time()
    return end_time - start_time
