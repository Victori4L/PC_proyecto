nombre_materia= (input ("nombre de la materia :"))

def calcular_promedio (cal_P1,cal_P2,cal_P3):
   promedio=((cal_P1 +cal_P2 +cal_P3)/3)
   return promedio 
cal_P1= float(input("Escribe calificación del primer parcial :"))
cal_P2= float(input("Escribe calificación del segundo parcial :"))
cal_P3= float(input("Escribe calificación del tercer parcial :"))
print (f"La calificacion de la materia {nombre_materia} es: {calcular_promedio (cal_P1,cal_P2,cal_P3)}")