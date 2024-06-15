
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

En la adquisición y procesamiento de señales EEG, es fundamental aplicar técnicas de filtrado para eliminar ruidos y artefactos que pueden distorsionar los datos. Una de las técnicas más comunes es el filtrado pasabanda, que se utiliza para eliminar ruidos en bandas de frecuencia específicas, como el latido del corazón (1-1.5 Hz) y la respiración (0.2-0.5 Hz), permitiendo así una limpieza efectiva de la señal cerebral sin afectar su contenido relevante. Además, se emplean filtros adaptativos, que ajustan sus parámetros en tiempo real para minimizar el impacto del ruido, siendo especialmente útiles cuando las frecuencias del ruido y la señal de interés se superponen. Estas técnicas son esenciales para garantizar la calidad y precisión de los datos EEG, facilitando su uso en aplicaciones como las interfaces cerebro-computadora (BCI)[2].

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

[2] N. Naseer y K.-S. Hong, "fNIRS-based brain-computer interfaces: a review," Frontiers in Human Neuroscience, vol. 9, art. 3, pp. 1-10, Jan. 2015, doi: 10.3389/fnhum.2015.00003. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4309034/#B70
