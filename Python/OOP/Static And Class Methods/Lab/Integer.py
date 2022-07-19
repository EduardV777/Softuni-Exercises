from math import floor

class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if type(float_value) == float:
            return Integer(floor(float_value))
        else:
            return "value is not a float"

    @staticmethod
    def from_roman(roman_value):
        romanNumbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI']

        for k in range(0, len(romanNumbers)):
            if roman_value == romanNumbers[k]:
                intValue = k+1
                break

        if intValue != 999:
            return Integer(intValue)

    @staticmethod
    def from_string(value):
        try:
            if type(value) != str:
                raise ValueError()
            return Integer(int(value))
        except ValueError:
            return "wrong type"




first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("XIX")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
