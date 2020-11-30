import unittest

from beamdice import dice

REPETITIONS = 100


class TestDice(unittest.TestCase):
  def test_roll(self):
    """
    Die rolls should be random. That is, over enough repetitions, the
    die roll should be something other than 6.
    """
    non_six = False
    for _ in range(REPETITIONS):
      roll = dice.roll()
      if roll != 6:
        non_six = True
    self.assertTrue(non_six, "The roller should eventually roll something other than 6.")

  def test_roll_distribution(self):
    """
    Dice should be able to roll all values in the 1 through 6 range,
    but never any values outside that range.
    """
    counts = [
      0,  # zero: never!
      0,  # one
      0,  # two
      0,  # three
      0,  # four
      0,  # five
      0,  # six
    ]
    for _ in range(REPETITIONS):
      roll = dice.roll()
      self.assertGreaterEqual(roll, 1)
      self.assertLessEqual(roll, 6)
      counts[roll] += 1
    for roll in [1, 2, 3, 4, 5, 6]:
      count = counts[roll]
      self.assertGreater(count, 0, f"Never saw {roll} (count={count})")
