def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for each in lst:
        if isinstance(each, list) == False:
            return False

    return True


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
