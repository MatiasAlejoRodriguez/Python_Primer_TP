import random

def show_progress (progress,word):
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    return (progress)

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
    print ("\n")

if decision == 1:
    word = random.choice(dictionary.get("Tipos_de_datos",[]))
    amount_of_words = len (dictionary["Tipos_de_datos"])
    category_words = random.sample (dictionary ["Tipos_de_datos"],3)
    
elif decision == 2 :
    word = random.choice(dictionary.get("Elementos_basicos_de_programacion",[]))
    amount_of_words = len (dictionary["Elementos_basicos_de_programacion"])
    category_words = random.sample (dictionary ["Elementos_basicos_de_programacion"],2)
    
else:
    word = random.choice(dictionary.get("Palabras_mas_conocidas",[]))
    amount_of_words = len (dictionary["Palabras_mas_conocidas"])    
    category_words = random.sample (dictionary ["Palabras_mas_conocidas"],2)

guessed = []
attempts = 6
score = 0
progress = ""

print("¡Bienvenido al Ahorcado! \n")

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = show_progress (progress,word)
    
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score += 6
        print(f"¡Adivinaste la palabra!, tu puntaje actual es {score}")
        amount_of_words -= 1
        category_words.remove (word)
        if amount_of_words == 0:
            print (f'Ganaste el juego!, tu puntuje final es {score}')
            break
        else:
            guessed = []
            word = random.choice (category_words)
            progress = show_progress (progress,word)
            print ("Ahora tendra que adivinar otra palabra de la categoria que eligio")

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input ("Ingresá una letra: ").lower()

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