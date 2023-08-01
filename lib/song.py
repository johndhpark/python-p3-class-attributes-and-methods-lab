class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.add_to_genres(genre)
            cls.genre_count[genre] = 0

        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.add_to_artists(artist)
            cls.artist_count[artist] = 0

        cls.artist_count[artist] += 1

