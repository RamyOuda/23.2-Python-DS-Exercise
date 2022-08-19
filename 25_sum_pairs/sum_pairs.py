def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    result = set()

    for each in nums:
        diff = goal - each

        if diff in result:
            return (diff, each)

        result.add(each)

    return ()

    # Looked at solution for this

    # I understand how the code works, but
    # the logic behind this is amazing... lol


print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))

print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
