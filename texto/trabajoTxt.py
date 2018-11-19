# contar la cantidad de 'principito' que aparecen en el txt y crear un nuevo archivo txt con 
# palabras del principito cambiadas en el
import timeit

#comenzamos a medir el tiempo
inicio = timeit.default_timer()

#contador de palabras
cont = 0
# nuevo archivo de texto
yondercito = open("./texto/yondercito.txt", "w")

# abrimos el archivo de texto en modo lectura, lo leemos y guardamos su contenido en la variable libro
libro = open('./texto/principito.txt', 'r').read()
# obtenemos una lista de las palabras que hay en el libro
palabras = libro.split(" ")

#contamos cuantos principitos hay en el libro y lo reemplazamos en el nuevo libro por yondercito
for palabra in palabras:
    if (palabra == 'principito'):
        palabra = 'Yondercito'
        cont += 1
    yondercito.write(palabra + " ")

# cerramos el archivo que creamos
yondercito.close()

# mostramos la cantidad de palabras encontradas
print("La cantidad de veces que aparece la palabra 'principito' en el libro es: " + str(cont))

#terminamos de medir el tiempo
fin = timeit.default_timer()
print('El tiempo de las operaciones fue de: ', fin - inicio)  