def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    # vvv -- why doesn't this work? -- vvv
    # lst = phrase.split(' ')

    # for each in lst:
    #     each = each.capitalize()  <-- this is not changing the value of 'each', why?

    # return ' '.join(lst)

    lst = []

    for each in phrase.split(' '):
        lst.append(each.capitalize())

    return ' '.join(lst)

    # return ' '.join([each.capitalize() for each in phrase.split(' ')])


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
