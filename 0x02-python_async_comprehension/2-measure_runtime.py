#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    p_counter = time.perf_counter()
    coroutines = (async_comprehension() for i in range(4))
    await asyncio.gather(*coroutines)
    n_counter = time.perf_counter()
    return n_counter - p_counter