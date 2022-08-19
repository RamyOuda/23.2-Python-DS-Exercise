def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    counts = {}
    for each in str(num1):
        counts[each] = counts.get(each, 0) + 1
    str1 = counts

    counts = {}
    for each in str(num2):
        counts[each] = counts.get(each, 0) + 1
    str2 = counts

    return str1 == str2

    # after looking at the solution, I see that I could have
    # made counting its own function instead of repeating it twice

    # def counter(nums):
    #     nums = str(nums)
    #     counts = {}

    #     for each in nums:
    #         counts[each] = counts.get(each, 0) + 1

    #     return counts

    # return counter(num1) == counter(num2)


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
