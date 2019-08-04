import unittest
from tools import Tools


class TestStringMethods(unittest.TestCase):

	def test_positive(self):
		tools = Tools()
		self.assertEqual(tools.plus(1, 2), 3)
		self.assertEqual(tools.plus(5, 5), 10)
		self.assertEqual(tools.plus(137, 49), 186)

	def test_negative(self):
  		tools = Tools()
		self.assertNotEqual(tools.plus(2, 3), 6)

if __name__ == '__main__':
    unittest.main()