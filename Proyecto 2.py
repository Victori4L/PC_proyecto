def calcular_promedio(lista):
    suma = 0
    for calificacion in lista:
        suma += calificacion
    return suma / len(lista)

def obtener_calificaciones(materias):
    alumno = input("Escribe el nombre del alumno: ")
    lista = [alumno]
    for nombre in materias:
        calificacion = float(input(f"Escribe la calificación de {nombre}: "))
        lista.append(calificacion)
    return lista
def main():
    repetir = input("¿Quieres calcular el promedio de las materias? (s/n): ")
    materias = ["matematicas", "espanol", "historia", "fisica"]
    matriz_alumnos = []

    while repetir == "s":
        lista = obtener_calificaciones(materias)
        matriz_alumnos.append(lista)

        print(f"La calificación del alumno {lista[0]} es: {calcular_promedio(lista[1:])}")
        if calcular_promedio(lista[1:]) >= 7.0:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha reprobado.")
        repetir = input("¿Quieres calcular el promedio de otro alumno? (s/n): ")

    print("\nResumen de Promedios de Cada Alumno:")
        
    for alumno in matriz_alumnos:
        nombre_alumno = alumno[0]
        promedio_alumno = calcular_promedio(alumno[1:])
        print(f"Alumno: {nombre_alumno}, Promedio: {promedio_alumno}")

    promedios_finales = [calcular_promedio(alumno[1:]) for alumno in matriz_alumnos]
    promedio_total = calcular_promedio(promedios_finales)
    print(f"Promedio final de todos los alumnos: {promedio_total}")

    print("Adiós")

main()
