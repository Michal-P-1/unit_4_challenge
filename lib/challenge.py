class MusicTracker:
    def __init__(self):
        self.songs = []

    def listening_to_song(self, song_name):
        self.songs.append(song_name)
        return song_name

    def display(self):
        return self.songs