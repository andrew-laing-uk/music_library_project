from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List them out
for album in albums:
    print(album)

# Retrieve the album with id 1
album_1 = album_repository.find(1)
print(f"\nThe album with id 1 is {album_1}")
