import random

dictionary = {

    "Tipos_de_datos": ["entero","lista","cadena"],
    "Elementos_basicos_de_programacion": ["variable","funcion"],
    "Palabras_mas_conocidas": ["python","programa"]

}

decision = 100
while  decision >=4 or decision <1: 

    print ("Ingrese un numero del 1 al 3 para seleccionar una categoria para jugar \n"
    "1)Tipos_de_datos \n"
    "2)Elementos_basicos_de_programacion \n"
    "3)Palabras_mas_conocidas")

    decision = int (input ("Su eleccion es: "))

if decision == 1:
    word = random.choice(dictionary.get("Tipos_de_datos",[]))
elif decision == 2 :
    word = random.choice(dictionary.get("Elementos_basicos_de_programacion",[]))
else:
    word = random.choice(dictionary.get("Palabras_mas_conocidas",[]))    

guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print(f"¡Ganaste!, tu puntaje es {score+6}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    if letter.isalpha () and len (letter)==1:                         
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            score -= 1
        print()
    else:
        print ("Entrada no valida\n")
        attempts -= 1 
        score -= 1    
else:
    print(f"¡Perdiste! La palabra era: {word}, tu puntaje es 0")