import unittest
from tool import taxonomy
class Tests(unittest.TestCase):
 def test_pairs(self): self.assertEqual(taxonomy(['cat','dog'],['dog','dog']),{'cat->dog':1})
if __name__=='__main__': unittest.main()
