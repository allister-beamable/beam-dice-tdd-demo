# beamdice.dice module

import random

LOTS = 10000


def roll():
  return random.randrange(LOTS) % 6
