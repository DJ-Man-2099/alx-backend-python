#!/usr/bin/env python3
"""2nd Task"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ You will spawn wait_random n times with the specified max_delay """
    time_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_end = time.time()
    return (time_end - time_start)/n
