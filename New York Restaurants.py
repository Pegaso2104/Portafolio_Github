-- 1. Obtener todos los datos de la tabla  
SELECT * 
FROM nomnom;

-- 2. Obtener los barrios únicos (neighborhoods)  
SELECT DISTINCT neighborhood 
FROM nomnom;

-- 3. Obtener los tipos de cocina únicos (cuisine types)  
SELECT DISTINCT cuisine 
FROM nomnom;

-- 4. Encontrar opciones de comida china para llevar  
SELECT * 
FROM nomnom 
WHERE cuisine = 'Chinese';

-- 5. Restaurantes con calificaciones de 4 o más  
SELECT * 
FROM nomnom 
WHERE review >= 4;

-- 6. Restaurantes italianos con precios $$$  
SELECT * 
FROM nomnom 
WHERE cuisine = 'Italian' AND price = '$$$';

-- 7. Encontrar un restaurante que contenga ‘meatball’ en su nombre  
SELECT * 
FROM nomnom 
WHERE name LIKE '%meatball%';

-- 8. Restaurantes en Midtown, Downtown o Chinatown  
SELECT * 
FROM nomnom 
WHERE neighborhood = 'Midtown' 
   OR neighborhood = 'Downtown' 
   OR neighborhood = 'Chinatown';

-- 9. Restaurantes con calificación de salud pendiente (valores vacíos)  
SELECT * 
FROM nomnom 
WHERE health_grade IS NULL;

-- 10. Ranking de los 10 mejores restaurantes según las reseñas  
SELECT * 
FROM nomnom 
ORDER BY review DESC 
LIMIT 10;

-- 11. Usar CASE para cambiar la calificación del sistema de reseñas  
SELECT name, 
       review,
       CASE 
           WHEN review > 4.5 THEN 'Extraordinary'
           WHEN review > 4 THEN 'Excellent'
           WHEN review > 3 THEN 'Good'
           WHEN review > 2 THEN 'Fair'
           ELSE 'Poor'
       END AS rating_category
FROM nomnom;
