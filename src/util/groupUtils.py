# public static final int GROUP_ID_OFFSET = 10000;
# public static final String MEMBER_PREFIX = "Member";
# public static final String MEMBERS_ENUMERATED = "MembersEnumerated";
# public static final String GROUP_DECLARATION_PREFIX = "Group";
# public static final String ID_AGGREGATION_PREFIX = "Id";
# public static final String GROUP_DECLARATIONS_ENUMERATED = "GroupsEnumerated";
# public static final String IDS_AGGREGATED = "IdsAggregated";

import sys
sys.path.append("..")
from contextSummary import *

GROUP_DECLARATIONS_ENUMERATED = "GroupsEnumerated"
GROUP_DECLARATION_PREFIX = "Group"

def getDeclaredMemberships(summary):
    """
    In Java: getDeclaredMemberships
    """
    result = []
    groupSize = summary.get(GROUP_DECLARATIONS_ENUMERATED)
    for i in range(groupSize):
        result.append(summary.get(GROUP_DECLARATION_PREFIX + str(i)))
    return result
    
def addToGroups(summary, gId):
    """
    addDeclaredGroupMembership
    """
    groups = getGroups(summary)
    

def checkGroupMembership(summary, groupId):
    """
    Check summary is a member of groupId
    In Java implementation: declaresGroupMembership
    """
    # 1. get group of summary
    groups = getDeclaredMemberships(summary)
    print groups
    return groupId in groups
    
if __name__ == "__main__":
    db = {"GroupsEnumerated":3,
          "Group0":0,"Group1":1,"Group2":2
          }
    summary = ContextSummary(db)
    print checkGroupMembership(summary, 4)