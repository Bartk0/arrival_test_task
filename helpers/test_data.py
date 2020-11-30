import random
import string

from helpers.bears import BearTypes


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def bears_generator(bears_count=10):
    for i in range(bears_count):
        bear_name = random_string("bear", 20)
        bear_type = [BearTypes.POLAR, BearTypes.GUMMY, BearTypes.BLACK, BearTypes.BROWN][random.randrange(3)]
        bear_age = random.uniform(-1.0, 80.5)
        yield bear_name, bear_type, bear_age
