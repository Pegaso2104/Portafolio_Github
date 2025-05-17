-- 1. Examinar las tres tablas
SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;

-- 2. Encontrar las claves primarias de las tablas
-- Para la tabla trips:
SELECT * FROM trips LIMIT 1;

-- Para la tabla riders:
SELECT * FROM riders LIMIT 1;

-- Para la tabla cars:
SELECT * FROM cars LIMIT 1;

-- 3. Intentar un simple CROSS JOIN entre riders y cars
SELECT * FROM riders
CROSS JOIN cars;

-- 4. Crear un Trip Log con la combinación de trips y riders usando LEFT JOIN
SELECT *
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- 5. Crear un link entre trips y cars usando INNER JOIN
SELECT *
FROM trips
INNER JOIN cars
  ON trips.car_id = cars.id;

-- 6. Apilar la tabla riders con la nueva tabla riders2
SELECT * FROM riders
UNION
SELECT * FROM riders2;

-- Bonus: Consultas y agregados

-- 7. Encontrar el costo promedio de un trip
SELECT AVG(cost) AS avg_cost FROM trips;

-- 8. Encontrar los riders que han usado Lyft menos de 500 veces
SELECT * FROM riders
WHERE trips_taken < 500;

-- 9. Calcular el número de autos activos
SELECT COUNT(*) AS active_cars
FROM cars
WHERE active = TRUE;

-- 10. Encontrar los dos autos con más trips_completed
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
