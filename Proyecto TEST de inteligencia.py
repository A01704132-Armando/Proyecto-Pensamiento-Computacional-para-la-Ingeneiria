#Inicio del programa

nombre=input("Introduzca su nombre")
edad= input("Introduzca su edad")
print("")

print ("Bienvenido a este test de inteligencia", nombre)
print("")

print ("Sección matemáticas")
print("")

#Funciones para la sección de matemáticas
def Vol_cilindro (PI, rad, altura):
    return (PI*rad**2)*altura

def Aceleracion (Vo, Vf, t):
    return (Vf-Vo)/t

def Regla_de_tres (v1, v2, v3):
    return v1*v2/v3

def Probabilidad (az, ve, am, na, mo):
    return (((az+ve+am+na+mo)-(am+na))/(az+ve+am+na+mo))*100
 
print ("Redondea tu respuesta a 3 decimales en caso de ser necesarios")

print ("Pregunta 1: Calcula el volumen de un cilindro con los siguientes datos: \nPI=3.1415 \nradio=5 \naltura=10")
float(input("Introduce tu respuesta"))
print ("Respuesta correcta:","%.1f" %Vol_cilindro(3.1416, 5, 10))

print()
print()

print ("Pregunta 2: Un automóvil inicia su trayecto con una velocidad de 12.3 m/s y termina su trayecto a una velocidad de 150 m/s. \nSi su tiempo en hacer el recorrido fue de 20 segundos, calcula su aceleración promedio")
float(input("Introduce tu respuesta"))
print ("Respuesta correcta:","%.3f" %Aceleracion(12.3, 150, 20))

print()
print()

print ("Pregunta 3 (versión fácil): Si un almacén de petróleo puede contener hasta 100 L \nCalcula al cantidad de petróleo que pueden contener 10 almacenes")
float(input("Introduce tu respuesta"))
print("Respuesta correcta:","%.0f" %Regla_de_tres(10, 100, 1))

print()
print()

print ("Pregunta 3 (versión difícil): En una bolsa hay 8 canicas azules, 4 canicas verdes, 1 canica amarilla, 3 canicas naranjas y 7 canicas moradas \nSi agarro una canica al azar, que posibilidad hay de que no me salga una canica amarilla o naranja ")
print()
print ("Recuerda multiplicar tu resultado x100 para que el resultado de tu porcentaje sea de 0 a 100")
float(input("Introduce tu respuesta"))
print("Respuesta correcta:","%.3f" %Probabilidad(8, 4, 1, 3, 7))

print()
print()
print()

print("Sección español")

print ("Pregunta 1: Cual de las siguientes palabras es esdrújula: \nMaíz \nÁrbol \nSábado")
input("Introduce tu respuesta")
print ("Respuesta correcta: Sábado")

print()
print()

print ("Pregunta 2: En esta oración, ¨Escribiste mal esa palabra, ya que hidrógeno lleva acento en la primera o¨, \ncual de las siguientes funciones del lenguaje predomina: \nMetalinguística \nRferencial \nEmotiva ")
input("Introduce tu respuesta")
print ("Respuesta correcta: Metalinguística")

print()
print()

print ("Pregunta 3 (versión fácil): Cuál de las siguientes palabras es sinónimo de intromisión: \nPleito \nCorrespondencia \nIntrusión \nConjetura  ")
input("Introduce tu respuesta")
print("Respuesta correcta: Intrusión")

print()
print()

print ("Pregunta 3 (versión difícil): En la siguiente frase: ¨Lleve a mi novia a Francia y en ese país tan romántico le pedí su mano¨, Escribe la figura retórica empleada")
input("Introduce tu respuesta")
print("Respuesta correcta: Sinécdoque")