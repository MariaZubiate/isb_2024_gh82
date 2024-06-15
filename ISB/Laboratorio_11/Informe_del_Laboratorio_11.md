
# Laboratorio 10
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

La electroencefalografía (EEG) es una técnica no invasiva utilizada para medir la actividad eléctrica del cerebro. Esta actividad es generada por la comunicación entre millas de millones de neuronas a través de sinapsis, lo que resulta en cambios en el voltaje a través de la membrana celular. Las señales EEG pueden proporcionar información valiosa sobre la función cerebral, reflejando diferentes procesos cognitivos, estados emocionales y trastornos neurológicos. El cerebro humano consta de regiones distintas, cada una responsable de funciones diferentes como el control motor, el procesamiento sensorial, la memoria y la cognición. Los electrodos EEG se colocan en el cuero cabelludo de acuerdo con el sistema internacional 10-20, permitiendo a los investigadores monitorear la actividad de áreas específicas del cerebro. Estas señales se caracterizan por diferentes bandas de frecuencia, como las ondas gamma, beta, alfa, theta y delta, cada una asociada con estados cerebrales específicos. La EEG se utiliza en diagnósticos médicos para condiciones como la epilepsia y los trastornos del sueño, así como en interfaces cerebro-computadora (BCI) para permitir la comunicación en individuos con discapacidades motoras severas como lesiones de la médula espinal[1].

**Técnicas de Filtrado para EEG**

La filtración de señales EEG es crucial para obtener datos precisos y fiables. Este proceso elimina artefactos como interferencias de línea eléctrica, movimientos musculares y parpadeos oculares, los cuales pueden distorsionar el análisis. Dos métodos de filtrado comunes son el filtro Butterworth de paso de banda de 4º orden y la transformada wavelet estacionaria (SWT). El filtro Butterworth es efectivo pero puede perder información original de la señal. En contraste, la SWT es más eficaz en mantener la integridad de la señal mientras elimina el ruido. Comparando ambos métodos, la SWT demuestra una superioridad en la preservación de la calidad del EEG, según los parámetros de error cuadrático medio (MSE) y relación señal a ruido de pico (PSNR).[2].

## *2. Objetivos* <a name="id2"></a>

1. Aislar frecuencias de interés y eliminar ruido en la señal EEG.
3. Normalizar los datos EEG para un análisis consistente.
4. Extraer y analizar características en bandas de frecuencia específicas.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodología* <a name="id4"></a>

Para la elaboración de este laboratorio se utilizara un repositorio de señales EEG de la pagina de PhysioNet. Este es un estudio sobre "EEG During Mental Arithmetic Tasks". Esta base de datos EEGMAT contiene grabaciones de EEG de sujetos antes y durante la realización de tareas de aritmética mental, utilizando ICA para eliminar artefactos. Incluye registros de 24 sujetos con buen rendimiento y 12 con bajo rendimiento

### *4.1.Filtrado* <a name="id5"></a>

**4.1.1. Filtrado pasa banda**

se utiliza un filtro Butterworth de paso de banda para filtrar señales EEG. Este filtro es diseñado utilizando las frecuencias de borde de la banda de paso y la banda de detención, normalizadas según la frecuencia de muestreo (fs). El filtro Butterworth se elige debido a su respuesta lineal en la banda de paso, lo que es crucial para mantener la integridad de la señal EEG. Se implementa un filtro de cuarto orden, similar al utilizado en el artículo "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for
Electroencephalography Signal"[2].

**4.1.2. ICA**


### *4.2.Procesamiento (normalización y alineamiento de la señal)* <a name="id6"></a>


### *4.3.Extracción de caractaristicas* <a name="id7"></a>

## *5. Resultados* <a name="id8"></a>


### *5.1. Resultado del filtrado* <a name="id9"></a>

**5.1.1. Resultados del filtrado pasa banda**


**5.1.2. Resultado del ICA**


### *5.2. Resultado del procesamiento* <a name="id10"></a>


### *5.3. Resultado de la extracción de caracteristicas* <a name="id11"></a>



## *6. Discusión* <a name="id12"></a>

## *7. Conclusiones* <a name="id13"></a>


## *8. Bibliografía* <a name="id14"></a>

[1] PLUX – Wireless Biosignals, SA, "BITalino (r)evolution Lab Guide: Guías experimentales para conocer y aprender sus bioseñales" 15 de febrero de 2021.

[2] S. S. Daud y R. Sudirman, "Butterworth Bandpass and Stationary Wavelet Transform Filter Comparison for Electroencephalography Signal," 2015 6th International Conference on Intelligent Systems, Modelling and Simulation, 2015, pp. 123-126, doi: 10.1109/ISMS.2015.29.

