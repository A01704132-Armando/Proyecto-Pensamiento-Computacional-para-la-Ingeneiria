# Proyecto ¿Qué tan inteligente eres?

### Contexto

Antes de 1983, era comunmente pensado que la inteligencia de un individuo dependía de su capacidad para resolver problemas matemáticos y lógicos. Sin embargo, en 1983 **Howard Gardner**, profesor de la Universidad de Harvard pensaba que la inteligencia es una red de conjuntos autónomos interrelacionados entre si (CEOLEVEL, 2016).

Todas las personas nos destacamos por tener una inteligencia más desarrollada que otras. Y esto es intersante, ya que esto es otra prueba de que todos somos diferentes y tenemos inteligencias distintas, además las desarrollamos de manera diferente. 

Hasta la fecha, se han identificado ocho tipos distintos de inteligencia: lingüístico-verbal, lógico-matemática, viso-espacial, musical, corpóral-cinestésica, intrapersonal, interpersonal y naturalista.

<p>>Lingüística (o verbal-lingüística): Habilidad para utilizar con un dominio avanzado el lenguaje oral y escrito.</p>
<p>>Lógico-matemática: Habilidad para el razonamiento complejo, la relación causa-efecto, la abstracción y la resolución de problemas.</p>
<p>>Espacial: Capacidad de percibir el mundo y poder crear imágenes mentales a partir de la experiencia visual. </p>
<p>>Corporal (o quinestésica): Habilidad de utilizar el cuerpo para aprender y para expresar ideas y sentimientos. Incluye el dominio de habilidades físicas.</p>
<p>>Musical (o rítmica): Habilidad de saber utilizar y responder a los diferentes elementos musicales.</p>
<p>>Intrapersonal (o individual): Habilidad de comprenderse a sí mismo y utilizar este conocimiento para operar de manera efectiva en la vida.</p>
<p>>Interpersonal (o social): Habilidad de interactuar y comprender a las personas y sus relaciones.</p>
<p>>Naturalista: Habilidad para el pensamiento científico, para observar la naturaleza, identificar patrones y utilizarla de manera productiva.</p>

![Los 8 tipos de inteligencias](https://blog.teachlr.com/wp-content/uploads/2019/08/xArtboard-1-960x540.png.pagespeed.ic.mPGemoYeha.png)
**Referencia de la imagen**: teachlr. (9 de Agosto de 2019). Inteligencias múltiples: 8 tipos de inteligencias. Obtenido de teachlr: https://blog.teachlr.com/inteligencias-multiples/


**Fuente:** 
CEOLEVEL. (26 de Agosto de 2016). 8 Inteligencias – La teoría de las inteligencias múltiples. Obtenido de CEOLEVEL: https://www.ceolevel.com/8-inteligencias-la-teoria-de-las-inteligencias-multiples

### Mi programa

Este programa planea evaluar 2 de esas inteligencias (verbal y matemática) a través de ciertas preguntas relacionadas al tema. Para evaluar cada inteligencia se presentarán 3 preguntas, donde si el usuario tuvo bien las 2 preguntas iniciales, la tercera será más complicada o si solo tuvo una bien o ninguna, la computadora arrojará una pregunta más fácil. Para cada pregunta, el usuario contara con dos intentos. Al final se te darán tus resultados y una breve frase diciendo cual es tu inteligencia dominante o te dirá que ambas de tus inteligencias están igual de desarrolladas en caso de no tener una dominante.

Pagina donde revise la librería empleada en el programa: https://docs.python.org/es/3/library/math.html#module-math


### Algoritmo

#### Sub-algoritmo 1
<p>E0 (resp_usuario, resp_correcta)</p>
<p>i=0</p>
<p>Mientras i<2</p>
 <p> -si resp_usuario==resp_correcta</p>
  <p>   --imprime ("Correcto, eres muy listo")</p>
  <p>  --EF cont_mate= cont_mate+1 y sale del ciclo</p>
 <p> -si resp_usuario!=resp_correcta</p>
  <p>   --imprime ("Mal, intenta de nuevo")</p>
  <p>  --i=i+1</p>
 <p>  --imprime("Se agotaron tus intentos")</p>
 <p>EF cont_mate</p>

  
#### Sub-algoritmo 2
<p>E0 (resp_usuario, resp_correcta)</p>
<p>i=0</p>
<p>Mientras i<2</p>
 <p> -si resp_usuario==resp_correcta</p>
  <p>   --imprime ("Correcto, eres muy listo")</p>
  <p>  --EF cont_Español= cont_Español+1 y sale del ciclo</p>
 <p> -si resp_usuario!=resp_correcta</p>
  <p>   --imprime ("Mal, intenta de nuevo")</p>
  <p>  --i=i+1</p>
 <p>  --imprime("Se agotaron tus intentos")</p>
 <p>EF cont_Español</p>
 
  
#### Algoritmo

<p>E0(Nombre_usaurio, edad)</p>

<p>imprime ("Bienvenido a este test de inteligencia")</p>
<p>imprime ("Sección: Matemáticas")</p>
<p>cont_mate=0</p>
<p>imprime ("Pregunta 1")</p>
<p>Sub-algoritmo 1</p>
<p>imprime ("Pregunta 2")</p>
<p>Sub-algoritmo 1</p>

<p>si cont_mate=2</p>
<p> -imprime ("Pregunta 3 versión difícil")</p>
 <p> -Sub-algoritmo 1</p>
  
<p>si no entonces</p>
 <p> -imprime ("Pregunta 3 versión fácil")</p>
 <p>- Sub-algoritmo 1</p>
  
<p>imprime ("Sección: Español")</p>
<p>cont_Español=0</p>
<p>imprime ("Pregunta 1")</p>
<p>Sub-algoritmo 2</p>
<p>imprime ("Pregunta 2")</p>
<p>Sub-algoritmo 2</p>

<p>si cont_Español=2</p>
 <p> -imprime ("Pregunta 3 versión difícil")</p>
 <p> -Sub-algoritmo 2</p>
  
<p>si no entonces</p>
 <p> -imprime ("Pregunta 3 versión fácil")</p>
 <p> -Sub-algoritmo 2</p>
  
<p>si cont_mate>cont_Español</p>
  <p>-imprime (Nombre_usuario,"Tu inteligencia dominante sin duda es la matemática, se nota que se te dan los números :D")</p>
  
<p>si cont_Español>cont_mate</p>
 <p> -imprime(Nombre_usuario,"Tu inteligencia dominante sin duda es la lingüística, eres todo un poeta :p")</p>
  
<p>si no</p>
<p>-imprime (Nombre_usuario,"Dominas ambas inteligencias por igual")</p>


<p>EF (Rregresa cont_mate y cont_lin)</p>
  











