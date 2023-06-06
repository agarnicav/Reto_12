
## Cantidad de vocales

def Contar_cantidad_vocales(text: str) -> int: # Se define l
    # Lista de vocales en minúsculas y mayúsculas
    Lista_Vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    Numero_vocales = 0  # Variable para almacenar la cantidad de vocales
    
    for vocal in text:
        if vocal in Lista_Vocales:  # Verificar si el carácter actual es una vocal
            Numero_vocales += 1  # Incrementar el contador de vocales en 1
    
    return Numero_vocales
       

if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        texto = file.read()
        Cantidad = Contar_cantidad_vocales(texto) 
        print("La cantidad de vocales que se encuentran en el texto es " + str(Cantidad))

