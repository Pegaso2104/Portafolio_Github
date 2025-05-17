 -- Crear la función para registrar cambios en la tabla customers_log
CREATE OR REPLACE FUNCTION log_customers_change() 
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO customers_log (customer_id, change_time, changed_column, old_value, new_value)
    VALUES (NEW.customer_id, CURRENT_TIMESTAMP, 'first_name', OLD.first_name, NEW.first_name);
    INSERT INTO customers_log (customer_id, change_time, changed_column, old_value, new_value)
    VALUES (NEW.customer_id, CURRENT_TIMESTAMP, 'last_name', OLD.last_name, NEW.last_name);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear el trigger para registrar actualizaciones en first_name o last_name
CREATE TRIGGER customer_update
    BEFORE UPDATE ON customers
    FOR EACH ROW
    WHEN (NEW.first_name IS DISTINCT FROM OLD.first_name OR NEW.last_name IS DISTINCT FROM OLD.last_name)
    EXECUTE PROCEDURE log_customers_change();
-- Crear el trigger para registrar una sola entrada de log por inserciones masivas
CREATE TRIGGER customer_insert
    AFTER INSERT ON customers
    FOR EACH STATEMENT
    EXECUTE PROCEDURE log_customers_change();
-- Función para asegurar que la edad no sea menor a 13
CREATE OR REPLACE FUNCTION override_with_min_age() 
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.age < 13 THEN
        NEW.age := 13;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
-- Crear el trigger para aplicar la validación de edad
CREATE TRIGGER customer_min_age
    BEFORE UPDATE ON customers
    FOR EACH ROW
    WHEN (NEW.age < 13)
    EXECUTE PROCEDURE override_with_min_age();
-- Eliminar el trigger que valida la edad mínima
DROP TRIGGER IF EXISTS customer_min_age ON customers;
-- Verificar la lista de triggers existentes
SELECT * FROM information_schema.triggers;
UPDATE customers
SET first_name = 'NuevoNombre'
WHERE customer_id = 1;

-- Verificar que se haya registrado el cambio en la tabla de logs
SELECT * FROM customers_log;
INSERT INTO customers (first_name, last_name, email, phone, city, state, age)
VALUES 
('Jeffrey', 'Cook', 'jeffrey.cook@example.com', '202-555-0398', 'Jersey City', 'New Jersey', 66),
('Sara', 'Smith', 'sara.smith@example.com', '202-555-0498', 'Hoboken', 'New Jersey', 34),
('Juan', 'Perez', 'juan.perez@example.com', '202-555-0399', 'Miami', 'Florida', 22);

-- Verificar que solo se haya insertado un registro en customers_log por el conjunto de inserciones
SELECT * FROM customers_log;
UPDATE customers
SET age = 12
WHERE customer_id = 1;

-- Verificar que la edad se haya corregido a 13
SELECT * FROM customers WHERE customer_id = 1;
