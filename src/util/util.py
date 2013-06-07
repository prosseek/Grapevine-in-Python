def removeAll(lists, removeLists):
    """
    Remove all of the removeLists from lists
    """
    result = []
    for member in lists:
        if member not in removeLists:
            result.append(member)
            
    return result