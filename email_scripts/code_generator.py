import os
import random


def generate_code():
    chars = list("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890А")
    random.shuffle(chars)
    verification_code = random.sample(chars, k=8)
    return "".join(verification_code)