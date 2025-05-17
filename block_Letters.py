def print_initial_c():
    width = 5
    height = 7
    letter_c = []

    # Crear la letra C en un bloque de 7x5
    for row in range(height):
        line = ''
        for col in range(width):
            if col == 0 or (row == 0 or row == height - 1) and col < width - 1:
                line += '#'  # Forma la letra "C"
            else:
                line += ' '  # Relleno con espacio
        letter_c.append(line)

    # Imprimir la letra C
    for line in letter_c:
        print(line)

print_initial_c()


