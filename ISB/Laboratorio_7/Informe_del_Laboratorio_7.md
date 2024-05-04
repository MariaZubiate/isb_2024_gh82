

# Laboratorio 7
## Integrantes
- Christian Martin Mucha Huatuco
- Maria del Carmen Zubiate Castillo
- Jossef Caleb Tintaya Salva
- Gianni Atilio Di Trani Grández

# *Tabla de contenidos*

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Materiales y equipos](#id3)
4. [Metodologia](#id4)\
     4.1 [Generar filtro FIR e IIR para ECG](#id5)\
     4.2 [Generar filtro FIR e IIR para EMG](#id6)\
     4.3 [Generar filtro FIR e IIR para EEG](#id7) 
5. [Resultados](#id8)\
     5.1 [Resultado de señal filtrada con filtro FIR e IIR para ECG](#id9)\
     5.2 [Resultado de señal filtrada con filtro FIR e IIR para EMG](#id10)\
     5.3 [Resultado de señal filtrada con filtro FIR e IIR para EEG](#id11) 
7.  [Bibliografia](#id12)
   
## *1. Introducción* <a name="id1"></a>

## *2. Objetivos* <a name="id2"></a>
ECG:
- Diseñar 1 filtros IIR, deben elegir si es Bessel, Butterworth, Chebyshev o Eliptico. 
- Diseñar 1 filtros FIR, elegir 2 métodos de ventana pueden ser: Hanning, Hamming, Bartlett, rectangular o Blackman
  
EMG:
- Eliminar frecuencias altas que correspondan a ruido eléctrico y artefactos de movimiento
- Aislar la banda de frecuencia de interés que corresponde a la actividad muscular.
  
EEG
- Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas
cerebrales específicas.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Generar filtro FIR e IIR para ECG* <a name="id5"></a>

#### 4.1.1. Filtro IIR (Bessel, Butterworth, Chebyshev o Eliptico)

#### 4.1.1. Filtro FIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)


### *4.2. Generar filtro FIR e IIR para EMG* <a name="id6"></a>

#### 4.2.1. Filtro IIR (Bessel, Butterworth, Chebyshev o Eliptico)

#### 4.2.1. Filtro FIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)


### *4.3. Generar filtro FIR e IIR para EEG* <a name="id7"></a>

Debido a que las señales obtenidas en laboratorios anteriores no han sido procesadas, se infiere que estas no están limpias y contienen ruido. Por lo tanto, en este apartado se plantea la generación de un filtro FIR y un filtro IIR con el fin de eliminar este ruido. Para ello, utilizaremos el paper "Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing" como guía para definir las características de nuestros filtros.



#### 4.3.1. Filtro IIR 
Basándonos en la información proporcionada, las opciones de filtro que destacan como las mejores son el filtro Butterworth y el filtro Bessel. Estos filtros demostraron obtener buenos resultados en la Relación Señal-Ruido (SNR), con valores de 4.12 dB para 6 Hz, 4.01 dB para 8 Hz y 3.98 dB para 9 Hz, lo que indica una buena calidad de la señal en comparación con el ruido de fondo. Además, mostraron un Error Cuadrático Medio (MSE) bajo, con valores de 0.0028 para 6 Hz, 0.0027 para 8 Hz y 0.0026 para 9 Hz, lo que sugiere una capacidad efectiva para preservar la forma de onda original [1M]. Estas dos opciones de filtro sobresalen por su rendimiento general en la detección de Potenciales Evocados Visuales[1M].
Se utilizo las caracteristicas sugeridad en el informe:  Fc = 30 Hz, Wp = 94 rad/s, Ws = 157 rad/s.

#### 4.3.1. Filtro FIR 
Los resultados de esta investigación arrojaron que el filtro FIR pasa bajo con ventana Hamming y Hanning demostraron ser opciones favorables para el procesamiento de señales de EEG. En términos de parámetros de rendimiento, ambas técnicas han mostrado una reducción significativa en el Mean Square Error (MSE) y Mean Absolute Error (MAE), lo que indica una mayor precisión en la reconstrucción de la señal original. Específicamente, se observaron valores de MSE de 0.0035 y MAE de 0.0474 para la técnica de ventana Hamming con filtro de orden 4, mientras que para la técnica de ventana Hanning se registraron valores de MSE de 0.0036 y MAE de 0.0478 con filtro de orden 4. Lo que indica una mejora capacidad para minimizar los errores de reconstrucción de las señales EEG, respaldando la eliminiación de ruido[2M].
Se utilizo las caracteristicas sugeridad en el informe: Fc = 12 Hz, paso banda para ondas alfa

## *5. Resultados* <a name="id8"></a>

### *5.1. Resultado de señal filtrada con filtro FIR e IIR para ECG* <a name="id9"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|BASAL |              |             |              |
|RESPIRACIÓN |              |             |              |
|POST-EJERCICIO |              |             |              |


### *5.2. Resultado de señal filtrada con filtro FIR e IIR para EMG* <a name="id10"></a>

|  **Campo**  | **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|DESCANSO |              |             |              |
|CONTRACCIÓN LEVE |              |             |              |
|CONTRACCIÓN FUERTE |              |             |              |

### *5.3. Resultado de señal filtrada con filtro FIR e IIR para EEG* <a name="id11"></a>


|  **Campo**  | **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|REPOSO | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3cdcd4b2-5044-40db-901c-0ffc6681cdd5)|             |              |
|PARPADEO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/999f8e54-e518-4279-bcda-4034d63fa96e)|             |              |
|REPOSO DESPUES DEL PARPADEO|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5eb427eb-cc41-48f1-a77b-a583dc587240)|             |              |
|RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a92defc5-6f50-4fc3-a07d-b31dae541698)|             |              |



## *6. Bibliografia* <a name="id12"></a>



[1] “A-15 Dispositivos y Circuitos Electrónicos II Ingeniería Electrónica Filtros Activos.” Available: https://www.fceia.unr.edu.ar/dce2/Files/Apuntes/FILTROS ACTIVOS - Notas de Clase (v-2019-1).pdf

[1M] 
J. A. Montalvo-Aguilar, I. Bazán, and A. Ramírez-García, "Evaluación de técnicas de filtrado aplicadas a señales electroencefalográficas simuladas para la detección de Potenciales Evocados Visuales," Ciencias Naturales e Ingenierías, vol. 12, no. 25, doi: 10.21640/ns.v12i25.2374, Universidad Autónoma de Aguascalientes, Departamento de Ingeniería Biomédica, Aguascalientes.


[2M] Anshul, Dipali Bansal, Rashima Mahajan, "Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing" *International Journal of Innovative Technology and Exploring Engineering (IJITEE)*, vol. 8, no. 10, pp. 3573-3576, Aug. 2019. Available: https://www.researchgate.net/publication/335570147_Performance_Analysis_of_IIR_FIR_Windowing_Techniques_in_Electroencephalography_Signal_Processing
