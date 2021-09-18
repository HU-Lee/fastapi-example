from typing import List
import random
import zlib

def round_robin(urls: List[str], count: int):
    count += 1
    return count, urls[count%len(urls)]

def weighted_round_robin(urls: List[str], weights: List[str], count: int):
    num = (count)%sum(weights)
    for i, w in enumerate(weights):
        if num < w:
            return count+1, urls[i]
        num -= w
    return count, None

def get_random(urls: List[str]) -> str:
    return urls[random.randint(0,len(urls)-1)]

def ip_hash(urls: List[str], ip: str) -> str:
    # some hash func...
    num = zlib.crc32(ip.encode("utf8"))

    return urls[num%len(urls)]