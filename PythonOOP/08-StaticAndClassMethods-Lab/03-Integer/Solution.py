from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(floor(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        return cls(Integer.__roman_to_int(value))

    @classmethod
    def from_string(cls, value):
        value = str(value)
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

    @staticmethod
    def __roman_to_int(s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number