class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {self.photos[page].index(label)}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            for slot in range(len(page)):
                if slot < len(page) - 1:
                    result += "[] "
                else:
                    result += "[]"
            result += "\n-----------\n"
        return result