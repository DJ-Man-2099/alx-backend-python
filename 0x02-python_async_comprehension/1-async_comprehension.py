#!/usr/bin/env python3
"""first task"""

import random
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """coroutine will collect 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers"""
    return [i async for i in async_generator()]
