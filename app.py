# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def print_all_album_titles(self):
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        for album in albums:
            print(f" * {album.id} - {album.title}")

    def print_all_artist_names(self):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        for artist in artists:
            print(f" * {artist.id} - {artist.name}")

    def run(self):
        print('Welcome to the music library manager!\n')
        print('What would you like to do?')
        print(' 1 - List all albums')
        print(' 2 - List all artists\n')

        while True:
            n = input('Enter your choice: ')
            if n == '1':
                self.print_all_album_titles()
                break
            elif n == '2':
                self.print_all_artist_names()
                break
            else:
                print(f"Error: invalid choice '{n}'")

if __name__ == '__main__':
    app = Application()
    app.run()
