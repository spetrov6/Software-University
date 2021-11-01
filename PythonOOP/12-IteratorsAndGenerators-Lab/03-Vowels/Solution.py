class vowels:
    def __init__(self, text):
        self.vowels = "AEOIUYaeoiuy"
        self.text = [letter for letter in text if letter in self.vowels]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.text[current_index]