#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
Return a float.
"""
from asyncio import run
import random
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start = time()
    run(wait_n(n, max_delay))
    stop = time()
    total_time = stop - start
    return total_time / n
