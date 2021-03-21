def isSubset(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    for i in set2:
        if i not in set1:
            return False
    return True

# computational complexity of isSubset is O(n)
