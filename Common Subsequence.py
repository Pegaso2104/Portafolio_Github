# 1. Declarar las cadenas de ADN
dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

# 2. Definir la función longest_common_subsequence
def longest_common_subsequence(string_1, string_2):
    print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
    
    # 3. Crear la grilla (tabla) de ceros
    grid = [[0 for _ in range(len(string_1) + 1)] for _ in range(len(string_2) + 1)]
    
    # 4. Iterar sobre las filas de la grilla
    for row in range(1, len(string_2) + 1):
        print("Comparing: {0}".format(string_2[row - 1]))  # Imprimir el carácter actual de string_2
        
        # 5. Iterar sobre las columnas de la grilla
        for col in range(1, len(string_1) + 1):
            print("Against: {0}".format(string_1[col - 1]))  # Imprimir el carácter actual de string_1
            
            # 6. Comparar los caracteres
            if string_1[col - 1] == string_2[row - 1]:
                # Si coinciden, tomamos el valor de la celda diagonal anterior + 1
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                # Si no coinciden, tomamos el valor máximo de la celda superior o la celda izquierda
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
    
    # 7. Imprimir la grilla completa para ver el proceso
    for row_line in grid:
        print(row_line)
    
    # La longitud de la subsecuencia común más larga está en la esquina inferior derecha de la grilla
    print(f"Length of LCS: {grid[-1][-1]}")
    
    # 8. Extraer la subsecuencia común más larga
    lcs = []
    row, col = len(string_2), len(string_1)
    
    while row > 0 and col > 0:
        if string_1[col - 1] == string_2[row - 1]:
            lcs.append(string_1[col - 1])  # Si coinciden, agregamos el carácter al resultado
            row -= 1
            col -= 1
        elif grid[row - 1][col] >= grid[row][col - 1]:
            row -= 1  # Si el valor superior es mayor, nos movemos arriba
        else:
            col -= 1  # Si el valor izquierdo es mayor, nos movemos a la izquierda
    
    # La subsecuencia se construye en orden inverso, por lo que la revertimos
    lcs.reverse()
    
    print(f"Longest Common Subsequence: {''.join(lcs)}")

# 9. Ejecutar la función
longest_common_subsequence(dna_1, dna_2)
