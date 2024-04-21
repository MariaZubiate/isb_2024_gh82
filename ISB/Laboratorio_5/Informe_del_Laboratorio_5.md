
# Laboratorio 5
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
     4.5 [Resumen y explicación de la señal ploteada](#id9)
5. [Analisis de las señales producidas por el Promsim4](#id10)
6. [Conclusiones](#id11)
7. [Bibliografia](#id12)
   
## *1. Introducción* <a name="id1"></a>

El electrocardiograma(ECG) es una herramienta de diagnóstico utilizada para medir la actividad del corazón. Consiste en colocar electrodos en partes especificas del cuerpo, las cuales tienen contacto con la piel. Estos detectan impulsos eléctricos generados por el corazón. Esta información se registras como ondas en un gráfico.

La señal ECG contan de diferentes componentes, entre ellos esta la onda P, el complejo QRS y la onda T; las cuales representan la despolarización auricular, despolarización ventricular y repolarización ventricular, respectivamente.

El ECG posee 12 derivadas, las cuales permiten visualizar el corazoón desde diferentes ángulos. Estas derivaciones se pueden utilizar para etectar attirmias y transtornos cardíacos. Entre las derivaciones tenemos: derivaciones bipolares(I,II,III), derivaciones unipolares(aVR, aVL,aVF) y derivaciones precordiales(V1-V6)[1]. 

Para la elaboración de esta labotorio hemos decido realizar una analisis de la primera derivada, la cual proporciona información sobre la actividad eléctrica que se dirige hacia y desde la parte frontal del corazón. Estos ensayos nos permitiran visualizar el cambio que surge en las ondas de acuerdo a diferentes actividades realizadas. 

La lectura de la señal ECG se realizará utilizando un dispositivo Bitalino, el cual permite la lectura de señales fisiologicas. Para su uso, se conecta el dispositivo al ordenador mediante un dongle Bluetooth y se emplea el software OpenSignals (r)evolution para la adquisición y análisis de datos. Los electrodos se colocan en diferentes posiciones del cuerpo según el tipo de señal a adquirir, como en el pecho, muñecas o clavículas para el ECG, y luego se realiza la grabación de datos siguiendo el protocolo [1].

## *2. Objetivos* <a name="id2"></a>

Adquirir señales biomédicas de ECG.
Hacer una correcta configuración de BiTalino.
Extraer la información de las señales ECG del software OpenSignals (r)evolution
## *3. Materiales y equipos* <a name="id3"></a>

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

## *4.Resultados* <a name="id4"></a>

### *4.1. Fotos de conexión usada* <a name="id5"></a>
Siguiendo la guía experimental del BITalino (r)evolution Lab Guide, se procedió a realizar la lectura de ECG utilizando la derivación I con los electrodos colocados en las muñecas. Primero, se acondicionaron las partes del cuerpo que se utilizarían para la colocación de electrodos. Luego, siguiendo las instrucciones proporcionadas en la guía, se colocaron los electrodos en las muñecas: el electrodo positivo (rojo) en la muñeca izquierda, el electrodo negativo (negro) en la muñeca derecha y el electrodo de referencia (blanco) en la parte inferior del abdomen, cerca del hueso de la cadera izquierda [1].

<div align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5a6af5a4-3323-4075-9bdd-5105d31df0ed" alt="Imagen1" width="300">
  <p>Imagen 1. Foto de conexión usada</p>
</div>


Siguiendo la guía, seleccionamos el ejercicio de sentadillas con saltos para realizar un análisis detallado de diferentes aspectos durante la actividad. Estos son:

1. Lectura del EKG en reposo.
2. Lectura del EKG durante la respiración profunda antes del ejercicio.
3. Lectura del EKG después del ejercicio.
4. Lectura del EKG durante la respiración profunda después del ejercicio.
5. Lectura del EKG en caso de paro cardiaco durante la actividad física.

Ejercicio realizado:

<div align="center">

|  *Ejercicio ejecutado*  | *Video*| 
|:------------:|:---------------:|
|Saltos con sentadillas | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/66060780-36f8-4a65-8f14-727dfa776c57"></video>|

</div>

### *4.2. Video de la señal* <a name="id6"></a>

| **TIPO** | **DEFINICIÓN** | **VIDEO** |
|:--------------:|:---------------:|:---------------:|
| Reposo | Análisis del electrocardiograma mientras el paciente se encuentra en reposo antes de iniciar cualquier actividad física. |  <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3749934a-30a9-4a4d-93c8-4abd15446a87"></video>|  
| Respiración profunda antes del ejercicio| Interpretación del electrocardiograma mientras el paciente realiza respiraciones profundas antes de comenzar el ejercicio.  | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/19898561-129a-44d6-9d40-a03e0312c40b"></video> |       
| Despues del ejercicio |  Evaluación del electrocardiograma inmediatamente después de que el paciente haya terminado la actividad física.  |<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/e9841319-294c-4599-b204-97e47710a7f9"></video>| 
|  Respiración profunda después del ejercicio  | Análisis del electrocardiograma mientras el paciente realiza respiraciones profundas después de haber finalizado la actividad física | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/7a17e564-6024-4342-a032-eb8a35acb914"></video>| 

### *4.3. Archivo de los datos de la señal ploteada* <a name="id7"></a> 
En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_ECG](./Data_ECG)

### *4.4. Ploteo de la señal en Python* <a name="id8"></a> 

##### 4.4.1. Lectura del EKG en reposo

Se utilizaron los archivos de txt de cada grabación del OpenSignals y se generó una lectura de los datos en Python.

|  *EKG en reposo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![Reposo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/df0c4abd-b7c2-41fe-8231-423f02dd0857)|![Reposo_int]![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/b03262bd-509d-4733-b70b-183cb8ef3cfc)
|![Reposo_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/eab5c839-71e4-41e1-b5bf-eb5d0e6ae2f5)|

##### 4.4.2. Lectura del EKG respiración profunda antes del ejercicio

|  *EKG respiración profunda antes del ejercicio*  | *Intervalo respectivo*|  *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![Breath_antes](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/fbaa7fec-e0c9-4f7e-b47c-43e9d3b75b40)|![Breath_antes_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e936df42-acce-4153-87b5-4a47ce3775bd)|![Breath_antes_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/317b1d50-1f6e-415b-9508-9204d2e0f99c)|

##### 4.4.3. Lectura del EKG después del ejercicio

|  *EKG después del ejercicio*  | *Intervalo respectivo*|  *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![training](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/5e705d44-47fb-4b2d-b88e-88b07702fc23)|![training_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/7fc1e564-e253-40df-9e46-5d56cad7feba)|![Training_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/d3c9e134-f9b8-4c2a-9e7e-0e05ebc63c8e)|

##### 4.4.4. Lectura del EKG respiración profunda después del ejercicio

|  *EKG respiración profunda después del ejercicio*  | *Intervalo respectivo*| *1 Ciclo*| 
|:------------:|:---------------:|:---------------:|
|![breath_despues](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9998790b-392c-47f9-a133-b51de88130e4)|![breath_despues_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/4dd6282f-b17a-449a-82fd-625be9716081)|![Breath_despues_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c8c2e3e6-5e32-4128-ac64-1433be78dfaf)|

### *4.5. Resumen y explicación de las señales ploteadas* <a name="id9"></a> 

##### 4.5.1. Lectura del EKG en reposo

La primera ilustración presenta un electrocardiograma que revela la función cardiaca de un individuo en estado de reposo. La traza del voltaje, que varía con el transcurso del tiempo, muestra una serie de picos y depresiones regulares que son representativos de un patrón de latido cardíaco normal. Dichos picos se alinean con las etapas distintas de un ciclo cardiaco saludable. La definición y regularidad del gráfico son indicativos de un funcionamiento cardíaco adecuado y proveen un registro confiable para fines de evaluación médica.

La segunda gráfica, aunque comparte la modalidad de la primera, se concentra en una ventana temporal más restringida, específicamente entre los 10 y 20 segundos. Se percibe una variabilidad más acentuada en el gráfico. Esta irregularidad podría interpretarse como una respuesta fisiológica momentánea o el resultado de movimientos mínimos por parte del sujeto, aún cuando se encuentra en reposo.

La tercera gráfica amplía un segmento breve del electrocardiograma, enfocándose en el entorno de los 12 segundos. Este nivel de detalle permite un escrutinio más exhaustivo de los eventos cardíacos que puedan considerarse atípicos. Un pico prominente se distingue dentro de este segmento, lo cual puede sugerir una contracción cardiaca inusualmente vigorosa o una respuesta cardíaca transitoria.

En un intervalo de 10 segundos se aprecia la presencia de 10 ciclos. Aplicando la regla de 3 simple, se obtiene que la frecuencia cardíaca es de 60 lpm. Un valor que está dentro del rango del ritmo cardíaco normal (entre 60 y 100 lpm) [2]

##### 4.5.2. Lectura del EKG respiración profunda antes del ejercicio

En la primera gráfica, tenemos una secuencia de ECG que cubre unos 35 segundos. Durante este tiempo, se nota cómo el patrón de los latidos del corazón cambia, algo que puede estar relacionado con que el sujeto tomó una respiración profunda. Es bien sabido que respirar profundamente puede hacer que el corazón lata más rápido cuando inhalamos y más despacio cuando exhalamos, lo cual es un proceso natural. La gráfica refleja este vaivén con sus altibajos que probablemente coinciden con la respiración del individuo.

La segunda gráfica se centra en una franja de tiempo más breve, específicamente de diez a veinte segundos. En esta sección, el detalle es mayor, permitiendo ver más claramente cómo varía el ritmo cardíaco. Podría ser que esta parte represente cuando la persona está aguantando la respiración y luego la suelta.

Finalmente, la tercera gráfica es un primer plano de un intervalo muy específico, de alrededor de 11.5 a 12.3 segundos. Este nivel de detalle muestra exactamente lo que sucede en un ciclo de respiración o latido del corazón. Se destaca una subida importante en el gráfico que puede ser resultado de cómo la respiración profunda afecta el corazón justo en el momento entre retener el aire y soltarlo.

##### 4.5.3. Lectura del EKG después del ejercicio

La primera imagen muestra un electrocardiograma tomado durante 30 segundos justo después de que nuestro compañero terminó de hacer ejercicio. Es claro que el corazón late más rápido de lo normal, lo cual es esperado tras la actividad física. Se notan muchos picos seguidos en el gráfico, que son los latidos del corazón, mostrando que está trabajando a un ritmo acelerado para recuperarse del esfuerzo.

La segunda imagen es un acercamiento a una parte del ECG, específicamente desde los 10 a los 20 segundos. Esta nos permite ver con más claridad que el corazón sigue latiendo rápido. La señal del ECG aquí tiene bastantes altibajos, mostrando cómo el corazón está respondiendo justo después de hacer ejercicio.

La tercera imagen nos lleva a una mirada más cercana, enfocándonos en los segundos entre 11.5 y 12.3. Aquí se detalla cómo es un solo latido del corazón en ese momento. Hay un pico muy marcado en el gráfico que suele pasar después de un esfuerzo físico y podría significar que el corazón está empujando con más fuerza la sangre debido al ejercicio reciente.

##### 4.5.4. Lectura del EKG respiración profunda después del ejercicio

La primera foto presenta cómo se comporta el corazón cuando se somete a ejercicios de respiración profunda. Durante los 30 segundos que dura la grabación, se ve cómo la línea del ECG sube y baja, lo que seguramente va al ritmo de los respiraciones profundas que está haciendo la persona. Es interesante observar cómo la señal varía, marcando las veces que nuestro compañero toma y suelta aire lentamente.

En la segunda foto, el enfoque es más estrecho, cubriendo solo 10 segundos de actividad cardíaca. Aquí, la señal del ECG parece bailar más, subiendo y bajando con la respiración que aún está controlada por los ejercicios que la persona acababa de hacer. Estos cambios son más evidentes que cuando el corazón está en calma y es justo lo que se esperaría después de respiraciones largas y controladas.

La última foto hace un acercamiento mucho mayor, centrándose en un único ciclo de respiración entre los 11.4 y 12.2 segundos. Podemos apreciar con gran claridad cómo afecta un suspiro profundo al corazón. Hay un pico que sobresale que puede ser justo cuando la persona estaba soltando el aire, un momento en que el corazón a veces toma un pequeño descanso después de tener que bombear un poco más rápido.

## *5. Análisis de las señales producidas por el Prosim4* <a name="id10"></a>

Se utilizo el Promsim4, un simulador de signos vitales, el cual nos permitira simular la frecuencia cardiaca. Se llevaron a cabo diversas pruebas. Estas incluyeron la visualización de una frecuencia respiratoria normal, la onda de presión venosa central (CVP), taquicardia ventricular a 160 lpm, fibrilación ventricular severa y asistolia [3].
|  *Señal completa en Python*  | *Descripción*|
|:--------------------:|:---------------:|
|![Prosim_completo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/f7277f70-44eb-44ef-bb78-a00234346d94)|Como se puede visualizar, en la simulación se presenta de manera explícita 5 etapas durante todo el ritmo cardiaco, evidenciado por los diversos patrones en el gráfico de Python. Las cuales se dividen en los siguientes intervalos de tiempo (en "segundos"): 0-40 s, 40-70 s, 70-100 s, 100-130 s y 130-150 s. Cada una de estas corresponde a cierta complicación cardiaca que se describirá más adelante.|


### 5.1. Lectura del EKG con ritmo sinusal normal(RSN) de 80BPM

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/37bd1119-d2b8-4837-9460-908392018482"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (6)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/16bf3972-1bfc-4751-96e1-aed37c86aab1)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa1](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/099ae69d-9aa5-41cb-bad9-d3dd04c5a830)|En esta etapa inicial, el corazón mantiene un ritmo constante de 80 latidos por minuto, caracterizado como ritmo sinusal normal. Este ritmo sugiere que el nódulo sinoauricular, el marcapasos natural del corazón, opera adecuadamente sin evidencia de estrés o deterioro cardíaco. La importancia de replicar fielmente este ritmo en simulaciones es destacada en investigaciones como las de Randazzo et al. (2021), quienes emplean el ProSim 4 de Fluke para verificar la autenticidad de las señales de ECG tanto en condiciones normales como patológicas, garantizando así la precisión del simulador para representar el RSN [4].|


### 5.2. Lectura del EKG con Onda de presión venosa central(CVP)

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/27c57372-0a59-4922-be60-afab24a67f2c"></video>|![WhatsApp Image 2024-04-20 at 09 10 01](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a67083b8-1738-411c-ab34-6667bfeb9995)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa2](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0c94e45c-0831-4cd9-9931-14a00c65dcb0)|La presión venosa central, es un indicativo de la presión sanguínea en las venas torácicas, que refleja el volumen intravascular y la funcionalidad del lado derecho del corazón. Aunque no se observan arritmias en esta fase, la monitorización de la CVP es crucial para evaluar la capacidad del corazón de manejar el volumen sanguíneo, especialmente bajo condiciones de choque o insuficiencia cardíaca. Sin embargo, se pueden identificar indicadores sutiles en la señal electrocardiográfica tal como la presencia de una onda P alta y puntiaguda en las derivaciones II, III o una desviación del eje eléctrico hacia la derecha en el ECG. De acuerdo con el estudio realizado por Chen y colaboradores en 2020, una monitorización precisa y regular de la presión venosa central en individuos con sepsis se correlaciona con una mejora notable en los resultados clínicos, subrayando el valor crítico de este indicador en el tratamiento efectivo de la sepsis [5].

### 5.3. Lectura del EKG con taquicardia ventricular a 160 lpm

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/fc4e1382-bc11-4b89-9b64-fcff8c6df573"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (3)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/ce3bb910-914d-4a0b-93c4-cf919fbec6e3)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa3](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c292c7f2-1af4-47c2-9dd3-420eede14bc7)|En esta fase, el corazón comienza a latir anormalmente rápido, a unos 160 latidos por minuto, en un ritmo originado en los ventrículos. En la señal electrocardiográfica se puede apreciar complejos QRS anchos y ausencia de ondas P. Esta es una arritmia grave que puede ser inestable y puede llevar a una disminución del gasto cardíaco y la perfusión de órganos vitales, incluido el cerebro. Como se discute en el estudio de Samuel et al. (2022) donde se analiza la conexión entre la frecuencia de taquicardia ventricular (VT) y la mortalidad, examinando cómo la frecuencia y gravedad de la VT influyen en los desenlaces a largo plazo para pacientes con problemas cardíacos. Se identifica que una VT a 160 lpm es un marcador de alto riesgo que requiere intervenciones dirigidas para mejorar las tasas de supervivencia. El estudio subraya la necesidad de una gestión y acción temprana efectivas en estos casos [6].

### 5.4. Lectura del EKG con fibrilación ventricular severa

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2d388713-c81f-4b52-b60a-5f07be1ebddc"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (2)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a8c8d1bb-f0d1-4872-8c22-c199b270fa90)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa4](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9abe390d-c0ce-4d05-98c7-609f2d310670)|Una progresión de la taquicardia ventricular, la fibrilación ventricular es un ritmo cardíaco caótico que resulta en contracciones ventriculares rápidas y desorganizadas. Esta es una condición crítica y es la causa más común de paro cardíaco inmediato. El corazón no puede bombear sangre efectivamente, llevando a un colapso circulatorio. En la señal de electrocardiografía se puede visualizar una ausencia de ondas P, QRS y T distinguibles. Además, en el electrocardiograma se observa una actividad eléctrica desorganizada y rápida, destacándose por presentar cambios significativos en amplitud, frecuencia y forma. Este perfil se identifica por la presencia de ondas irregulares y picos variables, lo que demuestra la falta de contracciones ventriculares regulares y de un ritmo cardíaco estable. En la investigación realizada por Szabó et al. (2020), se explora la eficacia de estrategias para el manejo de la fibrilación ventricular en contextos de emergencia, haciendo énfasis en la importancia de la desfibrilación inmediata y el empleo de agentes antiarrítmicos. El estudio propone una metodología actualizada, fundamentada en descubrimientos recientes, que busca no solo reinstaurar un ritmo cardíaco estable sino también optimizar la perfusión de los órganos después de un episodio de VF. Adicionalmente, destaca la importancia de coordinar eficazmente la reanimación cardiopulmonar avanzada y sugiere protocolos para el seguimiento y minimización de complicaciones posteriores a la reanimación [7].|

### 5.5. Lectura del EKG con asistolía

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/125b3219-db6d-4dc6-a762-8f24c9937045"></video>|![WhatsApp Image 2024-04-20 at 09 10 00](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/989f6aa3-c3e0-4de3-aa9d-ce140cd1718b)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa5](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e1d9d885-4f17-4672-bf54-b576348742a8)|Finalmente, el corazón deja de latir por completo (asistolia), lo que significa ausencia de actividad eléctrica en el corazón. Es uno de los ritmos cardíacos que se presentan en paro cardíaco y requiere intervención médica inmediata para intentar reanimación cardiopulmonar (RCP) y posiblemente el uso de medicamentos y un desfibrilador. Es interesante el hecho de que el ProSim4 puede emitir una señal de asistolia sin casi ningpun ruido, esta precisión es clave durante el desarrollo de equipos de electrocardiografía, tal como lo describe la investigación de Havlík J. & Sušánková M. sobre la precisión de los dispositivos de monitorización de signos vitales [8].|

## *6. Conclusiones* <a name="id11"></a>   

1. Las señales de electrocardiograma (ECG) reflejan la actividad eléctrica del corazón, influenciada por el estado fisiológico y movimiento del individuo. Durante las pruebas, la variabilidad de la frecuencia cardíaca demostró ser un indicador eficaz del estrés autonómico en los participantes, particularmente tras realizar ejercicio físico.
2. La aplicación de Python como lenguaje de programación resultó ser útil para realizar el análisis de datos complejos a partir de la data obtenida en .txt. Tal como se muestran en las imágenes, es posible analizar los episodios cuantitativamente.
3. La implementación de electrodos de superficie requiere una consideración meticulosa en su ubicación y en su fijación a la piel del individuo. Detalles como constantes desconexiones se obtuvieron en electrodos que se utilizaron en zonas anatómicas angulosas lo que generó ruido y la repetición de la muestra.

## *7. Bibliografia* <a name="id12"></a>

[1] PLUX – Wireless Biosignals, "BITalino (r)evolution Lab Guide," Lisbon, Portugal, 2020.

[2] «Dos maneras fáciles y precisas de medir tu frecuencia cardíaca», Mayo Clinic. Accedido: 20 de abril de 2024. [En línea]. Disponible en: https://www.mayoclinic.org/es/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979

[3] ProSim™, "Lectura del EKG con frecuencia respiratoria Normal," Fluke Biomedical, 2024. 

[4] V. Randazzo, J. Ferretti, y E. Pasero, "Anytime ECG monitoring through the use of a low-cost, user-friendly, wearable device," Sensors, vol. 21, no. 18, 2021.

[5] H. Chen, Z. Zhu, C. Zhao, Y. Guo, D. Chen, Y. Wei, y J. Jin, "Central venous pressure measurement is associated with improved outcomes in septic patients: an analysis of the MIMIC-III database," Critical Care, vol. 24, no. 1, p. 674, Dec. 2020, doi: 10.1186/s13054-020-03109-9. Disponible en: https://link.springer.com/article/10.1186/s13054-020-03109-9.

[6] M. Samuel, I. Elsokkari, y JL Sapp, 'Ventricular tachycardia burden and mortality: association or causality?' Canadian Journal of Cardiology, vol. 38, no. 8, pp. 1056-1064, Aug. 2022. Disponible en: https://www.sciencedirect.com/science/article/pii/S0828282X22000617.

[7] Z. Szabó, D. Ujvárosy, T. Ötvös, V. Sebestyén, y colaboradores, 'Handling of ventricular fibrillation in the emergency setting,' Frontiers in Pharmacology, vol. 11, artículo 1640, 2020. Disponible en: https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2019.01640/full.

[8] J. Havlík y M. Sušánková, "Comparison of Home Blood Pressure Measurement Devices on Artificial Signals," presentado en el World Congress on Medical Physics and Biomedical Engineering, 2019.
