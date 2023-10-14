def calcular_promedio(lista):
    suma = 0
    for indice in range(1, len(lista)):
        suma += lista[indice]
    return suma / (len(lista) - 1)

def obtener_calificaciones(materias):
    alumno = input("Escribe el nombre del alumno: ")
    lista = [alumno]
    for nombre in materias:
        calificaciones = float(input(f"Escribe la calificación de {nombre}: "))
        lista.append(calificaciones)
    return lista

def main():
    repetir = input("¿Quieres calcular el promedio de las materias? (s/n): ")
    materias = ["matematicas", "espanol"]
    lista_alumnos = []

    while repetir == "s":
        lista = obtener_calificaciones(materias)
        promedio = calcular_promedio(lista)
        lista_alumnos.append(lista)

        print(f"La calificación del alumno {lista[0]} es: {calcular_promedio(lista)}")
        if promedio >= 7.0:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha reprobado.") 

        repetir = input("¿Quieres calcular el promedio de otra materia? (s/n): ")

    print("\nResumen de Promedios de Cada Alumno:")
    
    for alumno in lista_alumnos:
        nombre_alumno = alumno[0]
        promedio_alumno = calcular_promedio(alumno)
        print(f"Alumno: {nombre_alumno}, Promedio: {promedio_alumno}")

    print("Adiós")


main()