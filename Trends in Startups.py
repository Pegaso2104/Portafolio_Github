-- 1. Ver toda la tabla
SELECT *
FROM startups;

-- 2. Calcular el número total de empresas en la tabla
SELECT COUNT(*) 
FROM startups;

-- 3. Calcular el valor total de todas las empresas
SELECT SUM(valuation)
FROM startups;

-- 4. ¿Cuál es la mayor cantidad de dinero recaudada por una startup?
SELECT MAX(amount_raised)
FROM startups;

-- 5. Máxima cantidad de dinero recaudada durante la etapa 'Seed'
SELECT MAX(amount_raised)
FROM startups
WHERE stage = 'Seed';

-- 6. ¿En qué año se fundó la empresa más antigua?
SELECT MIN(founded_year)
FROM startups;

-- 7. Retornar la valoración promedio
SELECT AVG(valuation)
FROM startups;

-- 8. Retornar la valoración promedio por categoría
SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

-- 9. Retornar la valoración promedio por categoría, redondeada a dos decimales
SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category;

-- 10. Retornar la valoración promedio por categoría, redondeada a dos decimales, ordenada de mayor a menor
SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category
ORDER BY AVG(valuation) DESC;

-- 11. Retornar el nombre de cada categoría con el número total de empresas que pertenecen a ella
SELECT category, COUNT(*)
FROM startups
GROUP BY category;

-- 12. Filtrar para incluir solo categorías con más de tres empresas
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3;

-- 13. ¿Cuál es el tamaño promedio de una startup en cada ubicación?
SELECT location, AVG(size)
FROM startups
GROUP BY location;

-- 14. ¿Cuál es el tamaño promedio de una startup en cada ubicación, con tamaños promedio superiores a 500?
SELECT location, AVG(size)
FROM startups
GROUP BY location
HAVING AVG(size) > 500;
