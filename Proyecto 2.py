def calcular_promedio(lista):
    suma=0
    for indice in range(1,len(lista)):
        suma=suma+lista[indice] 
    return suma/(len (lista)-1)
def obtener_calificaciones(materias):
    alumno=str(input("Escribe el nombre del alumno: "))
    lista=[alumno]
    for nombre in materias:
        calificaciones=float (input(f"Escribe la calificación de {nombre}: "))
        lista.append(calificaciones)
    return lista 
def main () :
    repetir= input ("¿Quieres calcular el promedio de una materia? (s/n): ")
    materias=["matematicas","espanol"]
    while repetir== "s":
        lista=obtener_calificaciones(materias)
        print (f"La calificacion del alumno {lista[0]} es : {calcular_promedio(lista)}")
        repetir=input ("¿Quieres calcular el promedio de otra materia?(s/n): ")
        
    print ("Adios")
    
main()
