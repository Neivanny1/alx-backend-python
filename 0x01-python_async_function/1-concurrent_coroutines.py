#!/usr/bin/env python3

"""
A couritine that return the list of all the delays (float values).
The list of the delays are in ascending order without
using sort() because of concurrency.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
