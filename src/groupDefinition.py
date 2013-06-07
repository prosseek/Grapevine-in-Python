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
        
        # newSummary should be a member of group
        if gid in groupIds:
            if uid not in currentGroupSummary.getMemberIds():
                currentGroupSummary.addMemberId(uid)
    
    def handleGroupSummary(self, currentGroupSummary, newGroupSummary):
        memberIds = currentGroupSummary.getMemberIds()
        newMemberIds = newGroupSummary.getMemberIds()
        
        #print memberIds
        #print newMemberIds
        
        # add only the members thatt is not in the memberIds
        # 1. find what is new in the newMemberIds
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
