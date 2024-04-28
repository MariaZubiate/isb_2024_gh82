# Laboratorio 6
## Integrantes
- Christian Martin Mucha Huatuco
- Maria del Carmen Zubiate Castillo
- Jossef Caleb Tintaya Salva
- Gianni Atilio Di Trani Grández

# *Tabla de contenidos*

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Materiales y equipos](#id3)
4. [Resultados](#id4)\
     4.1 [Fotos de conexión usada](#id5)\
     4.2 [Video de señal](#id6)\
     4.3 [Archivo de los datos de la señal ploteada](#id7)\
     4.4 [Ploteo de la señal en Python](#id8)\
     4.5 [Resumen y explicación de la señal ploteada](#id9)\
     4.6 [Fotos de conexión usada](#id10)\
     4.7 [Analisis de las señales producidad por el ultracortex](#id11)\
6. [Conclusiones](#id12)
7. [Bibliografia](#id13)
   
## *1. Introducción* <a name="id1"></a>

La electroencefalografía (EEG) es una técnica no invasiva utilizada para medir la actividad eléctrica del cerebro. Esta actividad es generada por la comunicación entre miles de millones de neuronas a través de sinapsis, lo que resulta en cambios en el voltaje a través de la membrana celular. Las señales EEG pueden proporcionar información valiosa sobre la función cerebral, reflejando diferentes procesos cognitivos, estados emocionales y trastornos neurológicos.
El cerebro humano consta de regiones distintas, cada una responsable de funciones diferentes como el control motor, el procesamiento sensorial, la memoria y la cognición. Los electrodos EEG se colocan en el cuero cabelludo de acuerdo con el sistema internacional 10-20, permitiendo a los investigadores monitorear la actividad de áreas específicas del cerebro. Estas señales se caracterizan por diferentes bandas de frecuencia, como las ondas gamma, beta, alfa, theta y delta, cada una asociada con estados cerebrales específicos.
La EEG se utiliza en diagnósticos médicos para condiciones como la epilepsia y los trastornos del sueño, así como en interfaces cerebro-computadora (BCI) para permitir la comunicación en individuos con discapacidades motoras severas [1].

En esta guía, exploraremos los principios de la EEG, la colocación de electrodos y cómo las diferentes actividades afectan las señales EEG.

## *2. Objetivos* <a name="id2"></a>
- Establecer un conocimiento teórico y práctico sobre la utilización y adquisición de señales EEG.
- Adquirir señales EEG biomédicas


## *3. Materiales y equipos* <a name="id3"></a>

<center>
    
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |  Kit BITalino   |      1       |
|      -       |     Laptop      |      1       |
|      OpenBCI       |     Ultracortex Mark IV EEG Headset      |      1       |
|      OpenBCI       |     OpenBCI Cyton 8-channel Board      |      1       |


</center>


## *4.Resultados* <a name="id4"></a>

### *4.1. Fotos de conexión usada - Caso con el Bitalino*  <a name="id5"></a>

Se colocaron tres electrodos en la persona. Dos de ellos se ubicaron en la frente, con una diferencia de distancia entre ellos, mientras que el tercero se colocó en el hueso detrás de la oreja.

|  **IMAGEN REFERENCIAL**  | **FOTO** | 
|:------------:|:---------------:|
|  ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d57dcfe8-8b8d-48dd-bee5-ead26ace7959)|  ![Sin título](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9dd999c5-c0ad-40af-a152-59310b4cda61) | 
|Fuente: BITalino (r)evolution Lab Guide |Fuente: imagen propia|


### *4.2. Video de la señal* <a name="id6"></a>

 En este inciso se podra visualizar los ensayos que realizamos en el laboratorio.
 
| **TIPO** | **DEFINICIÓN** | **VIDEO** | 
|:--------------:|:---------------:|:---------------:| 
| Reposo | Análisis del elencefalograma mientras el paciente se encuentra en reposo antes de iniciar cualquier actividad. | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/41357d5c-522b-48e1-b125-8d0a8545fcca"></video> |
| Actividad de parpadeo | Análisis del elncefalograma mientras el paciente repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos. |  <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/30d664a2-fdff-4e73-a6b0-2decb3797e09"></video>|  
| Después de la actividad de parpadeo | Análisis del elencefalograma del paciente despues de haber pasado un tiempo de descanso de la actividad  | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a61bb50b-2d60-4ceb-a69b-df26e2ba07ef"></video>| 
| Actividad de lectura | Análisis del elencefalograma mientras el paciente se encuentra  resolviendo mentalmente una serie 4 de ejercicios matemáticos luego de haberlos escuchado|  <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/69a3a3f0-4388-4d91-8c4b-5dc1ddd9e6e4"></video> |

### *4.3. Archivo de los datos de la señal ploteada* <a name="id7"></a> 
En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_EEG](./Data_EEG)

### *4.4. Ploteo de la señal en Python* <a name="id8"></a> 

Se utilizaron los archivos de txt de cada grabación del OpenSignals y se generó una lectura de los datos en Python.

##### 4.4.1. Lectura del EEG en reposo

|  *EEG en reposo*  | *EEG en reposo en un intervalo* |
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/56fff398-4d85-4a3c-8299-c4aa6f67748f)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/20956416-19a1-4371-a47f-cee8803751ba)|

##### 4.4.2. Lectura del EEG durante la actividad de parpadeo

|  *EEG durante la actividad del parpadeo*  | *EEG durante la actividad del parpadeo en un intervalo* |
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/ba18afa6-7288-4a1e-928f-d3ae9082b063)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/2ac2488c-7f4d-452e-9282-2fe3bc9168da)|

##### 4.4.3. Lectura del EEG después de la actividad de parpadeo

|  *EEG después de la actividad de parpadeo*  | *Intervalo respectivo* |
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/21052078-6579-4826-ae00-b37fc1c39fa7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/b19c9f58-2387-4698-9830-e6836662552a)|

##### 4.4.4. Lectura del EEG durante la actividad de resolver problemas mentalmente

|  *EEG durante la actividad de resolver problemas mentalmente*  | *Intervalo respectivo* |
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/93b99507-5070-4d85-8da5-b8ce671d1f97)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/813aa6ae-a466-4aa5-b89f-0530d5b9d1ea)|

### *4.5. Resumen y explicación de las señales ploteadas* <a name="id9"></a> 

##### 4.5.1. Lectura del EEG en reposo

El análisis de la señal electroencefalográfica, o EEG, que se muestra en la gráfica de la izquierda, revela la dinámica actividad eléctrica cerebral cuando una persona se encuentra en estado de descanso. La secuencia temporal, marcada en segundos, y la variabilidad en la magnitud de las señales, medida en microvoltios, son características esperadas de un cerebro en tranquilidad. Investigaciones recientes como las de Zhou y colaboradores [2] sugieren que la intensidad y frecuencia de las ondas alfa durante este estado podrían correlacionarse con los niveles de depresión. Este descubrimiento apunta a una conexión entre los patrones de ondas alfa, comúnmente ligados a estados de calma en personas despiertas pero relajadas, y el estado emocional general. Dicha investigación enfatiza la importancia de las ondas alfa, así como la presencia de ondas beta, que se asocian con niveles mayores de alerta, y las ondas theta y delta, que suelen aparecer en etapas de sueño o en la infancia.

Por otro lado, el gráfico de la derecha, al centrarse en un período más breve, ofrece un vistazo más detallado a la actividad cerebral, resaltando con más precisión la frecuencia y magnitud de cada onda. Los hallazgos de Grassini y su equipo [3] corroboran que actividades relajantes, como mirar videos de entornos naturales, producen cambios en la actividad alfa del EEG, lo que se interpreta como un signo de recuperación fisiológica. Estos cambios son consistentes con las ondas observadas en el gráfico, particularmente las ondas alfa, cuyas frecuencias de 8 a 12 Hz son más notorias en momentos de descanso y relajación, una condición que parece reflejarse en este caso, dado que el sujeto está con los ojos cubiertos.

##### 4.5.2. Lectura del EEG en actividad de parpadeo

1. Señal EEG durante el Parpadeo (izquierda): La visualización muestra la señal EEG extendida sobre un largo periodo, donde se hacen evidentes amplitudes variadas. Estas variaciones distintivas suelen corresponder a los artefactos generados por el parpadeo. En el estudio de Maddirala y Veluvolu [6], se explora cómo se pueden confundir estas señales indeseables con la actividad neuronal real y se propone una metodología para discernirlas y eliminarlas de las grabaciones de EEG, enfatizando la necesidad de tal precisión en el análisis de estos datos.

2. EEG durante la actividad del parpadeo en un intervalo (derecha): Este gráfico, enfocado en un tramo de tiempo reducido, detalla los picos específicos que coinciden con los parpadeos individuales. En la investigación realizada por Jurczak, Kołodziej y Majkowski [7], se ofrece una solución automatizada y eficaz para reconocer y depurar los artefactos de parpadeo de las señales EEG, poniendo de manifiesto la importancia de separar con precisión los eventos neurológicos auténticos de las distorsiones ocasionadas por el movimiento de los párpados.

##### 4.5.3. Lectura del EEG  después de la actividad de parpadeo

1. Señal EEG después del parpadeo (izquierda): La primera gráfica muestra la señal EEG tras una secuencia de parpadeos, revelando una señal más estable con menos picos agudos. Esto podría reflejar una disminución de las distorsiones causadas por los movimientos de los párpados, ofreciendo una visión más clara de la actividad eléctrica cerebral intrínseca. Investigaciones realizadas por Köhler, Stekelenburg y De Baene [8] han analizado las variaciones de las ondas alfa en condiciones de reposo con los ojos cerrados, lo cual es crucial para comprender cómo estas ondas se manifiestan durante la relajación.

2. Intervalo respectivo (derecha): En el gráfico de un segmento más breve, se observa una regularidad en la señal EEG que contrasta con las grabaciones tomadas durante el parpadeo. La investigación de Hohaia, Saurels y Johnston [9] indica que las ondas alfa en la región occipital del cerebro, que emergen cuando los ojos están cerrados, están influenciadas por la actividad visual latente. Esto corrobora la observación de una actividad alfa consistente y refuerza su asociación con estados de descanso más profundos.

##### 4.5.4. Lectura del EEG en actividad de lectura

1. Señal EEG durante la resolución de problemas mentalmente (izquierda): La gráfica muestra una señal EEG con notables fluctuaciones de amplitud a lo largo del tiempo, lo que sugiere una actividad cerebral intensa típica de la resolución de problemas complejos. En la investigación de Molina, Guevara y colaboradores [10], se examina la influencia de la resolución de problemas matemáticos en la actividad cortical, especialmente la aparición de ondas beta y gamma. El estudio arroja luz sobre los patrones de activación cerebral asociados con el pensamiento crítico y la concentración.

2. Intervalo respectivo (derecha): Este gráfico captura la actividad EEG en un fragmento de tiempo más breve durante el ejercicio mental. Los picos visibles pueden corresponder a momentos de aguda concentración y procesamiento cognitivo. Según Lee, Kim y Lee [11], el estrés puede incrementar las ondas beta, una observación que cobra relevancia aquí, ya que resolver ejercicios matemáticos mentalmente es una tarea que podría inducir estrés y requiere atención sostenida.

### *4.6. Fotos de conexión usada - Caso con  Ultracortex Mark IV EEG Headset*  <a name="id10"></a>
El Ultracortex es una serie de dispositivos de electroencefalografía (EEG) desarrollados por OpenBCI. Está diseñado para capturar señales cerebrales y facilitar la investigación y la creación de aplicaciones de interfaz cerebro-computadora. El Ultracortex utiliza electrodos no invasivos colocados en el cuero cabelludo para medir la actividad eléctrica del cerebro, lo que permite el control de dispositivos y la recopilación de datos para diversas aplicaciones en neurociencia, medicina y tecnología [12].





El software de visualización de imágenes del Ultracortex proporciona los datos obtenidos a través de la electroencefalografía (EEG). Nos permitira explorar las señales cerebrales. Con esta herramienta, es posible identificar patrones, correlaciones y cambios en la actividad cerebral [12].

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1f7ea3a4-2e13-4fc6-b815-0b39d2a4ab9a" alt="image" width="400">
</p>
<p align="center">
  <em>Fuente: OpenBCI. "Mark IV — OpenBCI Headwear"</em>
</p>


Se colocó el Ultracortex como la imagen de referencia, teniendo en cuenta la disposición del sistema de electrodos según la distancia de 10-20. Además, se ajustaron las perillas para asegurar el contacto adecuado con el cuero cabelludo.

|  **IMAGEN REFERENCIAL**  | **FOTO** | 
|:------------:|:---------------:|
| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/dc1a8776-fdf2-4a96-8a5b-abbd5f8cb8b3) | ![WhatsApp Image 2024-04-27 at 12 14 16](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5c3ab703-5197-42b2-a6bf-53b9d04affba)| 
|Fuente:OpenBCI. "Mark IV — OpenBCI Headwear" |Fuente: imagen propia|


 ### 4.7. *Analisis de las señales producidad por el ultracortex* <a name="id11"></a>

Se utilizan los archivos .txt proporcionados por OpenBCI para realizar un análisis en Python de las señales cerebrales, con el fin de observar los cambios que ocurren en ellas.

 

 
### *4.7.1. Lectura del EEG en reposo *  

|  *Video*  | *Ploteo en python*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2e21654a-956a-4475-9a5d-179a4b67bda9"></video>|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2f8016b8-afa7-4d03-9081-951fd78951e5)|




### *4.7.2 Lectura del EEG en actividad de parpadeo

|  *Video*  | *Ploteo en python*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/76c1d055-e03b-4ecc-bd0f-000118714b40"></video>|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/aba2da22-dc34-44a2-af5f-979563d73c82)|



### *4.7.3. Lectura del EEG  después de la actividad de parpadeo

|  *Video*  | *Ploteo en python*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/e6355baa-eef5-45e3-bbf5-323ff6a1e495"></video>|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3ee32f99-8b14-47d6-9560-6607fae01ae7)|



### 4.7.4. Lectura del EEG en actividad de lectura

|  *Video*  | *Ploteo en python*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3c0022b9-2858-41f0-88e5-42a6a043d169"></video>|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/167286ed-9f45-45f7-9205-fc8a8300604a)|



## *5. Conclusiones* <a name="id12"></a>   

1. Las variaciones observadas en la actividad cerebral, como los incrementos notados por Nsugbe et al. [1] durante actividades específicas o al solucionar problemas matemáticos, resaltan la versatilidad del cerebro para cumplir con demandas cognitivas y motoras. Los aumentos en frecuencia y amplitud de las ondas beta, identificados por Paszkiel et al. [12] y que normalmente oscilan entre 13 y 30 Hz, indican un estado de alerta y concentración necesarios para tareas de alta demanda cognitiva. Simultáneamente, las ondas theta (4-8 Hz) y delta (1-4 Hz) reflejan procesos mentales asociados con la relajación y la concentración intensa, esenciales para abordar retos intelectuales complejos. Esta capacidad de adaptación de la actividad neuronal no solo demuestra la extraordinaria plasticidad del cerebro, sino que también proporciona una base para el avance de tecnologías como las interfaces cerebro-computadora y los métodos de rehabilitación neurológica.

2. Por otro lado, el notable incremento en la amplitud de las señales EEG, especialmente en las ondas alfa (8-12 Hz) y beta, tras un período de privación visual, destaca una reactividad incrementada del sistema visual, tal como documentan Adeniyi y Awosika [13] y Snipes et al. [14]. Este fenómeno podría estar relacionado con un ajuste en las frecuencias de dichas ondas, en las que las ondas alfa, comúnmente ligadas a la relajación y al acto de cerrar los ojos, muestran un aumento en su potencia y posiblemente una disminución en su frecuencia en respuesta a la necesidad de procesar de forma intensa los estímulos visuales tras la privación. Esta alteración en frecuencia y amplitud es crucial para entender la plasticidad neural del sistema visual y su habilidad para adaptarse a nuevos entornos sensoriales. Además, esta información abre nuevas vías para el desarrollo de tratamientos de rehabilitación visual que emplean periodos controlados de privación visual para potenciar la capacidad visual en pacientes con deficiencias visuales de leves a moderadas.

## *6. Bibliografía* <a name="id13"></a>
[1] PLUX – Wireless Biosignals, S.A., "BITalino (r)evolution Lab Guide: Experimental Guides to Meet & Learn Your Biosignals" OD.LB.04.05, Feb. 15, 2021.

[2] Zhou et al., "Alpha peak activity in resting-state EEG is associated with depressive score," Frontiers in Neuroscience, 2023.

[3] Grassini et al., "Watching nature videos promotes physiological restoration: evidence from the modulation of alpha waves in electroencephalography," Frontiers in Psychology, 2022.

[4] M. Adeniyi, A. Awosika, "Impact of Gender on Post-Exercise Orthostasis Related Changes in EEG Amplitudes," J. Med. Sci, 2023.

[5] S. Snipes, E. Meier, S.N. Meissner, H.P. Landolt, R. Huber, "How and when EEG reflects changes in neuronal connectivity due to time awake," IScience, 2023.

[6] A.K. Maddirala, K.C. Veluvolu, "Eye-blink artifact removal from single channel EEG with k-means and SSA", Scientific Reports, 2021.

[7] M. Jurczak, M. Kołodziej, A. Majkowski, "Implementation of a convolutional neural network for eye blink artifacts removal from the electroencephalography signal", Frontiers in Neuroscience, 2022.

[8] M.S. Köhler, J. Stekelenburg, W. De Baene, "Mental Fatigue and its Effects on Alpha Waves: An EEG study," 2023.

[9] W. Hohaia, B.W. Saurels, A. Johnston, "Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes," Scientific Reports, 2022.

[10] J. Molina, M.Á. Guevara et al., "Cognitive training on the solving of mathematical problems: an EEG study in young men," Actualidades en Psicología, 2021.

[11] C. Kim, J. Lee, K.C. Lee, "An empirical approach to analyzing the effects of stress on individual creativity in business problem-solving: emphasis on the electrocardiogram and electroencephalogram," Frontiers in Psychology, 2022.

[12] OpenBCI. "Mark IV — OpenBCI Headwear", OpenBCI Documentation. April 27, 2024

[13] E. Nsugbe, O.W. Samuel, M.G. Asogbon, G. Li, "A self-learning and adaptive control scheme for phantom prosthesis control using combined neuromuscular and brain-wave bio-signals," Engineering Proceedings, vol. 2, no. 1, 2020.

[14] S. Paszkiel, P. Dobrakowski, A. Łysiak, "The impact of different sounds on stress level in the context of EEG, cardiac measures and subjective stress level: A pilot study," Brain sciences, vol. 10, no. 10, 2020.
