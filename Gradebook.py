last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Lista de asignaturas del semestre actual
subjects = ["physics", "calculus", "poetry", "history"]

# Lista de calificaciones del semestre actual
grades = [98, 97, 85, 88]

# 3. Crear una lista bidimensional que combine las asignaturas y las calificaciones
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# 4. Imprimir gradebook
print("Gradebook inicial:")
print(gradebook)

# 5. Agregar la clase de informática y la calificación 100
gradebook.append(["computer science", 100])

# 6. Agregar la clase de artes visuales y la calificación 93
gradebook.append(["visual arts", 93])

# 7. Modificar la calificación de la clase de artes visuales (agregar 5 puntos)
gradebook[-1][1] += 5  # 5 puntos extra

# 8. Eliminar la calificación de la clase de poesía
for subject in gradebook:
    if subject[0] == "poetry":
        gradebook.remove(subject)
        break

# 9. Agregar un valor "Pass" a la clase de poesía
gradebook.append(["poetry", "Pass"])

# 10. Combinar las calificaciones del semestre pasado con el libro de calificaciones actual
full_gradebook = last_semester_gradebook + gradebook

# Imprimir el libro de calificaciones completo
print("\nFull gradebook:")
print(full_gradebook)
