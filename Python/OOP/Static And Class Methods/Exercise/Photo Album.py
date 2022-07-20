class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = list()

        for k in range(0, pages):
            self.photos.append([])

    @staticmethod
    def from_photos_count(photos_count: int):
        return PhotoAlbum(photos_count / 4)
    
    def add_photo(self, label: str):
        for k in range(0, len(self.photos)):

            if len(self.photos[k]) != 4:
                self.photos[k].append(label)
                return f"{label} photo added successfully on page {k + 1} slot {len(self.photos[k])}"
            else:
                continue

        return "No more free slots"

    def display(self):
        output = "-----------\n"

        for k in range(0, len(self.photos)):

            for j in range(0, len(self.photos[k])):
                if self.photos[k][j] != "":
                    output += "[] "

            output += "\n-----------\n"
        
        return output


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
