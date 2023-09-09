class promedio :
    a= input ("¿Quieres calcular el promedio de una materia? (s/n):")
    while a== "s":
        materia=str(input("Nombre de la materia:"))
        def calcular_Promedio (P1,P2,P3):
            return (P1+P2+P3)/3
        P1=float (input("Escribe la calificación del primer parcial: "))
        P2=float (input("Escribe la calificación del segundo parcial: "))
        P3=float (input("Escribe la calificación del tercer parcial: "))
        print (f"La calificacion de la materia {materia} es : {calcular_Promedio(P1,P2,P3)}")
        a=input ("¿Quieres calcular el promedio de otra materia?(s/n): ")
    print ("Adios")
promedio ()
                  
            
                     