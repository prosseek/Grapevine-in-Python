import unittest
import sys

sys.path.append("../../src/util")
sys.path.append("../../src")
from groupUtils import *
from contextSummary import *

class TestGroupUtils(unittest.TestCase):  
    def setUp(self):
        db = {"GroupsEnumerated":3,
              "Group0":0,"Group1":1,"Group2":2
              }
        self.summary = ContextSummary(db)
        
        groupDbNull = {}
        self.groupSummaryNull = ContextSummary(groupDbNull)
        
        groupDb = {"MembersEnumerated":2,
                   "Mmeber0":10, "Member1":20}
        self.groupSummary = ContextSummary(groupDb)
              
    def test_getDeclaredMemberships(self):
        groups = getDeclaredMemberships(self.summary)
        # http://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets-in-python
        self.assertTrue(sorted(groups) == sorted([0,2,1]))
        
    def test_addDeclaredGroupMembership(self):
        self.assertFalse(declaresGroupMembership(self.summary, 100))
        groups = getDeclaredMemberships(self.summary)
        self.assertTrue(len(groups) == 3)
        
        addDeclaredGroupMembership(self.summary, 100)
        
        self.assertTrue(declaresGroupMembership(self.summary, 100))
        groups = getDeclaredMemberships(self.summary)
        self.assertTrue(len(groups) == 4)
        
    def test_declaresGroupMembership(self):
        self.assertFalse(declaresGroupMembership(self.summary, 4))
        self.assertTrue(declaresGroupMembership(self.summary, 2))
        #print self.summary
        
    def test_addGroupMember(self):
        addGroupMember(self.groupSummaryNull, 1200)
        
    def test_getGroupMembers(self):
        members = getGroupMembers(self.groupSummaryNull)


if __name__ == "__main__":
    unittest.main()
    