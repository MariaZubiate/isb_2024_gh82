
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
     4.3 [Resumen y explicación de la señal ploteada](#id8)\
     4.4 [Archivo de los datos de la señal ploteada](#id9)\
     4.5 [Ploteo de la señal en Python](#id10)
5. [Analisis de las señales producidas por el Promsim4](#id11)
6. [Bibliografia](#id12)
   
## *1. Introducción* <a name="id1"></a>

El electrocardiograma(ECG) es una herramienta de diagnóstico utilizada para medir la actividad del corazón. Consiste en colocar electrodos en partes especificas del cuerpo, las cuales tienen contacto con la piel. Estos detectan impulsos eléctricos generados por el corazón. Esta información se registras como ondas en un gráfico.

La señal ECG contan de diferentes componentes, entre ellos esta la onda P, el complejo QRS y la onda T; las cuales representan la despolarización auricular, despolarización ventricular y repolarización ventricular, respectivamente.

El ECG posee 12 derivadas, las cuales permiten visualizar el corazoón desde diferentes ángulos. Estas derivaciones se pueden utilizar para etectar attirmias y transtornos cardíacos. Entre las derivaciones tenemos: derivaciones bipolares(I,II,III), derivaciones unipolares(aVR, aVL,aVF) y derivaciones precordiales(V1-V6)[1]. 

Para la elaboración de esta labotorio hemos decido realizar una analisis de la primera derivada, la cual proporciona información sobre la actividad eléctrica que se dirige hacia y desde la parte frontal del corazón. Estos ensayos nos permitiran visualizar el cambio que surge en las ondas de acuerdo a diferentes actividades realizadas. 

La lectura de la señal ECG se realizará utilizando un dispositivo Bitalino, el cual permite la lectura de señales fisiologicas. Para su uso, se conecta el dispositivo al ordenador mediante un dongle Bluetooth y se emplea el software OpenSignals (r)evolution para la adquisición y análisis de datos. Los electrodos se colocan en diferentes posiciones del cuerpo según el tipo de señal a adquirir, como en el pecho, muñecas o clavículas para el ECG, y luego se realiza la grabación de datos siguiendo el protocolo[1].

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
Siguiendo la guía experimental del BITalino (r)evolution Lab Guide, se procedió a realizar la lectura de ECG utilizando la derivación I con los electrodos colocados en las muñecas. Primero, se acondicionaron las partes del cuerpo que se utilizarían para la colocación de electrodos. Luego, siguiendo las instrucciones proporcionadas en la guía, se colocaron los electrodos en las muñecas: el electrodo positivo (rojo) en la muñeca izquierda, el electrodo negativo (negro) en la muñeca derecha y el electrodo de referencia (blanco) en la parte inferior del abdomen, cerca del hueso de la cadera izquierda[1].

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


### *4.3. Resumen y explicación de la señal ploteada* <a name="id8"></a> 

##### 4.3.1. Lectura del EKG en reposo



##### 4.3.2. Lectura del EKG respiración profunda antes del ejercicio


##### 4.3.3. Lectura del EKG después del ejercicio



##### 4.3.4. Lectura del EKG respiración profunda después del ejercicio



### *4.4. Archivo de los datos de la señal ploteada* <a name="id9"></a> 
En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_ECG](./Data_ECG)

### *4.5. Ploteo de la señal en Python* <a name="id10"></a> 

##### 4.6.1. Lectura del EKG en reposo

Se utilizaron los archivos de txt de cada grabación del OpenSignals y se generó una lectura de los datos en Python.

|  *EKG en reposo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![Reposo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/df0c4abd-b7c2-41fe-8231-423f02dd0857)|![Reposo_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9bba41f0-c1fd-496c-a768-3b0fac98eadc)|![Reposo_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/eab5c839-71e4-41e1-b5bf-eb5d0e6ae2f5)|



##### 4.6.2. Lectura del EKG respiración profunda antes del ejercicio

|  *EKG respiración profunda antes del ejercicio*  | *Intervalo respectivo*|  *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![Breath_antes](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/fbaa7fec-e0c9-4f7e-b47c-43e9d3b75b40)|![Breath_antes_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e936df42-acce-4153-87b5-4a47ce3775bd)|![Breath_antes_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/317b1d50-1f6e-415b-9508-9204d2e0f99c)|


##### 4.6.3. Lectura del EKG después del ejercicio

|  *EKG después del ejercicio*  | *Intervalo respectivo*|  *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![training](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/5e705d44-47fb-4b2d-b88e-88b07702fc23)|![training_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/7fc1e564-e253-40df-9e46-5d56cad7feba)|![Training_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/d3c9e134-f9b8-4c2a-9e7e-0e05ebc63c8e)|


##### 4.6.4. Lectura del EKG respiración profunda después del ejercicio

|  *EKG respiración profunda después del ejercicio*  | *Intervalo respectivo*| *1 Ciclo*| 
|:------------:|:---------------:|:---------------:|
|![breath_despues](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9998790b-392c-47f9-a133-b51de88130e4)|![breath_despues_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/4dd6282f-b17a-449a-82fd-625be9716081)|![Breath_despues_1ciclo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c8c2e3e6-5e32-4128-ac64-1433be78dfaf)|



   
## *5. Analisis de las señales producidas por el Promsim4* <a name="id11"></a>

Se utilizo el Promsim4, un simulador de signos vitales, el cual nos permitira simular la frecuencia cardiaca. Se llevaron a cabo diversas pruebas. Estas incluyeron la visualización de una frecuencia respiratoria normal, la onda de presión venosa central (CVP), taquicardia ventricular a 160 lpm, fibrilación ventricular severa y asistolia[2].
|  *Señal completa en Python*  | *Descripción*|
|:--------------------:|:---------------:|
|![Prosim_completo](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/f7277f70-44eb-44ef-bb78-a00234346d94)|Como se puede visualizar, en la simulación se presenta de manera explícita 5 etapas durante todo el ritmo cardiaco, evidenciado por los diversos patrones en el gráfico de Python. Las cuales se dividen en los siguientes intervalos de tiempo (en "segundos"): 0-40 s, 40-70 s, 70-100 s, 100-130 s y 130-150 s. Cada una de estas corresponde a cierta complicación cardiaca que se describirá más adelante.|


### 5.1. Lectura del EKG con ritmo sinusal normal(RSN) de 80BPM

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/37bd1119-d2b8-4837-9460-908392018482"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (6)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/16bf3972-1bfc-4751-96e1-aed37c86aab1)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa1](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/099ae69d-9aa5-41cb-bad9-d3dd04c5a830)|En esta etapa inicial, el corazón mantiene un ritmo constante de 80 latidos por minuto, caracterizado como ritmo sinusal normal. Este ritmo sugiere que el nódulo sinoauricular, el marcapasos natural del corazón, opera adecuadamente sin evidencia de estrés o deterioro cardíaco. La importancia de replicar fielmente este ritmo en simulaciones es destacada en investigaciones como las de Randazzo et al. (2021), quienes emplean el ProSim 4 de Fluke para verificar la autenticidad de las señales de ECG tanto en condiciones normales como patológicas, garantizando así la precisión del simulador para representar el RSN[C1].|


### 5.2. Lectura del EKG con Onda de presión venosa central(CVP)

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/27c57372-0a59-4922-be60-afab24a67f2c"></video>|![WhatsApp Image 2024-04-20 at 09 10 01](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a67083b8-1738-411c-ab34-6667bfeb9995)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa2](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0c94e45c-0831-4cd9-9931-14a00c65dcb0)|Esta etapa implica medir la presión venosa central, un indicativo de la presión sanguínea en las venas torácicas, que refleja el volumen intravascular y la funcionalidad del lado derecho del corazón. Aunque no se observan arritmias en esta fase, la monitorización de la CVP es crucial para evaluar la capacidad del corazón de manejar el volumen sanguíneo, especialmente bajo condiciones de choque o insuficiencia cardíaca. La capacidad del ProSim 4 de Fluke para simular diversas condiciones cardiovasculares es una función clave en la educación médica y en el desarrollo de equipos médicos, como se evidencia en estudios que validan algoritmos para digitalizar imágenes de ECG utilizando este simulador[2].|

### 5.3. Lectura del EKG con taquicardia ventricular a 160 lpm

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/fc4e1382-bc11-4b89-9b64-fcff8c6df573"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (3)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/ce3bb910-914d-4a0b-93c4-cf919fbec6e3)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa3](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c292c7f2-1af4-47c2-9dd3-420eede14bc7)|En esta fase, el corazón comienza a latir anormalmente rápido, a unos 160 latidos por minuto, en un ritmo originado en los ventrículos. Esta es una arritmia grave que puede ser inestable y puede llevar a una disminución del gasto cardíaco y la perfusión de órganos vitales, incluido el cerebro. Los modelos de redes neuronales convolucionales para el análisis de señales de ECG, como los propuestos por Wasimuddin et al. (2021), demuestran la utilidad del ProSim 4 de Fluke en la simulación de taquicardias para entrenar sistemas de diagnóstico automático[3].|

### 5.4. Lectura del EKG con fibrilación ventricular severa

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2d388713-c81f-4b52-b60a-5f07be1ebddc"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (2)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a8c8d1bb-f0d1-4872-8c22-c199b270fa90)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa4](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9abe390d-c0ce-4d05-98c7-609f2d310670)|Una progresión de la taquicardia ventricular, la fibrilación ventricular es un ritmo cardíaco caótico que resulta en contracciones ventriculares rápidas y desorganizadas. Esta es una condición crítica y es la causa más común de paro cardíaco inmediato. El corazón no puede bombear sangre efectivamente, llevando a un colapso circulatorio. La detección de este tipo de arritmias usando simuladores como el ProSim 4 de Fluke es crucial para el desarrollo de métodos de detección ligeros y efectivos, como los investigados por Vasyltsov et al. (2016)[4].|

### 5.5. Lectura del EKG con asistolía

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/125b3219-db6d-4dc6-a762-8f24c9937045"></video>|![WhatsApp Image 2024-04-20 at 09 10 00](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/989f6aa3-c3e0-4de3-aa9d-ce140cd1718b)
|  *Ploteo Python*  | *Descripción*|
|![Prosim_etapa5](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e1d9d885-4f17-4672-bf54-b576348742a8)|Finalmente, el corazón deja de latir por completo (asistolia), lo que significa ausencia de actividad eléctrica en el corazón. Es uno de los ritmos cardíacos que se presentan en paro cardíaco y requiere intervención médica inmediata para intentar reanimación cardiopulmonar (RCP) y posiblemente el uso de medicamentos y un desfibrilador. La simulación de asistolia en dispositivos como el ProSim 4 permite a los profesionales médicos practicar la respuesta a estos eventos críticos, como se describe en la investigación sobre la precisión de los dispositivos de monitorización de signos vitales[5].|
   
## *6. Bibliografia* <a name="id12"></a>

[1] PLUX – Wireless Biosignals, "BITalino (r)evolution Lab Guide," Lisbon, Portugal, 2020.

[2] ProSim™, "Lectura del EKG con frecuencia respiratoria Normal," Fluke Biomedical, 2024. 

