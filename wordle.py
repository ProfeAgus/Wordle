"""
Pautas con los puntajes

- guardar la informacion del archivo palabras.txt en la lista words y agregar 10 palabras al archivo (3)
- No debe permitir que se ingrese adivinanzas que tengan letras de más o de menos, SIN QUE SE CORTE EL JUEGO (2)
- El jugador debe ver todo en español y que haya por lo menos una palabra más que tenga color (1)
- que el acumulador de cuantos intentos incremente despues de cada adivinanza (1)   
- cuando termine el juego, que muestre la palabra adivinada (2)    
- que avise cuantas letras tiene la palabra durante el juego o cambiar el subrayado del input del jugador por otro estilo* (1)

--------------------------------------------------
tips para proyectos de programación y para la vida:
--------------------------------------------------
Empiecen por las cosas que si entienden.
El que mucho abraza, poco aprieta.
No te ahogues en un vaso de agua.
Si google no tiene la respuesta, capaz que chatgpt.

 * para entender el tema de los colores y estilos de las letras en la consola lean el siguiente articulo:
 https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html

Entrega: 30 de julio, por classroom, con nombre de integrantes del grupo y que me aclaren cuales son las palabras 
         que elijieron que tienen color
"""

import os, time, random

clear = ""
if os.name == "nt":
    clear = "cls"
else:
    clear = "clear"

words = ["perro","gasto","gatos","leche","termo"]


###
### Aca se debe leer el archivo palabras.txt 
### mientras lo va leyendo, debe ir guardando las palabras en la lista words
###

word = words[random.randint(0, len(words)-1)] # elije la palabra aleatoriamente
hints = [" _ " for i in range(len(word))]
old_hints = []
is_over = False
count = 0

# mientras no se acaba
while not is_over:
    # Logica epica del juego
    
    os.system(clear) # borra todo en consola
    print(f"Guess the word \nGuesses: {count}")
    for i, h in enumerate(old_hints):
        if i % len(word) == len(word)-1 and i > 0:
            print(h)
        else:
            print(h, end="")
    
    print(f"\nTu ultima adivinanza fue ", end="")
    for h in hints:
        print(h, end="")
    print()
    hints = [" _ " for i in range(len(word))]
    guess = input("Adivina la palabra: \033[4;94m")
    print("\033[0m")
    
    # por aca deberia saltar el error si tiene letras de mas o menos, pista: usar palabra clave continue

    if guess.lower() == word:
        is_over = True
        continue

    # colorea letras de acuerdo a 
    for i, l in enumerate(guess):        
        if l in word:
            if word[i] == guess[i]:
                hints[i] = " \033[92m"+l.upper()+"\033[0m "
            else:
                hints[i] = " \033[93m"+l.lower()+"\033[0m " 
        else:
            hints[i] = " \033[91m"+l.lower()+"\033[0m "
        old_hints.append(hints[i])
    
    
print(f"La palabra era: (mostrar palabra) GOOD JOB !!, te llevó {count} adivinanzas ")
