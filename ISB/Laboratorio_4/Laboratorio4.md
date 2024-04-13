

# Laboratorio 4

# *Tabla de contenidos*

1. [Objetivos](#id1)
2. [Materiales y equipos](#id2)
3. [Resultados](#id3)\
     3.1 [Fotos de conexión usada](#id4)\
     3.2 [Video de señal](#id5)\
     3.3 [Ploteo de la señal en OpenSignal](#id6)\
     3.4 [Resumen y explicación de la señal ploteada](#id7)\
     3.5 [Archivo de los datos de la señal ploteada](#id8)\
     3.6 [Ploteo de la señal en Python](#id9)
4. [Bibliografia](#id10)
   
## *1. Objetivos* <a name="id1"></a>
* Adquirir señales biomédicas de EMG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG del software OpenSignals (r)evolution

## *2. Materiales y equipos* <a name="id2"></a>
* Kit BITalino
* Laptop  


##
La electromiografía y la velocidad de conducción nerviosa son procedimientos fundamentales en el diagnóstico y seguimiento de patologías que afectan el sistema nervioso periférico en pacientes pediátricos. La Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos, elaborada por el Instituto Nacional de Salud del Niño – San Borja, proporciona un marco técnico estandarizado para la realización de estos estudios[1]. 

En nuestro laboratorio, nos hemos guiado por este documento para llevar a cabo tres pruebas de electromiografía en diferentes regiones del cuerpo: mano, brazo y pierna. Esta guía nos ha permitido estandarizar los procesos, garantizando la calidad de los estudios realizados y asegurando una buena obtención de resultados.
##

## *3. RESULTADOS* <a name="id3"></a>

### *3.1. Fotos de conexión usada* <a name="id4"></a>
Se utilizó la placa Bitalino con conexión EMG, empleando el sensor EMG de 3 electrodos, como se puede visualizar en la siguiente imagen 

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/be068f65-d8cb-4049-86eb-769473c3d3de" alt="Bitalino" width="200">
</p>



### *3.2. Video de la señal* <a name="id5"></a>

Descripción de los patrones de actividad eléctrica esperados durante una electromiografía (EMG).

|  *En reposo*  | *Sin oposición* | *Con oposición* |
|:------------:|:---------------:|:------------:|
|Líneas de base estables.|Potenciales de acción muscular en respuesta al movimiento|Cambios en la amplitud y frecuencia de los potenciales de acción muscular en relación con la fuerza y velocidad del movimiento|

##### 3.2.1. Lectura del musculo de la mano

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo de la mano. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Mano en reposo*  | *Mano sin oposición* | *Mano con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/992c45ce-b300-4fde-93e4-c8b830b24b83"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2f7bf97c-3a95-4edb-8198-c4461e802a22"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/965ca49e-ba45-41da-9031-d3ccff87b05c"></video>|



##### 3.2.2. Lectura del musculo del brazo

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo del brazo. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Brazo en reposo*  | *Brazo sin oposición* | *Brazo con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f7f49c2-6be4-4870-a7e8-eceb64c939a5"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/584f563d-ff11-4118-9ac6-21e6ea6a8d99"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/8cfe8ff7-a35b-416f-97b7-32faa4c2a6cb"></video>|

 

##### 3.2.3. Lectura del musculo de la pierna

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo de la pierna. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Pierna en reposo*  | *Pierna sin oposición* | *Pierna con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1605be48-11b0-41d0-848f-ce09309d112d"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/dfba9255-2c5c-4456-888c-cf01668151e9"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/677f8032-84da-4d45-aebb-cef48d437505"></video>|

 
 
### *3.3. Ploteo de la señal en OpenSignals* <a name="id6"></a> 

El siguiente video es una recopilación de las imagenes obtenidas por OpenSignals de todos los ensayos en el laboratorio

[![Alt Text](http://img.youtube.com/vi/Wbo8ktPWpFk/0.jpg)](https://youtu.be/Wbo8ktPWpFk)



### *3.4. Resumen y explicación de la señal ploteada* <a name="id7"></a> 


### *3.5. Archivo de los datos de la señal ploteada* <a name="id8"></a> 

En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado

[Documentos_txt](./Documentos_txt)

### *3.6. Ploteo de la señal en Python* <a name="id9"></a> 
##### 3.6.1. Lectura del musculo de la mano en python

|  *Mano en reposo*  | *Mano sin oposición* | *Mano con oposición* |
|:------------:|:---------------:|:------------:|
|![image](![Imagen de WhatsApp 2024-04-13 a las 12 37 57_6449a3ca](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/36754cd3-20e4-450d-b5aa-182fa0f672eb)
)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|

|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd7e29b1-d61b-4be6-befa-e061fe3a6ad7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|

##### 3.6.2. Lectura del musculo del brazo en python

|  *Brazo en reposo*  | *Brazo sin oposición* | *Brazo con oposición* |
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd7e29b1-d61b-4be6-befa-e061fe3a6ad7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|

|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd7e29b1-d61b-4be6-befa-e061fe3a6ad7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|

##### 3.6.3. Lectura del musculo de la pierna en python

|  *Pierna en oposición*  | *Pierna sin oposición* | *Pierna con oposición* |
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd7e29b1-d61b-4be6-befa-e061fe3a6ad7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|

|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd7e29b1-d61b-4be6-befa-e061fe3a6ad7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/97120fc9-2a07-488a-acd9-81c31a551415)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f64e938-6199-4083-a62c-741eb4a157a7)|
 
   
## *4. Bibliografia* <a name="id10"></a>

[1] Instituto Nacional de Salud del Niño – San Borja. "Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos." Fecha: Octubre 2020. Código: GP-001/INSNSB/UAIE/SUAIEPSE – Neurología Pediátrica V01. Página 1-39.



