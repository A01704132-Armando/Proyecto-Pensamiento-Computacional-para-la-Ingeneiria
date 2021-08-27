### En esta parte del proyecto usaré operadores aritméticos para hacer la sección de matemáticas
### El programa actual aun no compará respuestas automáticamente, es decrr, no te dira si estas bien o no
### En el siguiente avance implementare funciones

print ("Sección matemáticas")
print ("Redondea tu respuesta a 3 decimales en caso de ser necesarios")
print ("Pregunta 1: Calcula el volumen de un cilindro con los siguientes datos: \nPI=3.1415 \nradio=5 \naltura=10")
PI=3.1415
rad=5
altura=10
Vol_cilindro= (PI*rad**2)*altura

float(input("Introduce tu respuesta"))
print ("Respuesta correcta:","%.3f" %Vol_cilindro)

print()
print()

print ("Pregunta 2: Un automóvil inicia su trayecto con una velocidad de 12.3 m/s y termina su trayecto a una velocidad de 150 m/s. \nSi su tiempo en hacer el recorrido fue de 20 segundos, calcula su aceleración promedio")
Vinicial=12.3
Vfinal=150
t_inicial=0
t_final=20
Ace_prom=(Vfinal-Vinicial)/(t_final-t_inicial)

float(input("Introduce tu respuesta"))
print ("Respuesta correcta:","%.3f" %Ace_prom)

print()
print()

print ("Pregunta 3 (versión fácil): Si un almacén de petróleo puede contener hasta 100 L \nCalcula al cantidad de petróleo que pueden contener 10 almacenes")
Cantidad_almacenes_iniciales=1
Cantidad_almacenes_finales=10
Límite_almacenes_inicial=100

Límite_almacenes_finales= Cantidad_almacenes_finales*Límite_almacenes_inicial/Cantidad_almacenes_iniciales
float(input("Introduce tu respuesta"))
print("Respuesta correcta:","%.0f" %Límite_almacenes_finales)

print()
print()

print ("Pregunta 3 (versión difícil): En una bolsa hay 8 canicas azules, 4 canicas verdes, 1 canica amarilla, 3 canicas naranjas y 7 canicas moradas \nSi agarro una canica al azar, que posibilidad hay de que no me salga una82 canica amarilla o naranja ")
print()
print ("Recuerda multiplicar tu resultado x100 para que el resultado de tu porcentaje sea de 0 a 100")
Azul=8
Verde=4
Amarillo=1
Naranja=3
Morada=7
Total_canicas=Azul+Verde+Naranja+Amarillo+Morada

Probabilidad=((Total_canicas)-(Amarillo+Naranja))/(Total_canicas)
Probabilidad= Probabilidad *100

float(input("Introduce tu respuesta"))
print("Respuesta correcta:","%.3f" %Probabilidad)




