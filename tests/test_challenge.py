from lib.challenge import MusicTracker

def test_song_1_added_to_list():
    music_library = MusicTracker()
    result = music_library.listening_to_song("Song_name_1") 
    assert result == "Song_name_1"

def test_song_2_added_to_list():
    music_library = MusicTracker()
    result = music_library.listening_to_song("Song_name_2") 
    assert result == "Song_name_2"

def test_display_songs():
    music_library = MusicTracker()
    music_library.listening_to_song("Song_name_1") 
    music_library.listening_to_song("Song_name_2") 
    result = music_library.display()
    assert result == ["Song_name_1", "Song_name_2"]

def test_display_songs_returns_list():
    music_library = MusicTracker()
    music_library.listening_to_song("Song_name_1") 
    music_library.listening_to_song("Song_name_2") 
    music_library.listening_to_song("Song_name_3") 
    result = music_library.display()
    assert result == ["Song_name_1", "Song_name_2", "Song_name_3"]