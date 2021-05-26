def letter_count(s):
    """
    Function counts letters (case insensitive) in a given string and return the letter count in a dictionary
    with 'letter' as key and count as 'value'.
    :param s: input string
    :return: dictionary with 'letter' as key and number of letter occurrences as 'value'
    """
    my_dict = {}
    for letter in s:
        if letter.lower() not in my_dict.keys():
            my_dict[letter.lower()] = 1
        else:
            my_dict[letter.lower()] += 1
    return my_dict

print(letter_count("MagDaLEnA"))

