"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self):
        self._playlist = {}


    def get_playlist_video(self, selected):

        for i in self._playlist:
            if i == selected:
                return  list(self._playlist[i])

    def get_playlist_key(self):

        return self._playlist.keys()
