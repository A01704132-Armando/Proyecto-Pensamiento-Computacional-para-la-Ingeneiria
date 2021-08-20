# Proyecto ¿Qué tan inteligente eres?

### Contexto

Antes de 1983, la inteligencia de un individuo dependía de su capacidad para resolver problemas matemáticos y lógicos. Sin embargo, en 1983 Howard Gardner, profesor de la Universidad de Harvard pensaba que la inteligencia es una red de conjuntos autónomos interrelacionados entre si (CEOLEVEL, 2016).

Todas las personas nos destacamos por tener una inteligencia más desarrollada que otras. Y esto es intersante, ya que todos somos diferentes y tenemos inteligencias distintas, además las desarrollamos de manera diferente. 

Hasta la fecha, se han identificado ocho tipos distintos de inteligencia: lingüístico-verbal, lógico-matemática, viso-espacial, musical, corpóral-cinestésica, intrapersonal, interpersonal y naturalista.

Lingüística (o verbal-lingüística): Habilidad para utilizar con un dominio avanzado el lenguaje oral y escrito.
Lógico-matemática: Habilidad para el razonamiento complejo, la relación causa-efecto, la abstracción y la resolución de problemas.
Espacial: Capacidad de percibir el mundo y poder crear imágenes mentales a partir de la experiencia visual. 
Corporal (o quinestésica): Habilidad de utilizar el cuerpo para aprender y para expresar ideas y sentimientos. Incluye el dominio de habilidades físicas.
Musical (o rítmica): Habilidad de saber utilizar y responder a los diferentes elementos musicales.
Intrapersonal (o individual): Habilidad de comprenderse a sí mismo y utilizar este conocimiento para operar de manera efectiva en la vida.
Interpersonal (o social): Habilidad de interactuar y comprender a las personas y sus relaciones.
Naturalista: Habilidad para el pensamiento científico, para observar la naturaleza, identificar patrones y utilizarla de manera productiva.

Fuente: 
CEOLEVEL. (26 de Agosto de 2016). 8 Inteligencias – La teoría de las inteligencias múltiples. Obtenido de CEOLEVEL: https://www.ceolevel.com/8-inteligencias-la-teoria-de-las-inteligencias-multiples

### Mi programa

Este programa planea evaluar 2 de esas inteligencias (verbal y matemática) a través de ceirtas preguntas relacionadas al tema. Para evaluar cada inteligencia se presentarán 3 preguntas, donde si el usuario tuvo bien las 2 preguntas iniciales, la tercera será más complicada o si solo tuvo una bien o ninguna, la computadora arrojará una pregunta más facil. Al final se te darán tus resultados y una breve frase diciendo cual es tu inteligencia dominante o te dirá que ambas de tus inteligencias están igual de desarrolladas en caso de no tener una dominante.


### Algoritmo

### Sub-algoritmo 1
E0 (resp_usuario, resp_correcta)

cont_mate=0

si resp_usuario==resp_correcta

  imprime ("Correcto, eres muy listo")
  
  cont_mate= cont_mate+1
  
si no entonces

 imprime ("Mal, que lástima")
 
  EF(imprime ("resp_correcta"))
  
  
### Sub-algoritmo 2
E0 (resp_usuario, resp_correcta)

cont_lin=0

si resp_usuario==resp_correcta

  imprime ("Correcto, eres muy listo")
  
  cont_lin= cont_lin+1
  
si no entonces

  imprime ("Mal, que lástima")
  
  EF(imprime ("resp_correcta"))

  
### Algoritmo

E0(Nombre, edad)


imprime ("Bienvenido a este test de inteligencia")

imprime ("Sección: Matemáticas")

imprime (Pregunta 1)

Sub-algoritmo 1

imprime (Pregunta 2)

Sub-algoritmo 1

si cont_mate=2

  imprime ("Pregunta 3 versión difícil")
  
  Subalgoritmo 1
  
si no entonces

  imprime ("Pregunta 3 versión fácil")
  
  Sub-algoritmo 1
  
imprime ("Sección: Lingüística")

imprime (Pregunta 1)

Sub-algoritmo 2

imprime (Pregunta 2)

Sub-algoritmo 2

si cont_lin=2

  imprime ("Pregunta 3 versión difícil")
  
  Subalgoritmo 2
  
si no entonces

  imprime ("Pregunta 3 versión fácil")
  
  Sub-algoritmo 2
  

Si cont_mate>cont_lin

  imprime ("Tu inteligencia dominante sin duda es la matemática, se nota que se te dan los números :D")
  
Si cont_mate<cont_lin

  imprime("Tu inteligencia dominante sin duda es la lingüística, eres todo un poeta :p")
 
Si no

imprime ("Dominas ambas inteligencias por igual")


EF (Rregresa cont_mate y cont_lin)
  











