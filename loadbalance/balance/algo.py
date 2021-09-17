from typing import List
import random
import zlib

def round_robin(urls: List[str], count):
    count += 1
    return urls[count%len(urls)]

def get_random(urls: List[str]):
    return urls[random.randint(0,len(urls)-1)]

def ip_hash(urls: List[str], ip: str):
    # some hash func...
    num = zlib.crc32(ip)
    return urls[num%len(urls)]