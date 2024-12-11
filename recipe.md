# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker:
    def __init__(self):
        # Parameters:
        #   name: list
        pass # No code here yet

    def listening_to_song(self, song_name):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def display(self):
        # Side-effects:
        #   Show list of songs I have listened to
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE
"""
Test if the state of element changes in list
"""
def test_song_added_to_list():
    music_library = MusicLibrary()
    result = music_library.listening_to_song("Song_name_1") 
    assert result == "Song_name_1"

"""
Test if the show method returns a list of songs
"""
def test_display_songs():
    music_library = MusicLibrary()
    music_library.listening_to_song("Song_name_1") 
    music_library.listening_to_song("Song_name_2") 
    result = music_library.display()
    assert result # => list of songs



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
