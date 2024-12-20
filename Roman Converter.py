class RomanConverter:
    def __init__(self, value):
        """Initialize the converter with an integer value."""
        self.value = value

    def to_roman(self):
        """Convert the integer value to a Roman numeral."""
        if not (0 < self.value < 4000):
            raise ValueError("Value must be between 1 and 3999")

        # Define the mapping of integers to Roman numerals
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = ""
        remaining_value = self.value

        for (integer, numeral) in roman_numerals:
            while remaining_value >= integer:
                result += numeral
                remaining_value -= integer

        return result
    
if __name__ == "__main__":
    try:
        value = int(input("Enter an integer value (1-3999): "))
        converter = RomanConverter(value)
        roman_numeral = converter.to_roman()
        print(f"The Roman numeral for {value} is: {roman_numeral}")
    except ValueError as e:
        print(f"Error: {e}")
