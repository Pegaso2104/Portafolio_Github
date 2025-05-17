import random

# Declarar las variables
name = "Joe"  # Cambia esto por el nombre que desees
question = "Will I win the lottery?"  # Cambia esto por tu pregunta
answer = ""  # Inicializamos como una cadena vacía

# Generar un número aleatorio entre 1 y 9
random_number = random.randint(1, 9)

# Asignar respuestas basadas en el número aleatorio
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Manejo de casos cuando el nombre o la pregunta están vacíos
if name.strip() == "" and question.strip() == "":
    print("Please provide your name and question.")
elif name.strip() == "":
    print(f"Question: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
elif question.strip() == "":
    print(f"{name} did not ask a question. Please provide a valid question.")
else:
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")
