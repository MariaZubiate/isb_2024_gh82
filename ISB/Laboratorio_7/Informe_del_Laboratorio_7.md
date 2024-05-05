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
6. [Conclusiones](#id12)
7.  [Bibliografia](#id13)
   
## *1. Introducción* <a name="id1"></a>


Los filtros digitales (FD) son sistemas que discriminan características de señales de entrada, permitiendo pasar ciertas frecuencias y suprimiendo otras. Realizan funciones similares a los filtros analógicos (FA) pero operan en señales digitales mediante algoritmos matemáticos. Pueden separar señales combinadas, restaurar señales distorsionadas, extraer información de interés y eliminar ruido no deseado. Los FD tienen ventajas como la programabilidad de sus respuestas en frecuencia, la linealidad de fase y una mayor precisión debido a la tolerancia de los circuitos digitales[1]. 

Entre los filtros IIR existe filtros Butterworth, Chebyshev y Bessel los cuales son tipos de filtros con ventana que se utilizan en el diseño de circuitos electrónicos para filtrar señales. Cada uno de estos filtros tiene características únicas en términos de su respuesta en frecuencia y su comportamiento en el dominio del tiempo.

Butterworth:Se destacan por su respuesta en frecuencia maxima plana en la banda de paso. Tienen un comportamiento suave en el dominio del tiempo, sin distorsionar la forma de onda de la señal filtrada. Son útiles cuando se requiere una respuesta de frecuencia lo más plana posible dentro de la banda de paso, sin preocuparse demasiado por la transición a la banda de rechazo[2].

Chebyshev:Son conocidos por su capacidad para lograr una pendiente de atenuación más pronunciada que los Butterworth, introduciendo ripple (variaciones) en la banda de paso o en la banda de rechazo. Esto permite una ganancia de señal más rápida en la transición entre la banda de paso y la de rechazo, lo que es útil en aplicaciones que requieren alta selectividad en la respuesta en frecuencia[2].

Bessel: Se caracterizan por tener una fase casi lineal en la banda de paso, lo que significa que la señal filtrada experimenta menos distorsión en el dominio del tiempo. Aunque tienen una respuesta en frecuencia menos constante que los Butterworth y Chebyshev, ofrecen mejor linealidad de fase, siendo útiles en aplicaciones donde la transmisión de señales precisa en el tiempo es crítica. Son menos comunes, pero importantes en aplicaciones donde la distorsión temporal es una preocupación, como en la transmisión de datos de alta velocidad[2].


<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/da34a18d-4652-4f47-a116-0f726c7cd04c" alt="Nombre de la imagen" width="300"/>
</p>

<p align="center">
  <em>Fuente: Dispositivos y Circuitos Electrónicos II</em>
</p>

En el diseño de filtros FIR, se utilizan diferentes tipos de ventanas para dar forma a la respuesta en frecuencia y controlar los lóbulos laterales

Rectangular: también conocida como ventana Bartlett, es la más simple de todas las ventanas utilizadas en el diseño de filtros FIR. Su respuesta en frecuencia tiene lóbulos laterales altos y una transición abrupta entre la banda de paso y la de paro. Esto la hace menos adecuada para aplicaciones que requieren una alta selectividad en la respuesta del filtro[3].

Hanning: Proporciona una transición más suave y lóbulos laterales más bajos que la ventana rectangular. Su forma de coseno la hace ideal para aplicaciones donde se necesita una buena supresión de lóbulos laterales y una respuesta en frecuencia más suave[3].

Hamming: Mejora aún más la supresión de lóbulos laterales con respecto a la ventana Hanning. Tiene una respuesta en frecuencia más ajustada y ofrece una transición más suave entre la banda de paso y la de paro. Esto la hace adecuada para aplicaciones que requieren un mejor rendimiento en la atenuación de frecuencias no deseadas[3].

Blackman: Ofrece una transición extremadamente suave y lóbulos laterales mínimos debido a su forma compuesta por varios términos coseno. Esto la convierte en una opción excelente para aplicaciones que requieren una alta selectividad y una buena supresión de lóbulos laterales, aunque a costa de una respuesta en frecuencia más ancha[3].

| Rectangular |	Hanning |	Hamming |	Blackman |
|:------------:|:---------------:|:------------:| :------------:| 
| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/bb0ed578-31ee-4bda-997a-19673836aa27) |  ![Imagen de WhatsApp 2024-05-04 a las 20 40 23_3f812909](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/80df702e-a0b6-466a-bd0b-dbaaf9ad21db)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cbed5a8e-b976-4d46-a45f-4bced38d78e6)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/cd4dfa46-6dcb-419c-b706-eddd3b31b9ea) | 
<p align="center">
  <em>Fuente: Digital Signal Processing. Principles, Algorithms, and Applications</em>
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
Se utilizó un filtro Butterworth pasa bajas de orden 60 y con una frecuencia de corte de 100 Hz [4].


#### 4.1.1. Filtro FIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)


### *4.2. Generar filtro FIR e IIR para EMG* <a name="id6"></a>

#### 4.2.1. Filtro IIR (Bessel, Butterworth, Chebyshev o Eliptico)
En el espectro de la señal, se vio que el único pico bien pronunciado para eliminar fue a una frecuencia de 50Hz. Entre los diferentes tipos de filtro, lo que al autor le resultó útil fue usa el filtro Butterworth de orden 2 con una frecuencia de bloqueo entre 49 y 51, con lo cual se logró perder la mínima información alrededor de la frecuencia a eliminar; manteniendo un contenido espectral bien definido en cada periodo corto de tiempo. [] A ello, cabe resaltar que según nuestro contexto, la frecuencia a eliminar no estaría en 50Hz, sino en 60Hz; esto debido a la interferencia de la toma local.
#### 4.2.1. Filtro FIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)
Se realizó un comparación de filtrado de señal EMG con 3 tipos de ventanas: Hamming, Hanning y Rectangular. Para lo cual, se evaluaron 4 parámetros a tener en cuenta en la comparación: relación potencia/potencia media, potencia promedio, relación señal-ruido (SNR) y relación de rechazo EMG. Y como resultado se observó que la ventana Rectangular es más informativa en comparación que las otras 2 ventanas, pues no elimina los picos existentes en la contracción muscular. Es decir, para el autor le resultó que la ventana rectangular es la técnica de ventana más adecuada, ya que brinda mejores parámetros para el análisis de la señal EMG durante cada actividad de movimiento.

### *4.3. Generar filtro FIR e IIR para EEG* <a name="id7"></a>

Debido a que las señales obtenidas en laboratorios anteriores no han sido procesadas, se infiere que estas no están limpias y contienen ruido. Por lo tanto, en este apartado se plantea la generación de un filtro FIR y un filtro IIR con el fin de eliminar este ruido. Para ello, utilizaremos los papres "Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing" y "Evaluation of Filtering Techniques applied to simulated Electroencephalogram signals for Visual Evoked Potential Detection" como guía para definir las características de nuestros filtros[1M-2M].



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
|BASAL | ![descarga (20)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/81677ad1-ccd6-474e-ac63-8acddc17fd10)|           |         |
|FFTS EN BASAL |       |         |         |
|RESPIRACIÓN |  ![descarga (21)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6b3fdf15-fe55-4830-8dbb-57ee7cc6ec86) |             |           |
|FFTS PARA RESPIRACIÓN |     |     |     |
|POST-EJERCICIO |   ![descarga (22)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/c54ed6a5-9a23-49a8-8e1f-0956ad76132e)  |           |             |
|FFTS POST-EJERCICIO |     |     |     |
|RESPIRACIÓN PROFUNDA POST-EJERCICIO |   ![descarga (23)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/a684930a-f559-4256-8099-b2e4764da05a)  |           |             |
|FFTS RESPIRACIÓN PROFUNDA POST-EJERCICIO |     |     |     |

### *5.2. Resultado de señal filtrada con filtro FIR e IIR para EMG* <a name="id10"></a>

|**Señal Cruda_REPOSO** |**FFT de la señal** |
|:------------:|:---------------:|
|![Captura de pantalla 2024-05-04 163706](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/161761df-f746-4a7b-be6a-45a583bf073a)|![Captura de pantalla 2024-05-04 165546](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/083e4128-2e7f-45eb-a885-aa00f8c2def3)|
|Filtro FIR |Señal filtrada con FIR|
![Captura de pantalla 2024-05-04 170847](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/39ed067e-7262-4786-9d1a-5c39e2b28fbb)|![Captura de pantalla 2024-05-04 171503](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/54603528-8512-4696-adf8-cf15c7afce00)|
|Filtro IIR |Señal filtrada con IIR|
|![Captura de pantalla 2024-05-04 172149](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/702ba510-c821-495b-b852-1d73fab1b505)|![Captura de pantalla 2024-05-04 171907](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/14b06633-c62a-4928-a731-eee2a61daa35)|


|**FLEXIÓN** |**Ploteo en Python** |
|:------------:|:---------------:|
|Señal original|![Captura de pantalla 2024-05-04 172935](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e1116ccf-37ba-4d18-b726-19fdd4f948d5)|
|FFT de la señal|![Captura de pantalla 2024-05-04 173201](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/085fd781-2ce0-4b6f-a08e-b05a43a87e14)|
|Señal filtrada con FIR| |
|Señal filtrada con IIR| |

|**CONTRAFUERZA** |**Ploteo en Python** |
|:------------:|:---------------:|
|Señal original|![Captura de pantalla 2024-05-04 225121](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/b90adc10-e045-42c7-98aa-5fa5b1111199)|
|FFT de la señal|![Captura de pantalla 2024-05-04 225256](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0ab9aa19-2850-4731-8d84-6080f9511dc7)|
|Señal filtrada con FIR|![Captura de pantalla 2024-05-04 230728](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/fea6a1da-ea1f-43aa-afbf-6136fb5d7855)|
|Señal filtrada con IIR|![Captura de pantalla 2024-05-04 231009](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c5dafc10-c211-4c23-b8a5-210222a2c71a)|


### *5.3. Resultado de señal filtrada con filtro FIR e IIR para EEG* <a name="id11"></a>


|  **Campo**  | **Señal cruda** | **Señal filtrada con IIR(naranja) superpuesta sobre la señal cruda** |  **Señal filtrada con FIR(naranja) superpuesta sobre la señal cruda** |
|:------------:|:---------------:|:------------:| :------------:|
|REPOSO | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3cdcd4b2-5044-40db-901c-0ffc6681cdd5)|![descarga](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6f5ad075-60fc-4ae2-a6d7-2dafbce121af) |      ![Captura de pantalla 2024-05-04 193639](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/abf1fcbf-83d8-42f6-b5f0-001fc2533a52)|
|FFTS DEL REPOSO |![descarga (4)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/69ad7621-c340-4797-9c4e-3596f8ef7a5b)|  ![descarga (12)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/a825d86c-dab1-484f-87f6-4fcc1b52c3a9)|   ![descarga (16)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/56ecde57-3653-4b20-b162-5172dbcfd632)|
|PARPADEO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/999f8e54-e518-4279-bcda-4034d63fa96e)|   ![descarga (1)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/f7ba6559-cde9-438a-98b6-c11fce5cb00e) |    ![Captura de pantalla 2024-05-04 193725](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/7512807c-74a8-4a4f-80a5-9329d18b5d09)  |
|FFTS DEL PARPADEO |![descarga (5)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/579bde96-5db5-47f2-b4e8-d88fe0843fd7)| ![descarga (13)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/fcd539d7-dba2-4ad2-978e-3c5256bc8373)|  ![descarga (17)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/648b899e-cb83-4cea-8280-3a2161987865) |
|REPOSO DESPUES DEL PARPADEO|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5eb427eb-cc41-48f1-a77b-a583dc587240)| ![descarga (2)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/71ecdc73-53bf-4c41-94eb-1b9ed72f1e15) |       ![Captura de pantalla 2024-05-04 193756](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/0bd11465-8ddb-4ca5-b6fd-474247c94244)|
|FFTS DEL REPOSO DESPUES DEL PARPADEO | ![descarga (6)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/8228f968-755c-44a7-9725-532f70311187) |  ![descarga (14)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6109c209-b5e3-4e2d-aa50-9c9739745faa)|  ![descarga (18)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/3faca185-e3bc-450d-9453-3110d95fe669)|
|RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a92defc5-6f50-4fc3-a07d-b31dae541698)|  ![descarga (3)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/b8d92eeb-bc5e-4147-8b27-49388ff4639a) |      ![Captura de pantalla 2024-05-04 193831](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/f08bb593-3a59-4031-8936-e850d785e95b)|
|FFTS DE LA RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS | ![descarga (7)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/0552020e-a55e-47d9-9b1e-e872b3216ac1)|  ![descarga (15)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/028e1d14-ab7c-4c1c-bf82-8edb3beb8875)| ![descarga (19)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/c19536f5-7fe0-4f67-8dd8-5ee27f3eb90b)|


## *6. Conclusiones* <a name="id12"></a>
## *7. Bibliografia* <a name="id13"></a>

[1] Larry H. Escobar s. Facultad de Ingenieria, UNAM, "Diseño de filtros digitales". Available: https://odin.fi-b.unam.mx/labdsp/files/libros/filtros.pdf

[2] Escuela de Ingeniería Electrónica, Universidad Nacional de Rosario, "Notas de Clase Filtros Activos," Dispositivos y Circuitos Electrónicos II, A-15, Edición 2018.1. Available: https://www.fceia.unr.edu.ar/dce2/Files/Apuntes/Notas%20de%20Clase%20Filtros%20Activos.pdf

[3] J. G. Proakis and D. G. Manolakis, "Digital Signal Processing: Principles, Algorithms, and Applications," 3rd ed. Upper Saddle River, NJ, USA: Prentice-Hall International, 1996. Available: https://uvceee.wordpress.com/wp-content/uploads/2016/09/digital_signal_processing_principles_algorithms_and_applications_third_edition.pdf

[4] H. Amhia y A. K. Wadhwani, «Stability and Phase Response Analysis of Optimum Reduced-Order IIR Filter Designs for ECG R-Peak Detection», J Healthc Eng, vol. 2022, p. 9899899, abr. 2022, doi: 10.1155/2022/9899899.
#### 4.1.1. Filtro IIR (Bessel, Butterworth, Chebyshev o Eliptico)

[1M] 
J. A. Montalvo-Aguilar, I. Bazán, and A. Ramírez-García, "Evaluation of Filtering Techniques applied to simulated Electroencephalogram signals for Visual Evoked Potential Detection," Nova scientia, vol. 12, no. 25, pp. 1-14, Nov. 2020. Available: https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S2007-07052020000200112


[2M] Anshul, Dipali Bansal, Rashima Mahajan, "Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing" *International Journal of Innovative Technology and Exploring Engineering (IJITEE)*, vol. 8, no. 10, pp. 3573-3576, Aug. 2019. Available: https://www.researchgate.net/publication/335570147_Performance_Analysis_of_IIR_FIR_Windowing_Techniques_in_Electroencephalography_Signal_Processing
