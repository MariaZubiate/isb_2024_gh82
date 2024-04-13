

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

##### 3.2.1. Lectura del musculo flexor del pulgar

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo felxor del pulgar. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Mano en reposo*  | *Mano sin oposición* | *Mano con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/992c45ce-b300-4fde-93e4-c8b830b24b83"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2f7bf97c-3a95-4edb-8198-c4461e802a22"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/965ca49e-ba45-41da-9031-d3ccff87b05c"></video>|



##### 3.2.2. Lectura del musculo bíceps del brazo

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo bíceps del brazo. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Brazo en reposo*  | *Brazo sin oposición* | *Brazo con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3f7f49c2-6be4-4870-a7e8-eceb64c939a5"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/584f563d-ff11-4118-9ac6-21e6ea6a8d99"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/8cfe8ff7-a35b-416f-97b7-32faa4c2a6cb"></video>|

 

##### 3.2.3. Lectura del musculo gemelo de la pantorrilla

En este experimento, se presentan tres tipos de ensayos realizados para estudiar la actividad del músculo gemelo de la pantorrilla. Estos ensayos incluyen momentos en los que el músculo está en movimiento, momentos de actividad sin oposición y momentos de actividad con oposición. Cada tipo de ensayo ofrece información valiosa sobre la respuesta del músculo en diferentes condiciones, lo que permite un análisis más completo de su funcionamiento y comportamiento

|  *Pierna en reposo*  | *Pierna sin oposición* | *Pierna con oposición* |
|:------------:|:---------------:|:------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1605be48-11b0-41d0-848f-ce09309d112d"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/dfba9255-2c5c-4456-888c-cf01668151e9"></video>|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/677f8032-84da-4d45-aebb-cef48d437505"></video>|

 
 
### *3.3. Ploteo de la señal en OpenSignals* <a name="id6"></a> 

El siguiente video es una recopilación de las imagenes obtenidas por OpenSignals de todos los ensayos en el laboratorio

[![Alt Text](http://img.youtube.com/vi/Wbo8ktPWpFk/0.jpg)](https://youtu.be/Wbo8ktPWpFk)



### *3.4. Resumen y explicación de la señal ploteada* <a name="id7"></a> 
Analizando los gráficos obtenidos, se puede observar claramente cómo varía la amplitud del voltaje en función del estado de actividad del músculo. En el caso de las señales obtenidas durante el reposo muscular, es evidente que la actividad eléctrica es mínima, reflejada por la baja amplitud del voltaje, la cual oscila típicamente entre -20 y 20 mV tanto para el músculo del pulgar como para los bíceps. Esto indica que durante el reposo, la actividad eléctrica en los músculos es casi nula, lo cual es esperado dado que no se está ejerciendo ninguna fuerza o movimiento significativo.

Por otro lado, al analizar las señales durante el movimiento de flexión y extensión muscular, se observa un marcado cambio en la amplitud del voltaje. Durante la fase de flexión, cuando el músculo se contrae y genera tensión, la amplitud del voltaje aumenta significativamente, alcanzando valores muy altos. Este aumento en la amplitud del voltaje refleja la intensa actividad eléctrica generada por la contracción muscular. En contraste, durante la fase de extensión, cuando el músculo se relaja, la amplitud del voltaje tiende a disminuir, ya que la actividad eléctrica asociada con la contracción muscular se reduce gradualmente.

Además, al introducir una fuerza de oposición al movimiento, se puede observar cómo la amplitud del voltaje aumenta aún más. Este aumento en la amplitud del voltaje durante la resistencia externa indica un mayor esfuerzo muscular para contrarrestar la fuerza opuesta. Valores de amplitud superiores a 1.3V sugieren un elevado grado de fuerza muscular aplicada para superar la resistencia externa, lo cual es indicativo del nivel de esfuerzo y actividad muscular requerido para vencer la oposición.
### *3.5. Archivo de los datos de la señal ploteada* <a name="id8"></a> 

En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado

[Documentos_txt](./Documentos_txt)

### *3.6. Ploteo de la señal en Python* <a name="id9"></a> 
##### 3.6.1. Lectura del musculo flexor del pulgar en python

|  *Pulgar en reposo*  | *Pulgar sin oposición, flexión natural* | *Pulgar con oposición* |
|:------------:|:---------------:|:------------:|
|![Pulgar_reposo](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/ea650291-c626-42d1-96a3-71eb2b2c1f6a)|![Pulgar_flexión](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/f4bd28d6-2412-49e2-8f42-4aeb02572335)|![Pulgar_Contra](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/671297fd-4322-4ad3-8094-2fc511170736)|

|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![Pulgar_reposo_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/b74a79d2-78d1-43c1-91b4-ee24a39b73b1)|![Pulgar_flexión_Int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/d6b1a840-a672-4459-b8ee-9dd299fd306b)|![Pulgar_contra_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/be410d64-29a1-44da-a10c-88a79e86fed4)|

##### 3.6.2. Lectura del musculo bíceps del brazo en python

|  *Brazo en reposo*  | *Brazo sin oposición, flexión natural* | *Brazo con oposición* |
|:------------:|:---------------:|:------------:|
|![Bicep_reposo](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/7227ab9f-9e12-44c5-8ad2-eb362351156e)|![Bicep_flexión](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6a85b086-9fb8-4cc4-a952-a5458e5e7111)|![Bicep_contra](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/14e9c29d-bf43-45ab-a9c4-a32181bd0a00)|


|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![Bicep_reposo_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/244eadf5-1287-4f88-af54-24e03b64a297)|![Bicep_flexión_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/ad2ec23f-8472-472d-9903-8bd2471868e1)|![Bicep_contra_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/d74cfbcc-01fe-4100-b90c-b3ea321c7d39)|

##### 3.6.3. Lectura del musculo gemelo de la pantorrilla en python

|  *Pierna en reposo*  | *Pierna sin oposición, flexión natural* | *Pierna con oposición* |
|:------------:|:---------------:|:------------:|
|![Pierna_reposo](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/2be51c73-2aad-4284-a81f-b267c32ab54a)|![Pierna_flexión](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/c88540c0-f4a4-41c8-9939-5e771f7951e1)|![Pierna_contra](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/550f4e78-f06a-4bc5-8f71-9b7549497c85)|

|  *Intervalo respectivo*  | *Intervalo respectivo* | *Intervalo respectivo* |
|:------------:|:---------------:|:------------:|
|![Pierna_reposo_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/3581fc5a-d611-4430-879d-8d0ddf1ec9b3)|![Pierna_flexión_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/c0c99924-371a-4743-a246-ff13ec177b43)|![Pierna_contra_int](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/85840e2b-c3cb-4a92-9ef5-82495df85264)|

   
## *4. Bibliografia* <a name="id10"></a>

[1] Instituto Nacional de Salud del Niño – San Borja. "Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos." Fecha: Octubre 2020. Código: GP-001/INSNSB/UAIE/SUAIEPSE – Neurología Pediátrica V01. Página 1-39.



