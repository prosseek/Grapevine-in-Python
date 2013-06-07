import unittest
import sys
sys.path.append("../src")
from contextHandler import *

class TestContextHandler(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_getInstance(self):
        ch = ContextHandler.getInstance()
        ch2 = ContextHandler.getInstance()
        self.assertEqual(ch, ch2)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)