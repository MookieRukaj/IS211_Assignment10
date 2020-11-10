DROP TABLE IF EXISTS artist, album, song;

CREATE TABLE artists 
(
    artist_id int PRIMARY KEY, 
    artist_name TEXT
    );

CREATE TABLE albums 
(
    album_id int PRIMARY KEY, 
    album_name text,	
    artist_id int
    );

CREATE TABLE songs 
(
    song_id int PRIMARY KEY, 
    song_name text,
    artist_id int,
    album_id int, 
    track_number int, 
    song_length int
    );
