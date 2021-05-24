def triangle(a, b, c):
    """
    Function takes three integers interpreted as lengths of the sides of a triangle.
    Function returns a message whether the triangle is equilateral, isosceles or scalene.
    :param a: triangle side 1
    :param b: triangle side 2
    :param c: triangle side 3
    :return: triangle type
    """
    if type(a) == int and type(b) == int and type(c) == int and a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and a + c > b:
            if a == b and a == c and b == c:
                return "Equilateral triangle"
            elif a == b or b == c or c == a:
                return "Isosceles triangle"
            else:
                return "Scalene triangle"
        else:
            return "wrong parameters"
    else:
        return "wrong parameters"
