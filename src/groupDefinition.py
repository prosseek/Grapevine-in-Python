from util.groupUtils import *
from util.util import *

class GroupDefinition(object):
    def __init__(self, gId):
        self.gId = gId
    
    def handleContextSummary(self, currentGroupSummary, newSummary):
        """
        Make sure currentGroupSummary has newSummary in its member
        when newSummary has currentGroupSummary as its group
        """
        uid = newSummary.getId()
        gid = currentGroupSummary.getId()
        groupIds = getDeclaredMemberships(newSummary)
        
        #print currentGroupSummary
        if gid in groupIds:
            if uid not in currentGroupSummary.getMemberIds():
                currentGroupSummary.addMemberId(uid)
        #print currentGroupSummary
    
    def handleGroupSummary(self, currentGroupSummary, newGroupSummary):
        memberIds = currentGroupSummary.getMemberIds()
        newMemberIds = newGroupSummary.getMemberIds()
        
        newMemberIds = removeAll(newMemberIds, memberIds)
        #print newMemberIds
        currentGroupSummary.addMemberIds(newMemberIds)
        
    def getId(self):
        return self.gId
    
if __name__ == "__main__":
    import sys
    sys.path.append("../test")
    from testGroupDefinition import *
    unittest.main(verbosity=2)
