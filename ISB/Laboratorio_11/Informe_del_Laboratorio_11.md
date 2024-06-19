
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

El artículo describe el conjunto de datos EEGMMIDB, que consiste en más de 1500 registros de EEG obtenidos de 109 voluntarios. Cada sujeto realizó 14 sesiones experimentales que incluyen períodos de reposo con los ojos abiertos y cerrados, así como tareas motoras y de imaginación. Estas tareas implicaron movimientos simples como abrir y cerrar el puño, así como complejas como imaginar dichos movimientos. Los datos están disponibles en formato EDF+ con anotaciones que indican los momentos de inicio de cada tarea específica. Estos datos seran utilizados para realizar un analisis de las señales EEG que se producen al momento de hacer una actividad [4]. 

### *4.1.Filtrado* <a name="id5"></a>

**4.1.1. Filtrado pasa banda**

En primera instania se utiliza un filtro Butterworth de paso de banda para filtrar las señales. Este filtro esta diseñado utilizando las frecuencias de borde de la banda de paso y la banda de detención, normalizadas según la frecuencia de muestreo (fs). El filtro Butterworth se elige debido a su respuesta lineal en la banda de paso, lo que es crucial para mantener la integridad de la señal EEG. Se implementa un filtro Butterworth de cuarto orden con frecuencia de corte mayor de 30 Hz, similar al utilizado en el artículo "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for Electroencephalography Signal"[2]. La frecuencia de corte menor es 1 Hz debido a ICA es sensible a las fluctuaciones de baja frecuencia y, por lo tanto, requiere que los datos sean filtrados con un filtro pasa altas antes de ajustarse [5].

**4.1.2. ICA**

se empleará el artículo "A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components" como base para aplicar el Análisis de Componentes Independientes (ICA) a las señales obtenidas mediante el ultracortex. El objetivo es utilizar esta técnica para separar y distinguir eficazmente entre los distintos estados y eventos registrados [3]. Se utilizo el codigo dado en el labotario para realizar el análisis de componentes independientes. 


### *4.2.Procesamiento (normalización y alineamiento de la señal)* <a name="id6"></a>


### *4.3.Extracción de caractaristicas* <a name="id7"></a>

## *5. Resultados* <a name="id8"></a>


### *5.1. Resultado del filtrado* <a name="id9"></a>

**5.1.1. Resultados del filtrado pasa banda**

Diagrama de bode del filtro pasa banda

![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/b02491c6-fc65-4e16-9117-415ee349f0c0)
![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/a7bc6866-7246-4530-97e5-d732bedcb6c7)

**5.1.2. Resultado del ICA**


**A. LINEA BASE OJOS CERRADOS**

**B. LINEA BASE OJOS ABIERTOS**

**C. ABRIR Y CERRAR PUÑO**

**D. IMAGINAR ABRIR Y CERRAR PUÑO**

### *5.2. Resultado del procesamiento* <a name="id10"></a>



### *5.3. Resultado de la extracción de caracteristicas* <a name="id11"></a>



## *6. Discusión* <a name="id12"></a>

## *7. Conclusiones* <a name="id13"></a>


## *8. Bibliografía* <a name="id14"></a>

[1] PLUX – Wireless Biosignals, SA, "BITalino (r)evolution Lab Guide: Guías experimentales para conocer y aprender sus bioseñales" 15 de febrero de 2021.

[2] S. S. Daud y R. Sudirman, "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for Electroencephalography Signal," 2015 6th International Conference on Intelligent Systems, Modelling and Simulation, 2015, pp. 123-126, doi: 10.1109/ISMS.2015.29.

[3] Dhani Dharmaprani, Hoang K. Nguyen, Trent W. Lewis, Dylan DeLosAngeles, John O. Willoughby, and Kenneth J. Pope. A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 825–828. Orlando, FL, USA, 2016. IEEE. doi:10.1109/EMBC.2016.7590828

[4] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, "BCI2000: A general-purpose brain-computer interface (BCI) system," in IEEE Transactions on Biomedical Engineering. 2004. https://physionet.org/content/eegmmidb/1.0.0/S001/#files-panel

[5]
