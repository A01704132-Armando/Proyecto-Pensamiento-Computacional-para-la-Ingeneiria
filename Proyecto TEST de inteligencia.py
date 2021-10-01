#Funciones para la sección de matemáticas
def Vol_cilindro (PI, rad, altura):
    return (PI*rad**2)*altura

def Aceleracion (Vo, Vf, t):
    return (Vf-Vo)/t

def Regla_de_tres (v1, v2, v3):
    return v1*v2/v3
###Función lista
def Probabilidad (lista):
    Total=sum(lista)
    Grupo_interes=lista[2]+lista[3]
    R=((Total)-(Grupo_interes))/(Total)
    return R*100

def Intentos_mate (Res_correcta):
    i=0
    while i<2:
        R=float(input("Introduce tu respuesta"))
        if R ==Res_correcta:
            i=i+2
            return print ("Muye bien hecho", nombre, "Tu respuesta es correcta")
            return print(cont_mate)
        elif R !=Res_correcta:
            if i==0:
                print ("Has fallado, intenta otra vez")
            else:
                return print("Se agotaron tus intentos, has fallado :( \nRespuesta correcta:","%.1f" %Res_correcta)
                return print(cont_mate)
        i=i+1
      
        
def Intentos_español (Res_correcta):
    i=0
    while i<2:
        R=str(input("Introduce tu respuesta"))
        if R ==Res_correcta:
            i=i+2
            return print ("Muye bien hecho", nombre, "Tu respuesta es correcta")
        elif R !=Res_correcta:
            if i==0:
                print ("Has fallado, intenta otra vez")
            else:
                return print("Se agotaron tus intentos, has fallado :( \nRespuesta correcta:",Res_correcta)
                 
        i=i+1
##Solo faltaría agregar contadores para ir sumando la calificación
##Pero me surgieron nuevas dudas y volveré a checarlo en asesoria con el profesor el lunes
#Inicio del programa

nombre=input("Introduzca su nombre")
edad= input("Introduzca su edad")
print("")

print ("Bienvenido a este test de inteligencia", nombre)
print("")


print ("Para cada pregunta poseeras de dos intentos")
print("")
print("")
print ("Sección matemáticas")
print("")

 
print ("Redondea tu respuesta a 1 solo decimal en caso de ser necesarios")

print ("Pregunta 1: Calcula el volumen de un cilindro con los siguientes datos: \nPI=3.1415 \nradio=5 \naltura=10")
Vol= float("%.1f" %Vol_cilindro(3.1415, 5, 10))
Intentos_mate(Vol)


print()
print()

print ("Pregunta 2: Un automóvil inicia su trayecto con una velocidad de 12.3 m/s y termina su trayecto a una velocidad de 150 m/s. \nSi su tiempo en hacer el recorrido fue de 20 segundos, calcula su aceleración promedio")
Ace=float("%.1f" %Aceleracion(12.3, 150, 20))
Intentos_mate (Ace)

print()
print()

print ("Pregunta 3 (versión fácil): Si un almacén de petróleo puede contener hasta 100 L \nCalcula al cantidad de petróleo que pueden contener 10 almacenes")
Regla3=Regla_de_tres(10, 100, 1)
Intentos_mate (Regla3)


print()
print()
###Añadí el uso de listas en este problema matemático
print ("Pregunta 3 (versión difícil): En una bolsa hay 8 canicas azules, 4 canicas verdes, 1 canica amarilla, 3 canicas naranjas y 7 canicas moradas \nSi agarro una canica al azar, que posibilidad hay de que no me salga una canica amarilla o naranja ")
print()
print ("Recuerda multiplicar tu resultado x100 para que el resultado de tu porcentaje sea de 0 a 100")
lista=[8, 4, 1, 3, 7]
Prob=float("%.1f" %Probabilidad(lista))
Intentos_mate(Prob)

print()
print()
print()

print("Sección español")
print("Importante: Escribe tus respuestas empezando con mayusculas y con sus acentos correspondientes")

print ("Pregunta 1: Cual de las siguientes palabras es esdrújula: \nMaíz \nÁrbol \nSábado")
Intentos_español ("Sábado")

print()
print()

print ("Pregunta 2: En esta oración, ¨Escribiste mal esa palabra, ya que hidrógeno lleva acento en la primera o¨, \ncual de las siguientes funciones del lenguaje predomina: \nMetalinguística \nReferencial \nEmotiva ")
Intentos_español ("Metalinguística")

print()
print()

print ("Pregunta 3 (versión fácil): Cuál de las siguientes palabras es sinónimo de intromisión: \nPleito \nCorrespondencia \nIntrusión \nConjetura  ")
Intentos_español ("Intrusión")

print()
print()

print ("Pregunta 3 (versión difícil): En la siguiente frase: ¨Lleve a mi novia a Francia y en ese país tan romántico le pedí su mano¨, Escribe la figura retórica empleada")
Intentos_español ("Sinécdoque")