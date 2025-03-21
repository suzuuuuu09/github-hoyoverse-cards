import random
import hashlib
import string
import time

def generate_ds():
    """DS（Dynamic Secret）を生成する"""
    salt = "6s25p5ox5y14umn1p61aqyyvbvvl3lrt"
    t = int(time.time())
    r = ''.join(random.choices(string.ascii_letters, k=6))
    h = hashlib.md5(f"salt={salt}&t={t}&r={r}".encode()).hexdigest()
    return f"{t},{r},{h}"