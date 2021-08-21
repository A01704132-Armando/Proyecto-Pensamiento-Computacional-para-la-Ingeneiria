# Proyecto ¿Qué tan inteligente eres?

### Contexto

Antes de 1983, la inteligencia de un individuo dependía de su capacidad para resolver problemas matemáticos y lógicos. Sin embargo, en 1983 **Howard Gardner**, profesor de la Universidad de Harvard pensaba que la inteligencia es una red de conjuntos autónomos interrelacionados entre si (CEOLEVEL, 2016).

Todas las personas nos destacamos por tener una inteligencia más desarrollada que otras. Y esto es intersante, ya que todos somos diferentes y tenemos inteligencias distintas, además las desarrollamos de manera diferente. 

Hasta la fecha, se han identificado ocho tipos distintos de inteligencia: lingüístico-verbal, lógico-matemática, viso-espacial, musical, corpóral-cinestésica, intrapersonal, interpersonal y naturalista.

<p>>Lingüística (o verbal-lingüística): Habilidad para utilizar con un dominio avanzado el lenguaje oral y escrito.</p>
<p>>Lógico-matemática: Habilidad para el razonamiento complejo, la relación causa-efecto, la abstracción y la resolución de problemas.</p>
<p>>Espacial: Capacidad de percibir el mundo y poder crear imágenes mentales a partir de la experiencia visual. </p>
<p>>Corporal (o quinestésica): Habilidad de utilizar el cuerpo para aprender y para expresar ideas y sentimientos. Incluye el dominio de habilidades físicas.</p>
<p>>Musical (o rítmica): Habilidad de saber utilizar y responder a los diferentes elementos musicales.</p>
<p>>Intrapersonal (o individual): Habilidad de comprenderse a sí mismo y utilizar este conocimiento para operar de manera efectiva en la vida.</p>
<p>>Interpersonal (o social): Habilidad de interactuar y comprender a las personas y sus relaciones.</p>
<p>>Naturalista: Habilidad para el pensamiento científico, para observar la naturaleza, identificar patrones y utilizarla de manera productiva.</p>

![Los 8 tipos de inteligencias](https://www.liderdelemprendimiento.com/wp-content/uploads/2019/05/Los-8-tipos-de-Inteligencia-seg%C3%BAn-Howard-Gardner-3000x1740.jpg)

Fuente: 
CEOLEVEL. (26 de Agosto de 2016). 8 Inteligencias – La teoría de las inteligencias múltiples. Obtenido de CEOLEVEL: https://www.ceolevel.com/8-inteligencias-la-teoria-de-las-inteligencias-multiples

### Mi programa

Este programa planea evaluar 2 de esas inteligencias (verbal y matemática) a través de ceirtas preguntas relacionadas al tema. Para evaluar cada inteligencia se presentarán 3 preguntas, donde si el usuario tuvo bien las 2 preguntas iniciales, la tercera será más complicada o si solo tuvo una bien o ninguna, la computadora arrojará una pregunta más facil. Al final se te darán tus resultados y una breve frase diciendo cual es tu inteligencia dominante o te dirá que ambas de tus inteligencias están igual de desarrolladas en caso de no tener una dominante.


### Algoritmo

#### Sub-algoritmo 1
<p>E0 (resp_usuario, resp_correcta)</p>
<p>cont_mate=0</p>
<p>si resp_usuario==resp_correcta</p>
 <p> imprime ("Correcto, eres muy listo")</p>
  <p>cont_mate= cont_mate+1</p>
<p>si no entonces</p>
<p> imprime ("Mal, que lástima")</p>
  <p>EF(imprime ("resp_correcta"))</p>

  
#### Sub-algoritmo 2
<p>E0 (resp_usuario, resp_correcta)</p>
<p>cont_lin=0</p>
<p>si resp_usuario==resp_correcta</p>
 <p> imprime ("Correcto, eres muy listo")</p>
  <p>cont_lin= cont_lin+1</p>
<p>si no entonces</p>
 <p> imprime ("Mal, que lástima")</p>
 <p> EF(imprime ("resp_correcta"))</p>

  
#### Algoritmo

<p>E0(Nombre, edad)</p>

<p>imprime ("Bienvenido a este test de inteligencia")</p>
<p>imprime ("Sección: Matemáticas")</p>
<p>imprime ("Pregunta 1")</p>
<p>Sub-algoritmo 1</p>
<p>imprime ("Pregunta 2")</p>
<p>Sub-algoritmo 1</p>

<p>si cont_mate=2</p>
<p> imprime ("Pregunta 3 versión difícil")</p>
 <p> Sub-algoritmo 1</p>
  
<p>si no entonces</p>
 <p> imprime ("Pregunta 3 versión fácil")</p>
 <p> Sub-algoritmo 1</p>
  
<p>imprime ("Sección: Lingüística")</p>
<p>imprime ("Pregunta 1")</p>
<p>Sub-algoritmo 2</p>
<p>imprime ("Pregunta 2")</p>
<p>Sub-algoritmo 2</p>

<p>si cont_lin=2</p>
 <p> imprime ("Pregunta 3 versión difícil")</p>
 <p> Sub-algoritmo 2</p>
  
<p>si no entonces</p>
 <p> imprime ("Pregunta 3 versión fácil")</p>
 <p> Sub-algoritmo 2</p>
  
<p>si cont_mate>cont_lin</p>
  <p>imprime ("Tu inteligencia dominante sin duda es la matemática, se nota que se te dan los números :D")</p>
  
<p>si cont_mate<cont_lin</p>
 <p> imprime("Tu inteligencia dominante sin duda es la lingüística, eres todo un poeta :p")</p>
  
<p>si no</p>
<p>imprime ("Dominas ambas inteligencias por igual")</p>


<p>EF (Rregresa cont_mate y cont_lin)</p>
  











