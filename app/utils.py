from asyncio.log import logger
import logging

def todict(ch):
    ch = ch.replace('people','')
    ch = ch.replace(' ','')
    L = ch.split(':')
    return [L[0].lower(), L[1]]

logging.basicConfig(
format='%(asctime)s %(levelname)-8s %(message)s',
level=logging.INFO,
datefmt='%Y-%m-%d %H:%M:%S')
