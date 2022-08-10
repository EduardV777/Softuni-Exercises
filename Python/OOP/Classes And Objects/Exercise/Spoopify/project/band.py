from project.album import Album

class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for k in range(0, len(self.albums)):
            if self.albums[k].name == album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        foundAlbum = False
        publishedOrNot = False
        
        for k in range(0, len(self.albums)):
            if self.albums[k].name == album_name:

                if self.albums[k].published == True:
                    publishedOrNot = True
                    break

                del self.albums[k]
                foundAlbum = True
                break
        
        if publishedOrNot == True:
            return "Album has been published. It cannot be removed."

        if foundAlbum == True:
            return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        output = f"Band {self.name}\n"

        for k in range(0, len(self.albums)):
            output += self.albums[k].details() + "\n"

        return output