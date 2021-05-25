def check_bmi(weight, height):
    """
    Function calculates body mass index (bmi_codewars = weight / height2) and returns:
    if bmi <= 18.5 return "Underweight"
    if bmi <= 25.0 return "Normal"
    if bmi <= 30.0 return "Overweight"
    if bmi > 30 return "Obese"
    :param weight: weight in kg
    :param height: height in m
    :return: information about bmi_codewars status
    """
    if weight <= 0 or height <= 0:
        return "Wrong value"

    bmi = float(weight / height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 25.0:
        return "Normal"
    elif 25.0 < bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
