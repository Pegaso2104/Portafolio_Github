# Your code below:

# Tarea 1: Crear la lista de toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Tarea 2: Crear la lista de precios
prices = [2, 6, 1, 3, 2, 7, 2]

# Tarea 3: Contar las ocurrencias de 2 en prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Tarea 4: Obtener la longitud de toppings
num_pizzas = len(toppings)

# Tarea 5: Imprimir la cantidad de pizzas
print(f"We sell {num_pizzas} different kinds of pizza!")

# Tarea 6: Crear la lista bidimensional pizza_and_prices
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Tarea 7: Imprimir pizza_and_prices
print(pizza_and_prices)

# Tarea 8: Ordenar pizza_and_prices por precio
pizza_and_prices.sort()

# Tarea 9: Almacenar la pizza más barata
cheapest_pizza = pizza_and_prices[0]

# Tarea 10: Almacenar la pizza más cara
priciest_pizza = pizza_and_prices[-1]

# Tarea 11: Eliminar la pizza más cara
pizza_and_prices.pop()

# Tarea 12: Agregar "peppers" y ordenar
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()

# Tarea 13: Obtener las tres pizzas más baratas
three_cheapest = pizza_and_prices[:3]

# Tarea 14: Imprimir las tres pizzas más baratas
print(three_cheapest)
