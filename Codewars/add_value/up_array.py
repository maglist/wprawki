def up_array(arr):
    """
    Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
    The array can't be empty. Only non-negative, single digit integers are allowed.
    Example: the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
    [4, 3, 2, 5] would return [4, 3, 2, 6]
    :param arr: array of single digit integers
    :return: an array that has 1 added to the value represented by the array
    """
    for el in arr:
        if el not in range(10):
            return None
    try:
        tmp = "".join([str(el) for el in arr])
        return [int(el) for el in list(str(int(tmp) + 1))]
    except:
        return None