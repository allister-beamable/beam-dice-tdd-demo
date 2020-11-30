# beamdice.dice module

import random

LOTS = 10000


def roll():
  face = random.randrange(LOTS) % 6
  if face > 0:
    return face
  else:
    return roll()
