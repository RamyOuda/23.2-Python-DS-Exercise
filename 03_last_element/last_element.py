def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """

    return None if len(lst) == 0 else lst.pop()


print(last_element([]) is None)
print(last_element([1, 2, 3]))
