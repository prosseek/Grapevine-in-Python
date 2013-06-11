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
        
            
    def test_writeSummaries(self):
        ### SETUP
        db = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        summary = ContextSummary(1, db)
        summary.setTimestamp(time.time())
        time.sleep(0.01)
        db2 = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        summary2 = ContextSummary(2, db2)
        summary2.setTimestamp(time.time())
        
        self.s.writeSummaries([summary, summary2])
        self.assertEqual(len(self.s.result), 182) #<-- two summaries summarizes up to 182
        #print summary
        # http://stackoverflow.com/questions/12871775/python-compress-ascii-string
        # import zlib
        # comp = zlib.compress(self.s.result)
        # print len(comp) # 73
        # print len(zlib.decompress(comp)) # 182
        
    def test_readSummaries(self):
        db = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        summary = ContextSummary(1, db)
        summary.setTimestamp(time.time())
        time.sleep(0.01)
        db2 = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        summary2 = ContextSummary(2, db2)
        summary2.setTimestamp(time.time())
        
        expected = [summary, summary2]
        res = self.s.writeSummaries(expected)
        #print len(res)
        # result = []
        result = self.s.readSummaries() # res)
        for i in range(len(result)):
            self.assertEqual(result[i], expected[i])
        
if __name__ == "__main__":
    unittest.main(verbosity=2)