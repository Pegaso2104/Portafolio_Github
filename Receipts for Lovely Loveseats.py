# Descripciones de los muebles
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

# Impuesto sobre las ventas
sales_tax = 0.088

# Registro de la compra del primer cliente
customer_one_total = 0
customer_one_itemization = ""

# El cliente compra el Loveseat Lovely
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# El cliente compra la Lámpara de Lujo
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calcular el impuesto sobre las ventas
customer_one_tax = customer_one_total * sales_tax

# Agregar el impuesto al total
customer_one_total += customer_one_tax

# Imprimir el encabezado de los artículos comprados
print("Customer One Items:")
print(customer_one_itemization)

# Imprimir el encabezado del total
print("Customer One Total:")
print(f"{customer_one_total:.2f}")  # Usamos .2f para formatear el total con dos decimales
