DROP TABLE IF EXISTS my_playlist;

CREATE TABLE IF NOT EXISTS playlist (
  id integer PRIMARY KEY AUTOINCREMENT,
  song_name text NOT NULL,
  artist text NOT NULL,
  duration text
);

INSERT INTO playlist (song_name, artist, duration)
VALUES ('22', 'Taylor Swift', '3.30');

ALTER TABLE playlist
RENAME TO my_playlist;

ALTER TABLE my_playlist
ADD album text default 'red';

INSERT INTO my_playlist (song_name, artist, duration, album)
VALUES ('Lover', 'Taylor Swift', '4.01', 'Lover');

DELETE FROM my_playlist
WHERE id = 2;

UPDATE my_playlist
SET artist = 'Taylor'
WHERE id = 1;