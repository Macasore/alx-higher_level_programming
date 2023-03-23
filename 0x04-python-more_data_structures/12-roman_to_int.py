#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 100, "D": 500}
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    else:
        roman_value = 0
        past_numeral = None

        for i in roman_string[::-1]:
            if past_numeral is None:
                roman_value += values[i]
                past_numeral = i
            else:
                if values[i] < values[past_numeral]:
                    roman_value -= values[i]
                    past_numeral = i
                else:
                    roman_value += values[i]
                    past_numeral = i
    return roman_value
