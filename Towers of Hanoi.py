from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Crear las pilas
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# Agregar las pilas a la lista de stacks
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Configurar el juego
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# Asegurarse de que el número de discos sea al menos 3
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Agregar los discos a la pila izquierda
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# Calcular el número de movimientos óptimos
num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

# Obtener la entrada del usuario (Elegir una pila)
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]  # Primera letra de cada nombre
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}")
        
        user_input = input()
        
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# Jugar el juego
num_user_moves = 0
while right_stack.get_size() != num_disks:
    # Mostrar las pilas actuales
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()

    # Obtener las pilas de origen y destino
    from_stack = None
    to_stack = None
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        
        # Comprobar si el movimiento es válido
        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try Again")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")
    
# Finalizar el juego
print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
