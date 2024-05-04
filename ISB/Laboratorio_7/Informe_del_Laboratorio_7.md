

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

Los filtros IIR existe filtros Butterworth, Chebyshev y Bessel los cuales son tipos de filtros con ventana que se utilizan en el diseño de circuitos electrónicos para filtrar señales. Cada uno de estos filtros tiene características únicas en términos de su respuesta en frecuencia y su comportamiento en el dominio del tiempo.

Butterworth:Se destacan por su respuesta en frecuencia maxima plana en la banda de paso. Tienen un comportamiento suave en el dominio del tiempo, sin distorsionar la forma de onda de la señal filtrada. Son útiles cuando se requiere una respuesta de frecuencia lo más plana posible dentro de la banda de paso, sin preocuparse demasiado por la transición a la banda de rechazo[1].

Chebyshev:Son conocidos por su capacidad para lograr una pendiente de atenuación más pronunciada que los Butterworth, introduciendo ripple (variaciones) en la banda de paso o en la banda de rechazo. Esto permite una ganancia de señal más rápida en la transición entre la banda de paso y la de rechazo, lo que es útil en aplicaciones que requieren alta selectividad en la respuesta en frecuencia[1].

Bessel: Se caracterizan por tener una fase casi lineal en la banda de paso, lo que significa que la señal filtrada experimenta menos distorsión en el dominio del tiempo. Aunque tienen una respuesta en frecuencia menos constante que los Butterworth y Chebyshev, ofrecen mejor linealidad de fase, siendo útiles en aplicaciones donde la transmisión de señales precisa en el tiempo es crítica. Son menos comunes, pero importantes en aplicaciones donde la distorsión temporal es una preocupación, como en la transmisión de datos de alta velocidad[1].


<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/da34a18d-4652-4f47-a116-0f726c7cd04c" alt="Nombre de la imagen" width="300"/>
</p>

<p align="center">
  <em>Fuente: Dispositivos y Circuitos Electrónicos II</em>
</p>





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
Basándonos en la información proporcionada, las opciones de filtro que destacan como las mejores son el filtro Butterworth y el filtro Bessel. Estos filtros demostraron obtener buenos resultados en la Relación Señal-Ruido (SNR), con valores de 4.12 dB para 6 Hz, 4.01 dB para 8 Hz y 3.98 dB para 9 Hz, lo que indica una buena calidad de la señal en comparación con el ruido de fondo. Además, mostraron un Error Cuadrático Medio (MSE) bajo, con valores de 0.0028 para 6 Hz, 0.0027 para 8 Hz y 0.0026 para 9 Hz, lo que sugiere una capacidad efectiva para preservar la forma de onda original[1M].
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



[1] Escuela de Ingeniería Electrónica, Universidad Nacional de Rosario, "Notas de Clase Filtros Activos," Dispositivos y Circuitos Electrónicos II, A-15, Edición 2018.1. Available: https://www.fceia.unr.edu.ar/dce2/Files/Apuntes/Notas%20de%20Clase%20Filtros%20Activos.pdf

[1M] 
J. A. Montalvo-Aguilar, I. Bazán, and A. Ramírez-García, "Evaluation of Filtering Techniques applied to simulated Electroencephalogram signals for Visual Evoked Potential Detection," Nova scientia, vol. 12, no. 25, pp. 1-14, Nov. 2020. Available: https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S2007-07052020000200112


[2M] Anshul, Dipali Bansal, Rashima Mahajan, "Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing" *International Journal of Innovative Technology and Exploring Engineering (IJITEE)*, vol. 8, no. 10, pp. 3573-3576, Aug. 2019. Available: https://www.researchgate.net/publication/335570147_Performance_Analysis_of_IIR_FIR_Windowing_Techniques_in_Electroencephalography_Signal_Processing
