import unittest

from beamdice import dice


class TestDice(unittest.TestCase):
  def test_roll(self):
    """
    Die rolls should be random. That is, over enough repetitions, the
    die roll should be something other than 6.
    """
    repetitions = 100
    non_six = False
    for _ in range(repetitions):
      roll = dice.roll()
      if roll != 6:
        non_six = True
    self.assertTrue(non_six, "The roller should eventually roll something other than 6.")
