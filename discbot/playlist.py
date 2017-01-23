import os

class Song(object):
    def __init__(source):
        if not (is_file(source) or is_link(source)):
            raise ValueError("Source is neither a file nor a Youtube link"
                             "(does not start with `https://www.youtube.com/`)")
        self.source = source
        # gather meta data here

    @property
    def is_link(self):
        return self.source.startswith('https://www.youtube.com/')

    @property
    def is_file(self):
        return os.path.isfile(source)

def get_all_playlists():
    # placeholder
    return {'default' : Playlist(folder=None)}


class Playlist(object):
    """
    The class represents a single playlist
    """
    def __init__(self, folder):
        """
        The playlist can be initialized both by a folder containing mp3s
        or a link to a youtube video
        """
        pass

    # The following function need to be replaced
    # Right now they just provide an arbitrary interface

    def __getattr__(self, name):
        def func(*args, **kwargs):
            return "test.mp3"
        return func
