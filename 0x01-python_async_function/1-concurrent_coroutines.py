#!/usr/bin/env python3
"""multiple coroutines"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines"""
    coroutines = (wait_random(max_delay) for i in range(n))
    lst = await asyncio.gather(*coroutines)
    return sorted(lst)