#!/usr/bin/env python3
'''
Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
Arguments: n: int, max_delay: int = 10
'''

from typing import List
import asyncio
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''
    Execute task_wait_random and returns sorted list of delay
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in tasks:
        await task
        delays.append(task.result())
    return delays
