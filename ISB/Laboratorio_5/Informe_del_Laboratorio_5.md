
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
En el siguiente linke se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_ECG](./Data_ECG)

### *4.5. Ploteo de la señal en Python* <a name="id10"></a> 

##### 4.6.1. Lectura del EKG en reposo

Se utilizaron los archivos de txt de cada grabación del OpenSignals y se generó una lectura de los datos en Python.

|  *EKG en reposo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|


##### 4.6.2. Lectura del EKG respiración profunda antes del ejercicio

|  *EKG respiración profunda antes del ejercicio*  | *Intervalo respectivo*| 
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|

##### 4.6.3. Lectura del EKG después del ejercicio

|  *EKG después del ejercicio*  | *Intervalo respectivo*| 
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|

##### 4.6.4. Lectura del EKG respiración profunda después del ejercicio

|  *EKG respiración profunda después del ejercicio*  | *Intervalo respectivo*| 
|:------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|

   
## *5. Analisis de las señales producidas por el Promsim4* <a name="id11"></a>

Se utilizo el Promsim4, un simulador de signos vitales, el cual nos permitira simular la frecuencia cardiaca. Se llevaron a cabo diversas pruebas. Estas incluyeron la visualización de una frecuencia respiratoria normal, la onda de presión venosa central (CVP), taquicardia ventricular a 160 lpm, fibrilación ventricular severa y asistolia[2].

### 5.1. Lectura del EKG con frecuencia respiratoria Normal

|  *Video*  | *Foto*| *Descripción*|
|:------------:|:---------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/37bd1119-d2b8-4837-9460-908392018482"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (6)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/16bf3972-1bfc-4751-96e1-aed37c86aab1)| ------|


### 5.2. Lectura del EKG con Onda de presión venosa central(CVP)

|  *Video*  | *Foto*| *Descripción*|
|:------------:|:---------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/27c57372-0a59-4922-be60-afab24a67f2c"></video>|![WhatsApp Image 2024-04-20 at 09 10 01](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a67083b8-1738-411c-ab34-6667bfeb9995)
| ------|

### 5.3. Lectura del EKG con taticardia ventricular a 160 lpm

|  *Video*  | *Foto*| *Descripción*|
|:------------:|:---------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/fc4e1382-bc11-4b89-9b64-fcff8c6df573"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (3)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/ce3bb910-914d-4a0b-93c4-cf919fbec6e3)| ------|

### 5.4. Lectura del EKG con fibrilación ventricular severa

|  *Video*  | *Foto*| *Descripción*|
|:------------:|:---------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2d388713-c81f-4b52-b60a-5f07be1ebddc"></video>|![WhatsApp Image 2024-04-20 at 09 10 00 (2)](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a8c8d1bb-f0d1-4872-8c22-c199b270fa90)| ------|

### 5.5. Lectura del EKG con asistolia

|  *Video*  | *Foto*| *Descripción*|
|:------------:|:---------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/125b3219-db6d-4dc6-a762-8f24c9937045"></video>|![WhatsApp Image 2024-04-20 at 09 10 00](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/989f6aa3-c3e0-4de3-aa9d-ce140cd1718b)
| ------|

   
## *6. Bibliografia* <a name="id12"></a>

[1] PLUX – Wireless Biosignals, "BITalino (r)evolution Lab Guide," Lisbon, Portugal, 2020.
[2] ProSim™, "Lectura del EKG con frecuencia respiratoria Normal," Fluke Biomedical, 2024. 

