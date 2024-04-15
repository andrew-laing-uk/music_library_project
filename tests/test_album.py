from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_albums_construct():
    album = Album(1, "Test Title", 2024, 4)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2024
    assert album.artist_id == 4

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2024, 4)
    assert str(album) == "Album(1, Test Title, 2024, 4)"


"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Test Title", 2024, 4)
    album_2 = Album(1, "Test Title", 2024, 4)
    assert album_1 == album_2
