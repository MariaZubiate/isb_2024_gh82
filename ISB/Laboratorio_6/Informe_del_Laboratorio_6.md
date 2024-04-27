


# Laboratorio 6
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
     4.5 [Resumen y explicación de la señal ploteada](#id9)\
     4.6 [Fotos de conexión usada](#id10)\
     4.7 [Analisis de las señales producidad por el ultracortex](#id11)\
6. [Conclusiones](#id12)
7. [Bibliografia](#id13)
   
## *1. Introducción* <a name="id1"></a>

La electroencefalografía (EEG) es una técnica no invasiva utilizada para medir la actividad eléctrica del cerebro. Esta actividad es generada por la comunicación entre miles de millones de neuronas a través de sinapsis, lo que resulta en cambios en el voltaje a través de la membrana celular. Las señales EEG pueden proporcionar información valiosa sobre la función cerebral, reflejando diferentes procesos cognitivos, estados emocionales y trastornos neurológicos.
El cerebro humano consta de regiones distintas, cada una responsable de funciones diferentes como el control motor, el procesamiento sensorial, la memoria y la cognición. Los electrodos EEG se colocan en el cuero cabelludo de acuerdo con el sistema internacional 10-20, permitiendo a los investigadores monitorear la actividad de áreas específicas del cerebro. Estas señales se caracterizan por diferentes bandas de frecuencia, como las ondas gamma, beta, alfa, theta y delta, cada una asociada con estados cerebrales específicos.
La EEG se utiliza en diagnósticos médicos para condiciones como la epilepsia y los trastornos del sueño, así como en interfaces cerebro-computadora (BCI) para permitir la comunicación en individuos con discapacidades motoras severas[1].

En esta guía, exploraremos los principios de la EEG, la colocación de electrodos y cómo las diferentes actividades afectan las señales EEG.

## *2. Objetivos* <a name="id2"></a>
- Establecer un conocimiento teórico y práctico sobre la utilización y adquisición de señales EEG.
- Adquirir señales EEG biomédicas


## *3. Materiales y equipos* <a name="id3"></a>

<center>
    
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |  Kit BITalino   |      1       |
|      -       |     Laptop      |      1       |
|      OpenBCI       |     Ultracortex Mark IV EEG Headset      |      1       |
|      OpenBCI       |     OpenBCI Cyton 8-channel Board      |      1       |


</center>


## *4.Resultados* <a name="id4"></a>

### *4.1. Fotos de conexión usada - Caso con el Bitalino*  <a name="id5"></a>

Se colocaron tres electrodos en la persona. Dos de ellos se ubicaron en la frente, con una diferencia de distancia entre ellos, mientras que el tercero se colocó en el hueso detrás de la oreja.

|  **IMAGEN REFERENCIAL**  | **FOTO** | 
|:------------:|:---------------:|
|  ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d57dcfe8-8b8d-48dd-bee5-ead26ace7959)|  ![Sin título](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9dd999c5-c0ad-40af-a152-59310b4cda61) | 
|Fuente: BITalino (r)evolution Lab Guide |Fuente: imagen propia|


### *4.2. Video de la señal* <a name="id6"></a>

 En este inciso se podra visualizar los ensayos que realizamos en el laboratorio.
 
| **TIPO** | **DEFINICIÓN** | **VIDEO** | 
|:--------------:|:---------------:|:---------------:| 
| Reposo | Análisis del elencefalograma mientras el paciente se encuentra en reposo antes de iniciar cualquier actividad. | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/41357d5c-522b-48e1-b125-8d0a8545fcca"></video> |
| Actividad de parpadeo | Análisis del elncefalograma mientras el paciente repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos. |  <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/30d664a2-fdff-4e73-a6b0-2decb3797e09"></video>|  
| Después de la actividad de parpadeo | Análisis del elencefalograma del paciente despues de haber pasado un tiempo de descanso de la actividad  | <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a61bb50b-2d60-4ceb-a69b-df26e2ba07ef"></video>| 
| Actividad de lectura | Análisis del elencefalograma mientras el paciente se encuentra  leyendo en voz alta una serie de ejercicios matemáticos|  <video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/69a3a3f0-4388-4d91-8c4b-5dc1ddd9e6e4"></video> |

### *4.3. Archivo de los datos de la señal ploteada* <a name="id7"></a> 
En el siguiente link se puede visualizar los archivos .txt de cada ensayo realizado.
[Data_EEG](./Data_EEG)

### *4.4. Ploteo de la señal en Python* <a name="id8"></a> 

Se utilizaron los archivos de txt de cada grabación del OpenSignals y se generó una lectura de los datos en Python.

##### 4.4.1. Lectura del EEG en reposo

|  *EEG en reposo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|------------|---------------|------------|

##### 4.4.2. Lectura del EEG en actividad de parpadeo

|  *EEG en actividad de parpadeo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|------------|---------------|------------|

##### 4.4.3. Lectura del EEG después de la actividad de parpadeo

|  *EEG después de la actividad de parpadeo*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|------------|---------------|------------|

##### 4.4.4. Lectura del EEG en actividad de lectura

|  *EEG en actividad de lectura*  | *Intervalo respectivo* | *1 Ciclo*|
|:------------:|:---------------:|:------------:|
|------------|---------------|------------|

### *4.5. Resumen y explicación de las señales ploteadas* <a name="id9"></a> 

##### 4.5.1. Lectura del EEG en reposo

##### 4.5.2. Lectura del EEG en actividad de parpadeo

##### 4.5.3. Lectura del EEG  después de la actividad de parpadeo

##### 4.5.4. Lectura del EEG en actividad de lectura


### *4.6. Fotos de conexión usada - Caso con  Ultracortex Mark IV EEG Headset*  <a name="id10"></a>
El Ultracortex es una serie de dispositivos de electroencefalografía (EEG) desarrollados por OpenBCI. Está diseñado para capturar señales cerebrales y facilitar la investigación y la creación de aplicaciones de interfaz cerebro-computadora. El Ultracortex utiliza electrodos no invasivos colocados en el cuero cabelludo para medir la actividad eléctrica del cerebro, lo que permite el control de dispositivos y la recopilación de datos para diversas aplicaciones en neurociencia, medicina y tecnología[2].





El software de visualización de imágenes del Ultracortex proporciona los datos obtenidos a través de la electroencefalografía (EEG). Nos permitira explorar las señales cerebrales. Con esta herramienta, es posible identificar patrones, correlaciones y cambios en la actividad cerebral[2].

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1f7ea3a4-2e13-4fc6-b815-0b39d2a4ab9a" alt="image" width="400">
</p>
<p align="center">
  <em>Fuente: OpenBCI. "Mark IV — OpenBCI Headwear"</em>
</p>


Se colocó el Ultracortex como la imagen de referencia, teniendo en cuenta la disposición del sistema de electrodos según la distancia de 10-20. Además, se ajustaron las perillas para asegurar el contacto adecuado con el cuero cabelludo.

|  **IMAGEN REFERENCIAL**  | **FOTO** | 
|:------------:|:---------------:|
| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/dc1a8776-fdf2-4a96-8a5b-abbd5f8cb8b3) | ![WhatsApp Image 2024-04-27 at 12 14 16](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5c3ab703-5197-42b2-a6bf-53b9d04affba)| 
|Fuente:OpenBCI. "Mark IV — OpenBCI Headwear" |Fuente: imagen propia|


 ### 4.7. *Analisis de las señales producidad por el ultracortex* <a name="id11"></a>

Se utilizan los archivos .txt proporcionados por OpenBCI para realizar un análisis en Python de las señales cerebrales, con el fin de observar los cambios que ocurren en ellas.

 
### *4.7.1. Lectura del EEG en reposo *  

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2e21654a-956a-4475-9a5d-179a4b67bda9"></video>|---
|  *Ploteo Python*  | *Descripción*|
|---|---|


### *4.7.2 Lectura del EEG en actividad de parpadeo

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/76c1d055-e03b-4ecc-bd0f-000118714b40"></video>|---
|  *Ploteo Python*  | *Descripción*|
|---|---|

### *4.7.3. Lectura del EEG  después de la actividad de parpadeo

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/e6355baa-eef5-45e3-bbf5-323ff6a1e495"></video>|---
|  *Ploteo Python*  | *Descripción*|
|---|---|

### 4.7.4. Lectura del EEG en actividad de lectura

|  *Video*  | *Foto*|
|:------------:|:---------------:|
|<video src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3c0022b9-2858-41f0-88e5-42a6a043d169"></video>|---
|  *Ploteo Python*  | *Descripción*|
|---|---|

## *5. Conclusiones* <a name="id12"></a>   


## *6. Bibliografía* <a name="id13"></a>
[1] PLUX – Wireless Biosignals, S.A., "BITalino (r)evolution Lab Guide: Experimental Guides to Meet & Learn Your Biosignals" OD.LB.04.05, Feb. 15, 2021.
[2] OpenBCI. "Mark IV — OpenBCI Headwear", OpenBCI Documentation. April 27, 2024
