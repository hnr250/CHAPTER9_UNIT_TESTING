class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


roman_numeral_map = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)


def to_roman(n):
    '''konwertuje liczbe calkowita do liczby rzymskiej'''
    if not 4000 > n > 0:
        raise OutOfRangeError("number out of range (it must be between 1 and 3999)")

    if not isinstance(n, int):
        raise NotIntegerError("parametr nie jest liczba calkowita")

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            #print('substracting %d from input, adding %s to output' % (integer, result))
    return result


def from_roman(s):
    '''konwertuje liczbe rzymska do liczby calkowitej'''
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result

