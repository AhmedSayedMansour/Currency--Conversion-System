import hashlib
import time


def create_hash():
    """This function generate 40 character long hash"""
    h = hashlib.sha512()
    h.update(str(time.time()).encode('utf-8'))
    return h.hexdigest()[0:16]
