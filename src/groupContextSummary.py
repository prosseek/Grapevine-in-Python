from contextSummary import *
from util.groupUtils import *

class GroupContextSummary(ContextSummary):
    #def __init__(self, gId, db = {}):
    def __init__(self, gId, db = None):
        if db == None: db = {}
        #print db
        super(GroupContextSummary, self).__init__(gId, db)
        
    def __str__(self):
        result = "(%d):%s" % (self.getId(), self.db)
        return result
        
    def getMemberIds(self):
        return getGroupMembers(self)
        
    def setMemberIds(self, ids):
        return setGroupMembers(self, ids)
        
    def addMemberId(self, uid):
        return addGroupMember(self, uid)
        
    def addMemberIds(self, ids):
        for uid in ids:
            self.addMemberId(uid)
            
    def getGroupCopy(self):
        return self.getCopy()
    
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testGroupContextSummary import *
    unittest.main(verbosity=2)