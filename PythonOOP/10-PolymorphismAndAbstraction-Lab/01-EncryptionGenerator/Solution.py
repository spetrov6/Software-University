class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        result = ""
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        for letter in self.text:
            ord_number = ord(letter) + other

            while ord_number > 126:
                ord_number -= 95

            while ord_number < 32:
                ord_number += 95

            result += chr(ord_number)

        return result