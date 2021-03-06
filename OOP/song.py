#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 15, 2018 7:52:07 AM$"

class Song:
    """ class to represent a song

        Attributes:
            title (str): The title of the song
            artist (Artist): An artist object representing the song's creator
            duration (int): The duration of the song in seconds.  May be zero.
        """

    def __init__(self, title, artist, duration=0):
        """ song init method

        Args:
            title (str): Initializes the 'title' attribute
            artist (Artist): An Artist object representing the song's creator
            duration (Optional(int)): Initial value for the 'attribute'.
                Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

#help(Song)
#help(Song.__init__)
#print(Song.__doc__)
#print(Song.__init__.__doc__)

class Album:
    """ Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible for the album.and
            If not specified, the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist == None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): a song to add
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic class to store artist details

    Attributes:
        name (str): the name of the artist
        albums (List[Album]): A list of the albums by this artist.

    Methods:
        add_album: Use to add a new album to the artist's album list.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (not yet implemented)
        """
        self.albums.append(album)

def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None

def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt", "r", encoding='utf-8') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
#            try:
#                print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
#            except UnicodeEncodeError:
#                print("ENCODING ERROR: {}:{}:{}:{}".format(artist_field, album_field.encode('ascii', 'replace'), year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_artist == None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)
                
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list

def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison with the original file """
    with open("checkfile.txt", 'w', encoding='utf-8') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)
 
if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists.".format(len(artists)))
    create_checkfile(artists)