
# Laboratorio 11
## Integrantes
- Christian Martin Mucha Huatuco
- Maria del Carmen Zubiate Castillo
- Jossef Caleb Tintaya Salva
- Gianni Atilio Di Trani Grández

# *Tabla de contenidos*

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Materiales y equipos](#id3)
4. [Metodología](#id4)\
     4.1 [Filtrado](#id5)\
     4.2 [Procesamiento (normalización y alineamiento de la señal)](#id6)\
     4.3 [Extracción de características)](#id7)
5. [Resultados](#id8)\
     5.1 [Resultados del filtrado pasa banda](#id9)\
     5.2 [Resultado del procesamiento](#id10)\
     5.3 [Resultado de la extracción de características](#id11)
6. [Discusión](#id12)
7. [Conclusiones](#id12)
8. [Bibliografía](#id13)
   
## *1. Introducción* <a name="id1"></a>

La electroencefalografía (EEG) es una técnica no invasiva utilizada para medir la actividad eléctrica del cerebro. Esta actividad es generada por la comunicación entre millas de millones de neuronas a través de sinapsis, lo que resulta en cambios en el voltaje a través de la membrana celular. Las señales EEG pueden proporcionar información valiosa sobre la función cerebral, reflejando diferentes procesos cognitivos, estados emocionales y trastornos neurológicos. El cerebro humano consta de regiones distintas, cada una responsable de funciones diferentes como el control motor, el procesamiento sensorial, la memoria y la cognición. Los electrodos EEG se colocan en el cuero cabelludo de acuerdo con el sistema internacional 10-20, permitiendo a los investigadores monitorear la actividad de áreas específicas del cerebro. Estas señales se caracterizan por diferentes bandas de frecuencia, como las ondas gamma, beta, alfa, theta y delta, cada una asociada con estados cerebrales específicos. La EEG se utiliza en diagnósticos médicos para condiciones como la epilepsia y los trastornos del sueño, así como en interfaces cerebro-computadora (BCI) para permitir la comunicación en individuos con discapacidades motoras severas como lesiones de la médula espinal [1].

**Técnicas de Filtrado para EEG**

El filtrado de señales EEG es crucial para obtener datos precisos y fiables. Este proceso elimina artefactos como interferencias de línea eléctrica, movimientos musculares y parpadeos oculares, los cuales pueden distorsionar el análisis. Dos métodos de filtrado comunes son el filtro Butterworth de paso de banda y la transformada wavelet estacionaria (SWT). El filtro Butterworth es efectivo pero puede perder información original de la señal. En contraste, la SWT es más eficaz en mantener la integridad de la señal mientras elimina el ruido. Comparando ambos métodos, la SWT demuestra una superioridad en la preservación de la calidad del EEG, según los parámetros de error cuadrático medio (MSE) y relación señal a ruido de pico (PSNR)[2].

**Alaisis de componentes Independientes (ICA)**

El Análisis de Componentes Independientes (ICA) en el EEG sirve para separar y discriminar las señales neuronales de los artefactos no deseados presentes en las mediciones. En el EEG, las señales cerebrales pueden verse contaminadas por diversos artefactos, como movimientos oculares, musculares o interferencias ambientales. El ICA utiliza propiedades estadísticas de las señales para descomponer la mezcla observada en componentes independientes, cada uno representando una fuente subyacente. Esto permite identificar y separar las señales cerebrales de estos artefactos, facilitando así un análisis más preciso de la actividad neuronal y mejorando la interpretación de los datos obtenidos en estudios de EEG [3].

## *2. Objetivos* <a name="id2"></a>

1. Aislar frecuencias de interés y eliminar ruido en la señal EEG.
3. Normalizar los datos EEG para un análisis consistente.
4. Extraer y analizar características en bandas de frecuencia específicas.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodología* <a name="id4"></a>

El artículo describe el conjunto de datos EEGMMIDB, que consiste en más de 1500 registros de EEG obtenidos de 109 voluntarios. Cada sujeto realizó 14 sesiones experimentales que incluyen períodos de reposo con los ojos abiertos y cerrados, así como tareas motoras y de imaginación. Estas tareas implicaron movimientos simples como abrir y cerrar el puño, así como complejas como imaginar dichos movimientos. Los datos están disponibles en formato EDF+ con anotaciones que indican los momentos de inicio de cada tarea específica. Estos este laboratorio utilizaremos los datos donde de UN pacientes para realizar un analisis de las señales EEG que se producen al momento de hacer una actividad [4]. 

### *4.1.Filtrado* <a name="id5"></a>

**4.1.1. Filtrado pasa banda**

En primera instania se utiliza un filtro Butterworth de paso de banda para filtrar las señales. Este filtro esta diseñado utilizando las frecuencias de borde de la banda de paso y la banda de detención, normalizadas según la frecuencia de muestreo (fs). El filtro Butterworth se elige debido a su respuesta lineal en la banda de paso, lo que es crucial para mantener la integridad de la señal EEG. Se implementa un filtro Butterworth de cuarto orden con frecuencia de corte mayor de 30 Hz, similar al utilizado en el artículo "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for Electroencephalography Signal"[2]. La frecuencia de corte menor es 1 Hz debido a ICA es sensible a las fluctuaciones de baja frecuencia y, por lo tanto, requiere que los datos sean filtrados con un filtro pasa altas antes de ajustarse [5].

**4.1.2. ICA**

se empleará el artículo "A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components" como base para aplicar el Análisis de Componentes Independientes (ICA) a las señales obtenidas mediante el ultracortex. El objetivo es utilizar esta técnica para separar y distinguir eficazmente entre los distintos estados y eventos registrados [3]. Se utilizo el codigo dado en el labotario para realizar el análisis de componentes independientes. 

**Protocolo experimental**

Este consistió en registrar señales EEG de 64 canales utilizando el sistema BCI2000 mientras los sujetos participaban en diversas tareas motoras e imaginarias. Cada sujeto completó un total de 14 carreras experimentales distribuidas de la siguiente manera:

1. Dos carreras de referencia de un minuto cada una, una con los ojos abiertos y otra con los ojos cerrados.
2. Tres carreras de dos minutos para cada una de las siguientes cuatro tareas:
   - Tarea 1: Realizar movimientos de apertura y cierre de puño izquierdo o derecho en respuesta a estímulos visuales.
   - Tarea 2: Imaginar movimientos de apertura y cierre de puño izquierdo o derecho en respuesta a estímulos visuales.
   - Tarea 3: Realizar movimientos de apertura y cierre simultáneos de ambos puños o ambos pies en respuesta a estímulos visuales.
   - Tarea 4: Imaginar movimientos de apertura y cierre simultáneos de ambos puños o ambos pies en respuesta a estímulos visuales.

Estas tareas fueron repetidas en secuencia, generando un total de 14 carreras experimentales por sujeto. Los datos EEG fueron registrados a una frecuencia de muestreo de 160 muestras por segundo y están disponibles en formato EDF+. Cada carrera experimental está etiquetada con anotaciones que indican los estados de reposo y los inicios de los movimientos reales o imaginarios, codificados como T0, T1 y T2 respectivamente, según las especificaciones del protocolo[4].

### *4.2.Procesamiento (normalización y alineamiento de la señal)* <a name="id6"></a>


### *4.3.Extracción de caractaristicas* <a name="id7"></a>

## *5. Resultados* <a name="id8"></a>


### *5.1. Resultado del filtrado* <a name="id9"></a>

**5.1.1. Resultados del filtrado pasa banda**

A continuación, se presenta el diagrama de Bode del filtro pasa banda. Este diagrama ilustra la respuesta en frecuencia del filtro, mostrando la atenuación de las frecuencias fuera de la banda de paso y la ganancia en la banda de paso, lo que permite evaluar la eficacia del filtro en la eliminación de ruidos no deseados.

Diagrama de bode del filtro pasa banda

| Función de tranferencia |	Angulos |	
|:------------:|:---------------:|
| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/6f617896-65f0-4bbb-8a76-3473804f7427) | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0d2fc9a3-111f-4bd5-a2cd-e977ff637dec)


Señales filtradas: 

| SUJETO 3 	||
|:------------:| :------------:|
 | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/99dac4df-42aa-482a-bd33-d5fe9398c2df)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/af963584-8c9f-445f-874f-2eed2558ff65)|
 ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9ee11b2b-002a-435d-83d8-c671746fcaec)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d10270e7-0cd1-487a-a64a-59db3f4a5731)
  | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0cc4de86-a63d-4565-be5d-59c874c2dfe4) |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/e231f269-57d6-4f76-b6df-80c15ba61dcc)
  | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c28473aa-4813-4624-8773-dae2d675d3ee) | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/fc4d1d97-486b-4e3f-a7ae-a7bbb9da63bd)
| ...... |.....


Los resultados obtenidos con el filtro Butterworth de paso de banda de cuarto orden demuestran una mejora significativa en la calidad de las señales EEG. Al aplicar frecuencias de corte de 1 Hz y 30 Hz, el filtro logra reducir el ruido de baja y alta frecuencia. La señal filtrada mostró una disminución notable en los artefactos indeseados, lo que facilita una interpretación más precisa y fiable de los datos EEG. 


**5.1.2. Resultado del ICA**

 Luego del primer filtrado, se realizo el analisis de ICA.

 1. Usando el codigo
     
![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/8f5ea681-e378-4948-9a7d-7a089d143bb1)

**señales EEG procesadas**

<div align="center">
<img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c236a647-c460-4a0a-9aea-e35f9e69e38d" width="400">
</div>

Podemos visualizar una serie de señales EEG procesadas a través de un filtro ICA (Análisis de Componentes Independientes). Cada fila (ICA000, ICA001, etc.) representa una de las componentes independientes extraídas de las señales EEG originales.

Los diferentes colores (azul, naranja y verde) indican segmentos de tiempo distintos en la grabación de EEG. Los segmentos están etiquetados como T0, T1 y T2:

T0 (azul): Segmentos iniciales o de base.
T1 (naranja): Segmentos intermedios o de algún evento particular.
T2 (verde): Segmentos finales o posteriores a un evento.

**Espectro de Pontencia**

Se la función plot_properties() de MNE para graficar el espectro de potencia de cada componente. Busca un mínimo alrededor de 10 Hz y un pico alrededor de 25 Hz.

|	||
|:------------:| :------------:|
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/91228821-e266-4e7f-b3d2-69e27ee254e8)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1f34482e-48ea-42c6-8de5-f8eb446ab6a8)
|||
![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/bcc007d0-b0d2-46a3-b0d3-b7862c6794ce)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c151088e-d158-4215-bb0b-4d83d1e9ed8b)
|||
![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5d718156-fbd6-4981-9845-9ec0374dcda7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2f8f1462-a13d-43f5-8e43-6ab7dc9b3903)
|||
|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2c552601-9e65-4ff7-9852-becedf2e3375)||


**Grafico de puntuación**

Se realizo un gráfico de puntuaciones de componentes ICA (Análisis de Componentes Independientes) para identificar artefactos musculares en señales EEG. Este gráfico se ha generado mediante un análisis ICA aplicado los datos.

<div align="center">
<img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c3f1cafa-822d-477b-adb9-bc59f52e5092">
</div>

En la imagen, los componentes ICA numerados 5, 10, 12, 13 y 14 son destacados en rojo, lo que indica que han sido identificados automáticamente como artefactos musculares. Las barras rojas muestran que estos componentes tienen puntuaciones significativamente más altas en comparación con otros componentes, lo que sugiere una fuerte correlación con la actividad muscular no deseada. 

### *5.2. Resultado del procesamiento* <a name="id10"></a>



### *5.3. Resultado de la extracción de caracteristicas* <a name="id11"></a>



## *6. Discusión* <a name="id12"></a>

## *7. Conclusiones* <a name="id13"></a>


## *8. Bibliografía* <a name="id14"></a>

[1] PLUX – Wireless Biosignals, SA, "BITalino (r)evolution Lab Guide: Guías experimentales para conocer y aprender sus bioseñales" 15 de febrero de 2021.

[2] S. S. Daud y R. Sudirman, "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for Electroencephalography Signal," 2015 6th International Conference on Intelligent Systems, Modelling and Simulation, 2015, pp. 123-126, doi: 10.1109/ISMS.2015.29.

[3] Dhani Dharmaprani, Hoang K. Nguyen, Trent W. Lewis, Dylan DeLosAngeles, John O. Willoughby, and Kenneth J. Pope. A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 825–828. Orlando, FL, USA, 2016. IEEE. doi:10.1109/EMBC.2016.7590828

[4] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, "BCI2000: A general-purpose brain-computer interface (BCI) system," in IEEE Transactions on Biomedical Engineering. 2004. https://physionet.org/content/eegmmidb/1.0.0/S001/#files-panel

[5] "mne.preprocessing.ICA — Documentación de MNE 1.7.0", MNE Tools, 2024. [En línea]. Disponible: https://mne.tools/stable/generated/mne.preprocessing.ICA.html.
