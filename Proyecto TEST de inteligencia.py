"""
Proyecto TEST de Inteligencia python
El programa realiza 3 preguntas de matemáticas y 3 de español
y califica la respuesta del usuario.
Al final le da una calificación y le muestra su inteligencia dominante.
"""

# Biblioteca
# Use esta biblioteca para poder hacer raíces cuadradas y potencias
import math
"""
================== funciones matemáticas  ======================
"""
   
def Vol_cilindro (PI, rad, altura):
    """
    (uso de operadores, uso de funciones)
    recibe: 3 valores numéricos: PI, radio y altura
    Multiplica el valor de PI por rad al cuadrado, por la altura
    devuelve: resultado de la operación: Volumen del cilindro
    """
    return (PI*math.pow(rad, 2)*altura)

    
def Regla_de_tres (v1, v2, v3):
    """
    (uso de operadores, uso de funciones)
    recibe: 3 valores numéricos: 3 volúmenes
    Multiplica v1 por v2 y el resultado lo divide entre v3
    devuelve: resultado de la operación: regla de tres
    """
    return v1*v2/v3

    
def Probabilidad (lista):
    """
    (uso de operadores, uso de funciones, uso de listas)
    recibe: 1 lista
    Resta la suma de todos los elementos numéricos de la lista menos
    la suma del tercer y cuarto elemento de la lista. Este resultado
    se divide entre la suma del total de los elementos.
    devuelve: resultado de la operación multiplicado por 100: Porbabilidad
    """
    Total=sum(lista)
    Grupo_interes=lista[2]+lista[3]
    R=((Total)-(Grupo_interes))/(Total)
    return R*100
 
    
def modulo_vector_resultante (matriz):
    """
    (uso de operadores, uso de funciones, uso de matrices)
    recibe: 1 matriz
    Suma los primeros elementos de ambas listas, suma los segundos
    elementos de cada lista. A esos resultados se les eleva a la
    segunda potencia y se les suma. A ese resultado se le
    aplica raíz cuadrada. 
    devuelve: resultado de la operación: vector resultante
    """
    i=0
    Suma_componentesx=0
    Suma_componentesy=0
    for linea in matriz:
        j=0
        for columna in linea:
            if j==0:
                Suma_componentesx=Suma_componentesx + matriz[i][j]
            if j==1:
                Suma_componentesy=Suma_componentesy + matriz[i][j]
            j=j+1
        i=i+1
        
    Modulo=(math.pow(Suma_componentesx, 2))+(math.pow(Suma_componentesy, 2))
    Modulo=math.sqrt(Modulo)
    return Modulo

    
def Intentos_mate (Res_correcta, cont_mate):
    """
    (uso de operadores, uso de funciones, uso de condiconales,uso de ciclos)
    recibe: 1 contador y la respuesta correcta
    La función compara la respuesta emitida por el usuario con la respuesta correcta.
    Si no son iguales, el usuario tiene otra oportunidad. Si la respuesta final es
    correcta, el contador suma un punto, si no lo es, no suma nada.
    devuelve: El contador de matemáticas
    """
    i=0
    while i<2:
        r=float(input("Introduce tu respuesta"))
        if r ==Res_correcta:
            print ("Muye bien hecho", nombre, "Tu respuesta es correcta \n \n")
            return cont_mate+1
        elif r !=Res_correcta and i ==0:
            print ("Has fallado, intenta otra vez")
        elif r !=Res_correcta and i ==1:
            print ("Has fallado tu segundo intento")
        i=i+1
        
    print("Se agotaron tus intentos :( \nRespuesta correcta:",
          "%.1f" %Res_correcta, "\n \n")
    return cont_mate
        

    
def Intentos_español (Res_correcta, cont_español):
    """
    (uso de operadores, uso de funciones, uso de condiconales,uso de ciclos)
    recibe: 1 contador y la respuesta correcta
    La función compara la respuesta emitida por el usuario con la respuesta correcta.
    Si no son iguales, el usuario tiene otra oportunidad. Si la respuesta final es
    correcta, el contador suma un punto, si no lo es, no suma nada.
    devuelve: El contador de español
    """ 
    i=0
    while i<2:
        r=str(input("Introduce tu respuesta"))
        if r ==Res_correcta:
            print ("Muye bien hecho", nombre, "Tu respuesta es correcta \n \n")
            return cont_español+1
        elif r !=Res_correcta and i ==0:
            print ("Has fallado, intenta otra vez")
        elif r !=Res_correcta and i ==1:
            print ("Has fallado tu segundo intento")
            
        i=i+1
   
    print("Se agotaron tus intentos :( \nRespuesta correcta:"
          ,Res_correcta, "\n\n")
    return cont_español         
 
 
"Parte principal del programa"

nombre=input("Introduzca su nombre")
edad= input("Introduzca su edad")
print("")
print ("Bienvenido a este test de inteligencia", nombre, "\n")

print ("Para cada pregunta poseeras de dos intentos \n \n")
print ("Sección matemáticas \n")

cont_mate=0
 
print ("Redondea tu respuesta a 1 solo decimal en caso de ser necesarios \n")

print ("""Pregunta 1: Calcula el volumen de un cilindro con los siguientes datos:
\nPI=3.1415 \nradio=5 \naltura=10""")
Vol= float("%.1f" %Vol_cilindro(3.1415, 5, 10))
cont_mate=Intentos_mate(Vol, cont_mate)


print ("""Pregunta 2: El vector R es la suma del vector A (3i + 4j) y el vector B
(5i -6j)\n Calcula el módulo o magnitud del vector R""")
Matriz=[[3, 4],[5,-6]]
Modulo_vector=float("%.1f" %modulo_vector_resultante (Matriz))
cont_mate=Intentos_mate(Modulo_vector, cont_mate)

#Si el usuario lleva dos respuesta correctas la siguiente pregunta será más complicada
#Si el usuario lleva al menos un error la siguiente pregunta será más sencilla

if cont_mate <2:
    print ("""Pregunta 3 (versión fácil): Si un almacén de petróleo puede contener
hasta 100 L\nCalcula al cantidad de petróleo que pueden contener 10 almacenes""")
    Regla3=Regla_de_tres(10, 100, 1)
    cont_mate=Intentos_mate(Regla3, cont_mate)

else:
    print ("""Pregunta 3 (versión difícil): En una bolsa hay 8 canicas azules,
4 canicas verdes, 1 canica amarilla 3 canicas naranjas y 7 canicas moradas
\nSi agarro una canica al azar,que posibilidad hay de que
no me salga una canica amarilla o naranja \n""")
    print ("""Recuerda multiplicar tu resultado x100 para que el
    resultado de tu porcentaje sea de 0 a 100""")
    lista=[8, 4, 1, 3, 7]
    Prob=float("%.1f" %Probabilidad(lista))
    cont_mate=Intentos_mate(Prob, cont_mate)
  
print("Tu puntuación de matemáticas ha sido de", cont_mate, "de 3 \n")

print("Sección español")
print("""Importante: Escribe tus respuestas empezando con mayusculas y con
sus acentos correspondientes \n""")
cont_español=0

print ("Pregunta 1: Cual de las siguientes palabras es esdrújula: \nMaíz \nÁrbol \nSábado\n")
cont_español=Intentos_español ("Sábado", cont_español)

print ("""Pregunta 2: En esta oración, ¨Escribiste mal esa palabra,
ya que hidrógeno lleva acento en la primera o¨, \ncual de las siguientes funciones
del lenguaje predomina: \nMetalinguística \nReferencial \nEmotiva \n""")
cont_español=Intentos_español ("Metalinguística", cont_español)

#Si el usuario lleva dos respuesta correctas la siguiente pregunta será más complicada
#Si el usuario lleva al menos un error la siguiente pregunta será más sencilla
if cont_español<2:
    print ("""Pregunta 3 (versión fácil): Cuál de las siguientes palabras es sinónimo
de intromisión:\nPleito \nCorrespondencia \nIntrusión \nConjetura \n""")
    cont_español=Intentos_español ("Intrusión", cont_español)
    
else:
    print ("""Pregunta 3 (versión difícil): En la siguiente frase: ¨Lleve a mi novia a Francia
    y en ese país tan romántico le pedí su mano¨, Escribe la figura retórica empleada \n""")
    cont_español=Intentos_español ("Sinécdoque",cont_español)

print("Tu puntuación de español ha sido de", cont_español, "de 3 \n \n \n")

# Resultados finales del programa
if cont_mate!=cont_español:
    if cont_mate<cont_español:
        print ("Dados los resultados de tu examen", nombre,
               "es notable que tu inteligencia dominante es el español")
    else:
        print ("Dados los resultados de tu examen", nombre,
               "es notable que tu inteligencia en dominante son las matemáticas")
else:
    print ("Dados los resultados de tu examen", nombre,
           "podemos afirmar que dominas ambas inteligencias por igual")