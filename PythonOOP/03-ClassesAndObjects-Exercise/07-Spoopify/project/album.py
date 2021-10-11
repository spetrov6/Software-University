from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if song not in self.songs:
            if not self.published:
                if not song.single:
                    self.songs.append(song)
                    return f"Song {song.name} has been added to the album {self.name}."

                return f"Cannot add {song.name}. It's a single"

            return "Cannot add songs. Album is published."

        return "Song is already in the album."

    def remove_song(self, song_name: str):
        if not self.published:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."

            return "Song is not in the album."

        return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        info = f"Album {self.name}\n"
        for song in self.songs:
            info += f"== {song.get_info()}\n"
        return info

