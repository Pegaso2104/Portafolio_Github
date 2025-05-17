CREATE TABLE friends (
   id INTEGER, 
   name TEXT, 
   birthday DATE
);
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');
SELECT * 
FROM friends;
INSERT INTO friends (id, name, birthday) 
VALUES (2, 'Your Friend 1', 'YYYY-MM-DD');

INSERT INTO friends (id, name, birthday) 
VALUES (3, 'Your Friend 2', 'YYYY-MM-DD');
UPDATE friends 
SET name = 'Storm' 
WHERE name = 'Ororo Munroe';
ALTER TABLE friends 
ADD COLUMN email TEXT;
UPDATE friends 
SET email = 'storm@codecademy.com' 
WHERE name = 'Storm';

UPDATE friends 
SET email = 'friend1@email.com' 
WHERE name = 'Your Friend 1';

UPDATE friends 
SET email = 'friend2@email.com' 
WHERE name = 'Your Friend 2';
DELETE FROM friends 
WHERE name = 'Storm';
SELECT * 
FROM friends;
