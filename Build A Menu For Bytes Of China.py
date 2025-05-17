-- Script para crear las tablas y relaciones

-- 1. Tabla restaurant
CREATE TABLE restaurant (
    restaurant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    phone VARCHAR(20),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES address(address_id)
);

-- 2. Tabla address
CREATE TABLE address (
    address_id INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(10)
);

-- 3. Tabla category
CREATE TABLE category (
    category_id CHAR(2) PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

-- 4. Tabla dish
CREATE TABLE dish (
    dish_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    description TEXT,
    is_spicy BOOLEAN
);

-- 5. Tabla review
CREATE TABLE review (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(2, 1),
    description TEXT,
    review_date DATE
);

-- 6. Tabla categories_dishes (para la relación muchos a muchos entre category y dish)
CREATE TABLE categories_dishes (
    category_id CHAR(2),
    dish_id INT,
    price DECIMAL(10, 2),
    PRIMARY KEY (category_id, dish_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (dish_id) REFERENCES dish(dish_id)
);

-- Consultas para validar las claves primarias

-- 7. Validar la clave primaria de la tabla restaurant
SELECT * FROM information_schema.columns
WHERE table_name = 'restaurant' AND column_key = 'PRI';

-- 8. Validar la clave primaria de la tabla address
SELECT * FROM information_schema.columns
WHERE table_name = 'address' AND column_key = 'PRI';

-- 9. Validar la clave primaria de la tabla category
SELECT * FROM information_schema.columns
WHERE table_name = 'category' AND column_key = 'PRI';

-- 10. Validar la clave primaria de la tabla dish
SELECT * FROM information_schema.columns
WHERE table_name = 'dish' AND column_key = 'PRI';

-- 11. Validar la clave primaria de la tabla review
SELECT * FROM information_schema.columns
WHERE table_name = 'review' AND column_key = 'PRI';

-- 12. Validar la clave primaria de la tabla categories_dishes
SELECT * FROM information_schema.columns
WHERE table_name = 'categories_dishes' AND column_key = 'PRI';

-- 13. Relación uno a uno entre restaurant y address
-- Ya implementada al agregar address_id como clave foránea en restaurant

-- 14. Relación uno a muchos entre category y categories_dishes
-- Ya implementada por la relación en la tabla categories_dishes

-- 15. Relación muchos a muchos entre category y dish
-- Ya implementada por la tabla categories_dishes

-- Insertar datos de muestra en las tablas

-- Insertar en address
INSERT INTO address (street, city, state, zip_code)
VALUES ('2020 Busy Street', 'Chinatown', 'MA', '02139');

-- Insertar en restaurant
INSERT INTO restaurant (name, phone, address_id)
VALUES ('Bytes of China', '617-555-1212', 1);

-- Insertar en category
INSERT INTO category (category_id, name, description)
VALUES
('A', 'Appetizers', NULL),
('C', 'Chicken', NULL),
('HS', 'House Specials', NULL),
('LS', 'Luncheon Specials', 'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice between 11:00 am and 3:00 pm from Monday to Friday.'),
('B', 'Beef', NULL);

-- Insertar en dish
INSERT INTO dish (name, price, description, is_spicy)
VALUES
('Spring Rolls', 4.95, 'Crispy spring rolls with a vegetable filling', FALSE),
('Hot and Sour Soup', 3.50, 'Spicy and sour broth with tofu and vegetables', TRUE),
('Chicken with Broccoli', 6.95, 'Tender chicken with broccoli in a savory sauce', FALSE);

-- Insertar en categories_dishes
INSERT INTO categories_dishes (category_id, dish_id, price)
VALUES
('A', 1, 4.95),
('C', 3, 6.95),
('LS', 3, 8.95);

-- Insertar en review
INSERT INTO review (rating, description, review_date)
VALUES
(5.0, 'Awesome service. Would love to host another birthday party at Bytes of China!', '2020-05-22'),
(4.5, 'Other than a small mix-up, I would give it a 5.0!', '2020-04-01'),
(3.9, 'A reasonable place to eat for lunch, if you are in a rush!', '2020-03-15');

-- Consultas

-- 1. Mostrar nombre del restaurante, dirección y teléfono
SELECT r.name, a.street, a.city, a.state, a.zip_code, r.phone
FROM restaurant r
JOIN address a ON r.address_id = a.address_id;

-- 2. Obtener la mejor calificación del restaurante
SELECT MAX(rating) AS best_rating FROM review;

-- 3. Mostrar nombre del plato, precio y categoría
SELECT d.name AS dish_name, cd.price, c.name AS category
FROM dish d
JOIN categories_dishes cd ON d.dish_id = cd.dish_id
JOIN category c ON cd.category_id = c.category_id
ORDER BY d.name;

-- 4. Mostrar nombre del plato, precio y categoría ordenados por categoría
SELECT c.name AS category, d.name AS dish_name, cd.price
FROM dish d
JOIN categories_dishes cd ON d.dish_id = cd.dish_id
JOIN category c ON cd.category_id = c.category_id
ORDER BY c.name;

-- 5. Mostrar los platos picantes con su precio y categoría
SELECT d.name AS spicy_dish_name, c.name AS category, cd.price
FROM dish d
JOIN categories_dishes cd ON d.dish_id = cd.dish_id
JOIN category c ON cd.category_id = c.category_id
WHERE d.is_spicy = TRUE;

-- 6. Mostrar el dish_id y el número de veces que un plato aparece en diferentes categorías
SELECT cd.dish_id, COUNT(cd.dish_id) AS dish_count
FROM categories_dishes cd
GROUP BY cd.dish_id;

-- 7. Mostrar solo los platos que aparecen más de una vez
SELECT cd.dish_id, COUNT(cd.dish_id) AS dish_count
FROM categories_dishes cd
GROUP BY cd.dish_id
HAVING COUNT(cd.dish_id) > 1;

-- 8. Mostrar los platos que aparecen más de una vez, con su nombre
SELECT d.name AS dish_name, COUNT(cd.dish_id) AS dish_count
FROM categories_dishes cd
JOIN dish d ON cd.dish_id = d.dish_id
GROUP BY cd.dish_id
HAVING COUNT(cd.dish_id) > 1;

-- 9. Mostrar la mejor calificación con su descripción
SELECT r.rating AS best_rating, r.description
FROM review r
WHERE r.rating = (SELECT MAX(rating) FROM review);
