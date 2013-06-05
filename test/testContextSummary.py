import unittest
import sys
sys.path.append("../src")
from contextSummary import *

class TestContextSummary(unittest.TestCase):
    def setUp(self):
        db = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        self.summary = ContextSummary(db)
        
    def test_get(self):
        self.assertEqual(None, self.summary.get("FOO"))
        self.assertEqual(self.summary.get("Group0"), 0)
        self.assertEqual(self.summary.get("Group1"), 1)
        self.assertEqual(self.summary.get("Group2"), 2)
        self.assertEqual(self.summary.get("GroupsEnumerated"), 3)
        
    def test_put(self):
        self.assertEqual(None, self.summary.get("FOO"))
        
        self.summary.put("FOO", 100)
        self.assertEqual(100, self.summary.get("FOO"))
        
    def test_containKeys(self):
        self.assertFalse(self.summary.containsKey("FOO"))
        self.assertTrue(self.summary.containsKey("Group0"))
        
if __name__ == "__main__":
    unittest.main()