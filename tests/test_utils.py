import unittest

from optimizely_platform import utils


class TestUtils(unittest.TestCase):
  """Tests for the various methods in utils."""

  def test_chunkify(self):
    """Test that the chunkify function works correctly.
    For example:
    a = [1, 2, 3, 4]
    The iterator from chunkify(a, 2) should yield:
      [1, 2]
      [3, 4]

    If b = [1, 2, 3]
    The iterator from chunkify(b, 2) should yield:
      [1, 2]
      [3]
    """
    long_list = [1, 2, 3]
    chunked_list = utils.chunkify(long_list, 2)
    for index, chunked in enumerate(chunked_list):
      if index == 0:
        self.assertEqual(2, len(chunked))
      else:
        self.assertEqual(1, len(chunked))
