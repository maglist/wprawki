def find_uniq(l):
    """
    There is an array with some numbers. All numbers are equal except for one. It’s guaranteed that
    array contains at least 3 numbers.
    :param l: input list
    :return: unique element
    """
    for i in l:
        if type(i) not in [float, int]:
            return "Wrong type of input"
    for i in l:
        if l.count(i) == 1:
            return i
    return "Lack of unique element"

