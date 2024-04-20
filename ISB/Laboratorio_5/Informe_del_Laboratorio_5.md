

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
     4.3 [Ploteo de la señal en OpenSignal](#id7)\
     4.4 [Resumen y explicación de la señal ploteada](#id8)\
     4.5 [Archivo de los datos de la señal ploteada](#id9)\
     4.6 [Ploteo de la señal en Python](#id10)
5. [Bibliografia](#id11)
   
## *1. Introducción* <a name="id1"></a>

El electrocardiograma(ECG) es una herramienta de diagnóstico utilizada para medir la actividad del corazón. Consiste en colocar electrodos en partes especificas del cuerpo, las cuales tienen contacto con la piel. Estos detectan impulsos eléctricos generados por el corazón. Esta información se registras como ondas en un gráfico.

La señal ECG contan de diferentes componentes, entre ellos esta la onda P, el complejo QRS y la onda T; las cuales representan la despolarización auricular, despolarización ventricular y repolarización ventricular, respectivamente[1].

El ECG posee 12 derivadas, las cuales permiten visualizar el corazoón desde diferentes ángulos. Estas derivaciones se pueden utilizar para etectar attirmias y transtornos cardíacos. Entre las derivaciones tenemos: derivaciones bipolares(I,II,III), derivaciones unipolares(aVR, aVL,aVF) y derivaciones precordiales(V1-V6). 

Para la elaboración de esta labotorio hemos decido realizar una analisis de la primera derivada, la cual proporciona información sobre la actividad eléctrica que se dirige hacia y desde la parte frontal del corazón. Estos ensayos nos permitiran visualizar el cambio que surge en las ondas de acuerdo a diferentes actividades realizadas. 


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
Siguiendo la guia experimental del BITalino (r)evolution Lab Guide, se procedio a hacer la lectura de ECG. Para ellos primero se acondiciono las partes del cuerpo a utilizar y luego se procedio a colocar los electrodos, como se puede observar en la imagen 1. 

<div align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/b1c71f32-25c3-4a37-9769-9ec741d84f95" width="300" alt="Descripción de la imagen">
</div>



### *4.2. Video de la señal* <a name="id6"></a>
Despues de colocar los electrodos, se procedio a realizar las siguientes lecturas: ECG en reposo, ECG con respiración profunda antes del ejercicio, ECG despues del ejercicio, ECG con respiración profund despues del ejercicio. 

| **TIPO** | **DEFINICIÓN** | **VIDEO** |
|:--------------:|:---------------:|:---------------:|
| Reposo | ----- |  ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/f2de5d5f-7580-4284-8e2b-142b4efcb1d5)|  
| Respiración profunda antes del ejercicio| ----- |    ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/57579b71-3884-4310-a65b-d75a4c717991)|       
| Despues del ejercicio |  ----- | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/fc5902ee-1275-4d23-a308-8ae1bdd27b88)| 
|  Respiración profunda después del ejercicio  | ----- |  ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2216a6ef-5142-4160-81ff-2c16fb761911) | 
| Paro cardiaco | ----- ||


##### 4.2.1. Lectura del EKG en reposo

![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)

##### 4.2.2. Lectura del EKG respiración profunda antes del ejercicio

![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)

##### 4.2.3. Lectura del EKG después del ejercicio

![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)

##### 4.2.4. Lectura del EKG respiración profunda después del ejercicio

![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)

##### 4.2.5 Lectura del EKG paro cardiaco

### *4.3. Ploteo de la señal en OpenSignals* <a name="id7"></a> 

|  *EKG en reposo*  | *EKG respiración profunda antes del ejercicio*|  *EKG después del ejercicio*  | *EKG respiración profunda después del ejercicio*| 
|:------------:|:---------------:| :------------:|:---------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/11e4b0c5-04fe-4bb4-842f-c12f540d4b12)|

### *4.4. Resumen y explicación de la señal ploteada* <a name="id8"></a> 

### *4.5. Archivo de los datos de la señal ploteada* <a name="id9"></a> 
En el siguiente linke se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_ECG](./Data_ECG)

### *4.6. Ploteo de la señal en Python* <a name="id10"></a> 

##### 4.6.1. Lectura del EKG en reposo

|  *EKG en reposo*  | *Intervalo respectivo*| 
|:------------:|:---------------:|
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

   
## *5. Bibliografia* <a name="id11"></a>

[1] PLUX – Wireless Biosignals, "BITalino (r)evolution Lab Guide," Lisbon, Portugal, 2020.
[1] Facultad de Medicina de la Universidad Complutense, "Electrocardiografia basica. Realizacion e interpretacion de un ECG", Madrid, 2012.

