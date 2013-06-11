import unittest
import sys
sys.path.append("../src")

from contextSummarySerializer import *
from contextSummary import *

class TestContextSummarySerializer(unittest.TestCase):
    def setUp(self):
        db = {"GroupsEnumerated":3,
              "Group0":100,"Group1":102,"Group2":103,
              "IdsAggregated":5,
              "Id0":10, "Id1":20, "Id2":30, "Id3":40, "Id4":50
              }
        self.summary = ContextSummary(1, db)
        self.s = ContextSummarySerializer()
        
    def test_writeObjectData(self):
        self.s.writeSummary(self.summary)
        # You can't compare the size alone because of the timestamp differences.
        #expected = "[0x1] ... "
        # the self.summary has total of 123 bytes
        self.assertEqual(167, self.s.size())
        
    def test_readObjectData(self):
        self.s.writeSummary(self.summary)
        summary = self.s.readSummary() # serializedData)
        #print summary.timestamp, type(summary.timestamp)
        self.assertTrue(summary == self.summary)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)