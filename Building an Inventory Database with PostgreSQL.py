SELECT * FROM parts LIMIT 10;
ALTER TABLE parts
ADD CONSTRAINT unique_code UNIQUE (code);

ALTER TABLE parts
ALTER COLUMN code SET NOT NULL;
UPDATE parts
SET description = 'No description provided'
WHERE description IS NULL;
ALTER TABLE parts
ALTER COLUMN description SET NOT NULL;
-- Intentar insertar con description vacío
INSERT INTO parts (id, description, code, manufacturer_id) 
VALUES (54, '', 'V1-009', 9);  -- Esto debería fallar debido a la restricción NOT NULL en description.

-- Insertar con description válido
INSERT INTO parts (id, description, code, manufacturer_id) 
VALUES (54, 'Part description', 'V1-009', 9);  -- Esta inserción debería funcionar.
ALTER TABLE reorder_options
ALTER COLUMN price_usd SET NOT NULL;

ALTER TABLE reorder_options
ALTER COLUMN quantity SET NOT NULL;
ALTER TABLE reorder_options
ADD CONSTRAINT price_positive CHECK (price_usd > 0);

ALTER TABLE reorder_options
ADD CONSTRAINT quantity_positive CHECK (quantity > 0);
ALTER TABLE reorder_options
ADD CONSTRAINT price_and_quantity_positive CHECK (price_usd > 0 AND quantity > 0);
