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

MEMBERS_ENUMERATED = "MembersEnumerated"
MEMBER_PREFIX = "Member"

def getDeclaredMemberships(summary):
    """
    In Java: getDeclaredMemberships
    """
    result = []
    groupSize = summary.get(GROUP_DECLARATIONS_ENUMERATED)
    for i in range(groupSize):
        result.append(summary.get(GROUP_DECLARATION_PREFIX + str(i)))
    return result
    
def addDeclaredGroupMembership(summary, gId):
    """
    add gId into the membership, and re-enumerate
    ??? Why we just append the new one ???
    """
    declaredMemberships = getDeclaredMemberships(summary)
    # declaredMemberships.append(gId)
    #print declaredMemberships

    # I don't think this is necessary
    # for i, g in enumerate(declaredMemberships):
    #     summary.put(GROUP_DECLARATION_PREFIX + str(i), g)
    length = len(declaredMemberships)
    summary.put(GROUP_DECLARATION_PREFIX + str(length), gId)
        
    summary.put(GROUP_DECLARATIONS_ENUMERATED, length + 1)

def declaresGroupMembership(summary, groupId):
    """
    Check summary is a member of groupId
    In Java implementation: declaresGroupMembership
    """
    # 1. get group of summary
    groups = getDeclaredMemberships(summary)
    #print groups
    return groupId in groups
    
def addGroupMember(groupSummary, id):
    """
    For the group summary add id as its member
    """
    if groupSummary.containsKey(MEMBERS_ENUMERATED):
        membersEnumerated = groupSummary.get(MEMBERS_ENUMERATED)
    else:
        membersEnumerated = 0
        
    groupSummary.put(MEMBER_PREFIX + str(membersEnumerated), id)
    groupSummary.put(MEMBERS_ENUMERATED, membersEnumerated + 1)
    
def getGroupMembers(groupSummary):
    members = []
    membersEnumerated = groupSummary.get(MEMBERS_ENUMERATED)
    
if __name__ == "__main__":
    sys.path.append("../../test/util")
    from testGroupUtils import *
    
    unittest.main()