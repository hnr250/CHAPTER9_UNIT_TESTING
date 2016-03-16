import re


class OutOfRangeError(ValueError):
    pass


class NotIntegerError(ValueError):
    pass


class InvalidRomanNumeralError(ValueError):
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


roman_numeral_pattern = re.compile('''
    ^                       # the beginning of string
    M{0,3}                  # thousands - 0 to 3
    (CM|CD|D?C{0,3})        # hundreds - 900 (CM), 400 (CD),
                            # 0 - 300 (Cs - 0 to 3), 500 - 800 (D and Cs from 0 to 3)
    (XC|XL|L?X{0,3})        # tens - 90 (XC), 40 (XL),
                            # 0 - 30 (Xs: 0 to 3), 50 - 80 (L and Xs: 0 - 3)
    (IX|IV|V?I{0,3})        # ones - 9 (IX), 4 (IV),
                            # 0 - 3 (Is 0 to 3), 5 - 8 (V and 0 to 3 Is)
    $                       # end of string
    ''', re.VERBOSE)


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
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError("Invalid Roman numeral: {0}".format(s))

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result

