**EXERCISE ONE**

Use a JOIN query to select the id and title of all the albums from Taylor Swift.

```sql
SELECT albums.id, albums.title FROM albums
    JOIN artists
    ON artists.id = albums.artist_id 
    WHERE artists.name = 'Taylor Swift';
```
Result:
```
 id |  title
----+----------
  6 | Lover
  7 | Folklore
```


**EXERCISE TWO**

Use a JOIN query to find the id and title of the (only) album from Pixies released in 1988.

```sql
SELECT albums.id, albums.title FROM albums
    JOIN artists
    ON artists.id = albums.artist_id 
    WHERE artists.name = 'Pixies' 
    AND albums.release_year = 1988;
```
Result:
```
 id |    title
----+-------------
  2 | Surfer Rosa
```

***CHALLENGE***

Find the album_id and title of all albums from Nina Simone released after 1975.

```sql
SELECT albums.id, albums.title FROM albums
    JOIN artists
    ON artists.id = albums.artist_id 
    WHERE artists.name = 'Nina Simone' 
    AND albums.release_year > 1975;
```

Result:
```
 id |       title
----+--------------------
  9 | Baltimore
 11 | Fodder on My Wings
```