from project.song import Song

class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [song for song in args]

    def add_song(self, song: Song):
        if self.published == True:
            return "Cannot add songs. Album is published."

        for k in range(0,len(self.songs)):
            if self.songs[k].name == song.name:
                return "Song is already in the album."
            
        if song.single == True:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published == True:
            return "Cannot remove songs. Album is published."

        foundSong = False

        for k in range(0, len(self.songs)):
            if self.songs[k].name == song_name:
                foundSong = True
                del self.songs[k]
                return f"Removed song {song_name} from album {self.name}."
                break

        if foundSong == False:
            return "Song is not in the album."

    def publish(self):
        if self.published == False:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."
    
    def details(self):
        output = f"Album {self.name}\n"

        for k in range(0, len(self.songs)):
            output += "== " + self.songs[k].get_info() + "\n"

        return output