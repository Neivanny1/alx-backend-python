#!/usr/bin/env python3
"""
A couritine that return the list of all the delays (float values).
The list of the delays are in ascending order without
using sort() because of concurrency.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Waits for ran delay until max_delay, returns list of actual delays
    """
    spawns = []
    delays = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delays.append(x.result()))
        spawns.append(delayed_task)

    for spawn in spawns:
        await spawn
    return delays
