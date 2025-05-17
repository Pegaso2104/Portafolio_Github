 -- 1. Obtener las 5 historias más populares con las puntuaciones más altas
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- 2. Encontrar el puntaje total de todas las historias
SELECT SUM(score)
FROM hacker_news;

-- 3. Encontrar los usuarios con más de 200 puntos combinados
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200;

-- 4. Calcular el porcentaje de puntuación total de estos usuarios
SELECT (SUM(score) * 1.0) / (SELECT SUM(score) FROM hacker_news) AS percentage
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200;

-- 5. Contar cuántas veces cada usuario ha publicado el enlace de rickroll
SELECT user, COUNT(*)
FROM hacker_news
WHERE url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
GROUP BY user;

-- 6. Categorizar cada historia según su fuente (GitHub, Medium, New York Times)
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
END AS 'Source'
FROM hacker_news;

-- 7. Contar las historias por cada fuente
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
END AS 'Source',
   COUNT(*) AS story_count
FROM hacker_news
GROUP BY 1;

-- 8. Ver las primeras 10 marcas de tiempo de las historias
SELECT timestamp
FROM hacker_news
LIMIT 10;

-- 9. Probar la función strftime para extraer la hora de la marca de tiempo
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

-- 10. Consultar la hora, el promedio de la puntuación y el conteo de historias por cada hora
SELECT strftime('%H', timestamp) AS hour,
   AVG(score) AS avg_score,
   COUNT(*) AS story_count
FROM hacker_news
GROUP BY 1;

-- 11. Editar la consulta para redondear las puntuaciones, renombrar las columnas y filtrar valores nulos
SELECT strftime('%H', timestamp) AS hour,
   ROUND(AVG(score), 2) AS avg_score,
   COUNT(*) AS story_count
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1;
