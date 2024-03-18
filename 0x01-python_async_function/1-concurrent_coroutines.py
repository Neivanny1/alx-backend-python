#!/usr/bin/env python3
"""
A couritine that return the list of all the delays (float values).
The list of the delays are in ascending order without
using sort() because of concurrency.
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
