# Listas de datos proporcionadas
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Calcular el precio promedio de un corte
total_price = 0
for price in prices:
    total_price += price  # Sumamos cada precio
average_price = total_price / len(prices)  # Calculamos el promedio
print(f"Average Haircut Price: {average_price}")  # Imprimimos el precio promedio

# 2. Crear una nueva lista con los precios reducidos en 5 dólares
new_prices = [price - 5 for price in prices]  # Lista de comprensión para reducir los precios
print(new_prices)  # Imprimimos la nueva lista de precios

# 3. Calcular los ingresos totales de la última semana
total_revenue = 0
for i in range(len(hairstyles)):  # Usamos range(len(hairstyles)) para iterar por los índices
    total_revenue += prices[i] * last_week[i]  # Calculamos la ganancia por cada corte
print(f"Total Revenue: {total_revenue}")  # Imprimimos el total de ingresos

# 4. Calcular el ingreso diario promedio
average_daily_revenue = total_revenue / 7  # Calculamos el promedio diario
print(average_daily_revenue)  # Imprimimos el ingreso diario promedio

# 5. Crear una lista de cortes de pelo cuyo precio sea menor que 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]  # Lista de cortes con precios menores a 30
print(cuts_under_30)  # Imprimimos los cortes de pelo bajo 30

