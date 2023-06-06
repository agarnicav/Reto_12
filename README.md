# Reto_12

## Primer punto 

Hallar la cantidad de vocales

### Codigo 

    
    def Contar_cantidad_vocales(text: str) -> int: # Se define la función para contar vocales 
    # Se crea una lista de vocales en minúsculas y mayúsculas
        Lista_Vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
        Numero_vocales = 0  # Variable para almacenar la cantidad de vocales
    
        for vocal in text:
            if vocal in Lista_Vocales:  # Verificar si el carácter actual es una vocal
                Numero_vocales += 1  # Incrementar el contador de vocales en 1
    
        return Numero_vocales
       

    if __name__ == "__main__":
        with open("mbox-short.txt", "r") as file:
            texto = file.read() # Leer el contenido del archivo en la variable 'texto'
            Cantidad = Contar_cantidad_vocales(texto) 
            print("La cantidad de vocales que se encuentran en el texto es " + str(Cantidad))
            
## Segundo punto 

Hallar la cantidad de consonantes 

### Codigo

    def Contar_cantidad_Consonantes(text: str) -> int:  # Se define la función para contar consonantes 
    
      # Lista de consonantes en minúsculas y mayúsculas
        Lista_Consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    
     Numero_Consonantes = 0  # Variable para almacenar la cantidad de consonantes
    
        for consonante in text:
            if consonante in Lista_Consonantes:  # Verificar si el carácter actual es una consonante
                Numero_Consonantes += 1  # Incrementar el contador de consonantes en 1
    
        return Numero_Consonantes

    if __name__ == "__main__":
        with open("mbox-short.txt", "r") as file:
            texto = file.read() texto = file.read() # Leer el contenido del archivo en la variable 'texto'
            Cantidad = Contar_cantidad_Consonantes(texto) 
            print("La cantidad de consonantes que se encuentran en el texto es: " + str(Cantidad))
            
## Tercer punto

Listado de las 50 palabras que más se repiten

### Codigo 

    def Contar_cantidad_palabras_repetidas(text: str) -> int: # Se define la función para dar el listado de las 50 palabras que mas se repiten
        Lista_signos = [".", ",", ":", ";", "_", "-", " "]  # Lista de signos de puntuación y espacios para filtrar las palabras
    
        palabras = text.split()  # Dividir el texto en palabras
    
        # Filtrar y limpiar las palabras
        for i in range(len(palabras)):
            if not palabras[i].isalpha():  # Verificar si la palabra contiene caracteres no alfabéticos
                palabra = palabras[i].strip("".join(Lista_signos))  # Eliminar los signos de puntuación al principio y al final de la palabra
                palabras.pop(i)  # Eliminar la palabra original
                palabras.insert(i, palabra)  # Insertar la palabra filtrada
            
    # Eliminar palabras no alfabéticas adicionales
        for palabra in palabras: 
            if not palabra.isalpha():
                palabras.remove(palabra)
        
        Palabras_repetidas = {}  # Diccionario para almacenar las palabras repetidas y su frecuencia
    
        # Contar la frecuencia de las palabras
        for palabra in palabras:
            if palabra in Palabras_repetidas:
                Palabras_repetidas[palabra] += 1
            else:
                Palabras_repetidas[palabra] = 1

        # Obtener las palabras con mayor frecuencia
        Palabras_lista = [list(Palabras_repetidas.items())[i][::-1] for i in range(len(Palabras_repetidas))]
        frecuencia_Palabras = sorted(Palabras_lista, reverse=True)[:50]

        # Imprimir las palabras con su frecuencia
        for palabra, frecuencia in frecuencia_Palabras:
            print("La palabra '" + palabra + "' se repite " + str(frecuencia) + " veces")

        return len(frecuencia_Palabras)


    if __name__ == "__main__":
        with open("mbox-short.txt", "r") as file:
            texto = file.read() # Leer el contenido del archivo en la variable 'texto'
            Cantidad = Contar_cantidad_palabras_repetidas(texto)  # Llamar a la función 'Contar_cantidad_palabras_repetidas' y pasarle el texto como argumento
            
            
## Cuarto Punto 

Listado de destinatarios con cantidad de mensajes recibidos

    def Cantidadd_Mensajes_Recibidos(text: str) -> dict:  # Se define la función para encontrar la cantidad de mensajes recibidos por cada destinatario
        palabras = text.split()  # Dividir el texto en palabras
        mensajes_recibidos = {}  # Diccionario para almacenar la cantidad de mensajes recibidos por cada usuario

        for i in range(len(palabras)):
            # Verificar si la palabra actual es "by" o "BY" y si la palabra anterior contiene un punto
            if (palabras[i] == "by" or palabras[i] == "BY") and "." in palabras[i-1]:
                correo = palabras[i+1]  # Obtener el correo electrónico del remitente
                if correo in mensajes_recibidos:
                    mensajes_recibidos[correo] += 1  # Incrementar la cantidad de mensajes recibidos para ese correo
                else:
                    mensajes_recibidos[correo] = 1  # Agregar el correo al diccionario con una cantidad de mensajes inicial de 1

        return mensajes_recibidos


    if __name__ == "__main__":
        with open("mbox-short.txt", "r") as file:
            texto = file.read()  # Leer el contenido del archivo en la variable 'texto'
            cantidad = Cantidadd_Mensajes_Recibidos(texto)  # Llamar a la función 'Cantidadd_Mensajes_Recibidos' y pasarle el texto como argumento

            # Imprimir la cantidad de mensajes recibidos por cada usuario
            for correo, mensajes in cantidad.items():
                print("El usuario " + correo + " recibió " + str(mensajes) + " mensajes.")

            
            
# Quinto Punto 

Cantidad de mensajes enviados por cada día

### Codigo

    def cantidad_mensajes_por_dia(text: str) -> dict: # Se define la función para encontrar la cantidad de mensaajes enviados por día
        mensajes_recibidos = []  # Lista para almacenar los segmentos de mensajes recibidos
        palabras = text.split()  # Dividir el texto en palabras

        i = 0
        while i < len(palabras):
            if palabras[i] == "Received:":  # Verificar si la palabra actual es "Received:"
                segmento = []
                while i < len(palabras) and palabras[i] != "-0500" and palabras[i + 1] != "(GMT)": i < len(palabras): # Se verifica que el índice i sea menor que la longitud de la lista palabras y se omprueba que la palabra en la posición i de la lista palabras no sea igual a "-0500" se Verifica que la siguiente palabra después de palabras[i] no sea igual a "(GMT)".


                    segmento.append(palabras[i + 1])  # Agregar las palabras siguientes al segmento
                    i += 1
                mensajes_recibidos.append(segmento)  # Agregar el segmento de mensajes a la lista
            i += 1

        mensajes_dia = {}  # Diccionario para almacenar la cantidad de mensajes por día

        for mensaje in mensajes_recibidos:
            indice = mensaje.index("Jan")  # Encontrar el índice de la palabra "Jan" que indica el mes
            dia = mensaje[indice - 1]  # Obtener el día anterior al mes

            if dia in mensajes_dia:
                mensajes_dia[dia] += 1  # Incrementar la cantidad de mensajes para ese día
            else:
                mensajes_dia[dia] = 1  # Agregar el día al diccionario con una cantidad de mensajes inicial de 1

       return mensajes_dia


    if __name__ == "__main__":
        with open("mbox-short.txt", "r") as file:
           texto = file.read()  # Leer el contenido del archivo en la variable 'texto'
            cantidad = cantidad_mensajes_por_dia(texto)  # Llamar a la función 'cantidad_mensajes_por_dia' y pasarle el texto como argumento
        
            dias_totales = {}  # Diccionario para almacenar la cantidad total de mensajes por día

            for dia, cantidad_mensajes in cantidad.items():
               dia = dia.lstrip("0")  # Eliminar el cero inicial en caso de días de un solo dígito

                if dia in dias_totales:
                    dias_totales[dia] += cantidad_mensajes  # Incrementar la cantidad de mensajes para ese día
                else:
                    dias_totales[dia] = cantidad_mensajes  # Agregar el día al diccionario con una cantidad de mensajes inicial

            for dia, cantidad_mensajes in dias_totales.items():
                print("El día " + dia + " se enviaron " + str(cantidad_mensajes) + " mensajes")  # Imprimir la cantidad de mensajes por día


## Consulta 
Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

endswith(suffix): Verifica si la cadena termina con el sufijo especificado. Retorna True si es así, y False en caso contrario.

startswith(prefix): Verifica si la cadena comienza con el prefijo especificado. Retorna True si es así, y False en caso contrario.

isalpha(): Verifica si todos los caracteres de la cadena son letras (alfabéticos). Retorna True si todos son letras, y False si hay al menos un carácter que no es una letra.

isalnum(): Verifica si todos los caracteres de la cadena son alfanuméricos (letras o dígitos). Retorna True si todos son alfanuméricos, y False si hay al menos un carácter que no es alfanumérico.

isdigit(): Verifica si todos los caracteres de la cadena son dígitos numéricos. Retorna True si todos son dígitos, y False si hay al menos un carácter que no es un dígito.

isspace(): Verifica si todos los caracteres de la cadena son espacios en blanco. Retorna True si todos son espacios en blanco, y False si hay al menos un carácter que no es un espacio en blanco.

istitle(): Verifica si la cadena está en formato de título, es decir, si todas las palabras tienen la primera letra en mayúscula y el resto en minúscula. Retorna True si está en formato de título, y False en caso contrario.

islower(): Verifica si todos los caracteres de la cadena están en minúscula. Retorna True si todos son minúsculas, y False si hay al menos un carácter que no es minúscula.

isupper(): Verifica si todos los caracteres de la cadena están en mayúscula. Retorna True si todos son mayúsculas, y False si hay al menos un carácter que no es mayúscula.




 
