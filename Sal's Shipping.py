# Sal's Shippers

# Manejo de entrada del usuario con un valor predeterminado en caso de error
try:
    weight = float(input("Ingrese el peso del paquete en libras: "))
except EOFError:
    print("No se ingresó peso. Usando un peso predeterminado de 4.8 libras.")
    weight = 4.8
except ValueError:
    print("Entrada inválida. Usando un peso predeterminado de 4.8 libras.")
    weight = 4.8

# Envío terrestre
# ----------------
ground_flat_rate = 20.00
if weight <= 2:
    ground_cost = weight * 1.50 + ground_flat_rate
elif weight <= 6:
    ground_cost = weight * 3.00 + ground_flat_rate
elif weight <= 10:
    ground_cost = weight * 4.00 + ground_flat_rate
else:
    ground_cost = weight * 4.75 + ground_flat_rate

# Envío terrestre premium
# -------------------------
premium_ground_cost = 125.00

# Envío con drones
# -----------------
if weight <= 2:
    drone_cost = weight * 4.50
elif weight <= 6:
    drone_cost = weight * 9.00
elif weight <= 10:
    drone_cost = weight * 12.00
else:
    drone_cost = weight * 14.25

# Mostrar los costos
print(f"\nCostos de envío para un paquete de {weight} libras:")
print(f"Envío terrestre: ${ground_cost:.2f}")
print(f"Envío terrestre premium: ${premium_ground_cost:.2f}")
print(f"Envío con drones: ${drone_cost:.2f}")

# Determinar el método más barato
if ground_cost < premium_ground_cost and ground_cost < drone_cost:
    cheapest_method = "Envío terrestre"
    cheapest_cost = ground_cost
elif premium_ground_cost < ground_cost and premium_ground_cost < drone_cost:
    cheapest_method = "Envío terrestre premium"
    cheapest_cost = premium_ground_cost
else:
    cheapest_method = "Envío con drones"
    cheapest_cost = drone_cost

# Mostrar el método más económico
print(f"\nEl método más barato es: {cheapest_method} (${cheapest_cost:.2f})")

