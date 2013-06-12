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

ID_AGGREGATION_PREFIX = "Id"
IDS_AGGREGATED = "IdsAggregated"

def getDeclaredMemberships(summary):
    """
    In Java: getDeclaredMemberships
    """
    result = []
    groupSize = summary.get(GROUP_DECLARATIONS_ENUMERATED)
    if groupSize is not None:
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
    *** id is added only when it's not already a member
    """
    if groupSummary.containsKey(MEMBERS_ENUMERATED):
        membersEnumerated = groupSummary.get(MEMBERS_ENUMERATED)
    else:
        membersEnumerated = 0
        
    # ???
    # add id only when id is not already a member
    members = getGroupMembers(groupSummary)
    if not (id in members):
        groupSummary.put(MEMBER_PREFIX + str(membersEnumerated), id)
        groupSummary.put(MEMBERS_ENUMERATED, membersEnumerated + 1)
    
def getGroupMembers(groupSummary):
    members = []
    membersEnumerated = groupSummary.get(MEMBERS_ENUMERATED)
    if membersEnumerated is not None:
        for i, value in enumerate(range(membersEnumerated)):
            #print i
            #print groupSummary.get(MEMBER_PREFIX + str(i))
            members.append(groupSummary.get(MEMBER_PREFIX + str(i)))
    return members
        
def setGroupMembers(groupSummary, memberIds):
    """
    Make memberIds (set) as a member of groupSummary
    ???
    Why do we make this too complicated ???
    Is this because the operation is expensive ???
    """
    previousNumberOfMembers = groupSummary.get(MEMBERS_ENUMERATED)
    newNumberOfMembers = len(memberIds)
    
    # You need this code to reset the number
    groupSummary.put(MEMBERS_ENUMERATED, 0)
    for memberId in memberIds:
        addGroupMember(groupSummary, memberId)
        
    if previousNumberOfMembers is not None:
        for index in range(newNumberOfMembers, previousNumberOfMembers):
            groupSummary.remove(MEMBER_PREFIX + str(index))
            
def isAggregated(summary, idToCheck):
    idsAggregated = getAggregatedIds(summary)
    return idToCheck in idsAggregated
    
def haveNoCommonAggregation(summary1, summary2):
    ids1 = getAggregatedIds(summary1)
    ids2 = getAggregatedIds(summary2)
    # http://www.saltycrane.com/blog/2008/01/how-to-find-intersection-and-union-of/
    return len (set(ids1) & set(ids2)) == 0
    
def getAggregatedIds(summary):
    ids = []
    idsAggregated = summary.get(IDS_AGGREGATED)
    if idsAggregated is not None:
        for i in range(idsAggregated):
            # mimic set operation 
            if not (i in ids):
                ids.append(summary.get(ID_AGGREGATION_PREFIX + str(i)))
    #print ids
    return ids
    
def addAggregatedId(summary, memberId):
    if summary.containsKey(IDS_AGGREGATED):
        idsAggregated = summary.get(IDS_AGGREGATED)
    else:
        idsAggregated = 0
        
    summary.put(ID_AGGREGATION_PREFIX + str(idsAggregated), memberId)
    summary.put(IDS_AGGREGATED, idsAggregated + 1)
    
def setAggregatedIds(summary, aggregatedIds):
    """
    It's not Evan's API
    """
    previousNumberOfIds = summary.get(IDS_AGGREGATED)
    #print summary
    newNumberOfIds= len(aggregatedIds)
    
    summary.put(IDS_AGGREGATED, 0)
    for memberId in aggregatedIds:
        addAggregatedId(summary, memberId)
        
    #print previousNumberOfIds
    if previousNumberOfIds is not None:
        for index in range(newNumberOfIds, previousNumberOfIds):
            #print index
            summary.remove(ID_AGGREGATION_PREFIX + str(index))
    
def aggregateIntoGroupSummary(groupSummary, summary):
    """
    I guess groupSummary is only with memebers, and 
    summary is only with aggregatedIds.
    
    This method is blindlingly merge the two information into one to
    store back into groupSummary. 
    """
    # step 1 - find all the group members from groupSummary and summary
    memberIds = getGroupMembers(groupSummary)
    ###??? summary doesn't have the groupMember ???
    memberIds += getGroupMembers(summary)
    # step 2 - update the groupSummary
    setGroupMembers(groupSummary, memberIds)
    
    # Do the same thing with aggregation
    aggregatedIds = getAggregatedIds(groupSummary)
    aggregatedIds += getAggregatedIds(summary)
    setAggregatedIds(groupSummary, aggregatedIds)
    ### temporal

def updateGroupAggForOneSummary(groupSummary, summary):
    gid = groupSummary.getId()
    #print declaresGroupMembership(summary, gid)
    if (declaresGroupMembership(summary, gid) or summary.getId() == gid) \
       and not isAggregated(groupSummary, summary.getId) \
       and haveNoCommonAggregation(groupSummary, summary):
        #print gid
        aggregateIntoGroupSummary(groupSummary, summary)
        
def updateGroupAgg(groupSummary, summaries):
    for summary in summaries:
        updateGroupAggForOneSummary(groupSummary, summary)

        
if __name__ == "__main__":
    sys.path.append("../../test/testUtil")
    from testGroupUtils import *
    
    unittest.main(verbosity=2)