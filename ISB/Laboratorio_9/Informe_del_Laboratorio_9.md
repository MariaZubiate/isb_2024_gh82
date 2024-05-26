
# Laboratorio 9
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
     4.1. [Filtros para EMG](#id5)\
     4.2. [Parametros estáticos y temporales para EMG](#id6)
6. [Resultados](#id7)\
     5.1 [Resultado de elección de filtro para EMG](#id8)\
     5.2 [Resultado de los parametros estáticos y temporales para EMG](#id9) 
8. [Conclusiones](#id10)
9. [Bibliografia](#id11)
   
## *1. Introducción* <a name="id1"></a>

La electromiografía (EMG) y la velocidad de conducción nerviosa son procedimientos fundamentales en el diagnóstico y seguimiento de patologías que afectan el sistema nervioso periférico en pacientes pediátricos. La Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos, elaborada por el Instituto Nacional de Salud del Niño – San Borja, proporciona un marco técnico estandarizado para la realización de estos estudios [1].

**Filtrado de Señales EMG con Transformada Wavelet**

Las señales EMG obtenidas necesitan ser filtradas para eliminar los ruidos presentes. Una técnica efectiva para esta tarea es el uso de la transformada Wavelet, que permite la eliminación de ruido y partes no deseadas de la señal EMG. Los filtros Wavelet se utilizan con una descomposición de niveles para separar las señales EMG en componentes de diferentes resoluciones. Mediante métodos de umbralización, se evalúa su efectividad en la reducción de ruido. Según el estudio "Wavelet packet based Denoising of EMG Signal", ambos métodos de umbralización (suave y duro) mejoraron significativamente la calidad de las señales EMG, manteniendo la integridad de la señal. Para evaluar el desempeño de estos filtros, se utilizaron medidas estadísticas como la media, desviación estándar y desviación media absoluta, alcanzando valores óptimos [2]. 

**Importancia de la Extracción de Parámetros EMG**

La extracción precisa de parámetros de las señales EMG es crucial para el desarrollo de sistemas inteligentes de biofeedback EMG, utilizados para monitorizar y mejorar la recuperación muscular en pacientes. Los parámetros extraídos, como la media, desviación estándar y desviación media absoluta, proporcionan información importante sobre la actividad muscular, facilitando diagnósticos más precisos y tratamientos personalizados. La investigación ha demostrado que estos parámetros extraídos de las señales EMG son vitales para el diseño de terapias de biofeedback eficientes y personalizadas [3].

## *2. Objetivos* <a name="id2"></a>

1. Elección del mejor filtro Wavelet para EMG
   
3. Segmentación de la señal.
   
5. Extracción de parámetros estáticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

Para comenzar, se realizó una búsqueda de 3 diferentes filtros que resultaron óptimos en diveros estudios para la eliminación de ruido en señales EMG. Cada estudio analizó un tipo de familia Wavelet en específica, las cuales fueron: Daubechies, Symmlet y Biortogonal. Estos 3 filtros se aplicaron para cada señal EMG obtenida en los laboratorios anteiores, siguiendo los parámetros que indicó cada estudio. 

Una vez obtenida las 3 señales filtradas, se analizaron 3 parámetros: relación señal-ruido (SNR), media cuadrática (RMS) y el error cuadrático medio (MSE); ya que estos 3 parámetros son los que usan los estudios revisados como  base de comparación para ver qué filtro es más eficiente. De acuerdo a los valores obtenidos por cada parámetro se concluirá qué filtro fue el mejor y con ello se realizará la extracción de parámetros estáticos y temporales de la señal.


### *4.1. Filtros para EMG* <a name="id5"></a>

Como se mencionó anteriormente, los filtros evaluados corresponden a las familias: Daubechies, Symmlet y Biortogonal. Para lo cual, a continuación se presenta una breve descripción de cada una de ellas.

*Wavelets Daubechies*

Son compactamente soportados, lo que significa que son no nulos solo en una región finita del dominio, proporcionando eficiencia computacional en la transformada wavelet de una señal. Una de sus características más destacadas es el alto número de momentos de anulación, lo que les permite capturar detalles finos y eliminar tendencias de baja frecuencia sin perder información crucial. Estas propiedades son esenciales para descomponer señales no estacionarias y con características transitorias, como las señales EMG. En el análisis de señales EMG, los wavelets Daubechies ofrecen una localización precisa en el dominio tiempo-frecuencia, importante para capturar y analizar componentes transitorias, como los potenciales de acción de unidades motoras (MUAPs). Además, la capacidad de estos wavelets para filtrar el ruido de alta frecuencia mientras se preservan las características importantes de la señal mejora la calidad de la descomposición y el análisis de la señal EMG, facilitando una interpretación precisa.

*Wavelets Symlets*

Al igual que los Daubechies, son compactamente soportados, proporcionando eficiencia en la descomposición de señales. Sin embargo, los Symlets se destacan por tener la menor asimetría posible y una fase casi lineal, lo que minimiza la distorsión de la señal durante la descomposición y la reconstrucción. Esta característica es especialmente importante en nuestro análisis de señales EMG, donde la preservación de la forma de la señal es crítica para el diagnóstico preciso de la actividad muscular y neuromuscular. La capacidad de los Symlets para manejar transitorios con mínima distorsión permite una descomposición precisa de componentes transitorias en las señales EMG, facilitando la identificación y el análisis de los MUAPs. 

*Wavelet Biortogonal Inverso*

Este wavelet mantiene la ortogonalidad durante las transformaciones, con una reconstrucción precisa de la señal original. Su diseño simétrico evita la distorsión de fase, lo cual es crucial para preservar las características transitorias de la señal EMG. Además, su soporte compacto facilita una buena localización temporal, y su número específico de momentos de anulación le permite filtrar el ruido de eficazmente y resaltar las características significativas de la señal. Este wavelet es especialmente efectivo para señales EMG debido a su capacidad para proporcionar una excelente localización en el dominio tiempo-frecuencia, para identificar rápidamente los cambios relacionados con la actividad muscular y la fatiga. 

En el apartado siguiente, se describe el tipo de filtro Wavelet ganador de cada estudio; así como las indicaciones que consideraron para su aplicación en la señal

**1.Primer filtro: De la familia Symlets**

Para este primer filtro, se utilizó el estudio "Non-invasive detection of low-level muscle fatigue using surface EMG with Wavelet decomposition", la cual basa su análisis en medir la fatiga muscular usando sEMG. Esta investigación menciona que el filtro que les resultó más eficiente fue la función Wavelet "Sym8", debido a que con ello obtuvo un rendimiento superior a comparación de los demás Symmlets. Para su aplicación, se menciona que se utilizaron 9 niveles de descomposición; de los cuales, para el procesamiento, se eliminaron los coeficientes de detalle 1, 8, 9 y el coeficiente de aproximación; debido a la presencia de artefactos de baja frecuencia como artefactos de movimientos. Finalmente, se obtiene el filtro y se reconstruye la señal[4]. 


**2. Segundo filtro: Daubechies Wavelets**

Para el segundo filtro, se utilizó la investigación titulada "Comparative study of wavelet denoising in myoelectric control applications", la cual analizó diferentes wavelets para la mejora de la calidad de la señal miográfica antes de su uso en diseños protésicos. De ello, se obtuvo que la función Wavelet más eficiente fue "db4". Para su aplicación, la señal se descompuso en 4 niveles y se aplicó umbral suave (threshold "soft") basada en la regla del Umbral Universal. Finalmente, se obtiene el filtro y se reconstruye la señal [5].


**3. Tercer filtro: Wavelet biortogonal inversa**

Para el último filtro se utilizó el articulo "Discrete wavelet transform analysis of surface electromyography for the fatigue assessment of neck and shoulder muscles", la cual compararon familias de Wavelet para evaluar la fatiga muscular en el cuello y los hombros bajo condiciones dinámicas repetitivas. Se probaron diez funciones Wavelet comunes, y se encontró que la wavelet "Rbio3.1" era la más sensible a los cambios espectrales inducidos por la fatiga. Para su aplicación, se usaron 7 niveles de descomposición y se eliminaron el coeficiente de aproximación y los coeficientes 5, 6 y 7. [6]. 

   
### *4.2. Parametros estáticos y temporales para EMG* <a name="id6"></a>

#### *Parametros estáticos*
##### *4.2.1. Mediana* 

La mediana representa el valor promedio de la señal [2M]. 
La mediana representa el valor central de la señal EMG y es útil para entender el nivel típico de actividad muscular sin verse afectada por valores atípicos extremos. En los experimentos de EMG, como los de lectura del músculo flexor del pulgar, bíceps del brazo y gemelo de la pantorrilla, la mediana permite comparar la actividad muscular en reposo, sin oposición y con oposición. Esto nos ayudará a identificar cambios en la actividad muscular de manera más estable ante la presencia de picos o artefactos en la señal. En la Imagen 1, se puede observar la formula a utilizar.

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/78aab2ca-8c90-4977-ad43-41f39ce31dcb" alt="Imagen1" >
</p>
<p align="center">
  Imagen 1. Fuente: Biosignalnotebook-github
</p>

##### *4.2.2. Varianza y desviación estandar*

La desviación estándar, siendo la raíz cuadrada de la varianza, proporciona una medida de dispersión en las mismas unidades que los datos originales. En los experimentos de EMG, estos parámetros ayudan a evaluar la consistencia de la señal y a detectar variaciones significativas en la actividad muscular. Por ejemplo, al comparar la desviación estándar de las señales en reposo y en actividad, se puede determinar la estabilidad y la variabilidad de la contracción muscular[2M]. En la Imagen 2, se puede observar la formula a utilizar.

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/65fa30e8-ee5d-40e9-8edc-a8180c363262" alt="Imagen2">
</p>

<p align="center">
  Imagen 2. Fuente: Biosignalnotebook-github
</p>

##### *4.2.3. Skewness*

Mide la asimetría de la distribución de los datos. Una distribución normal tiene un skewness de 0. Un valor positivo indica que la cola derecha de la distribución es más larga, mientras que un valor negativo indica una cola izquierda más larga. En nuestro estudio de señales EMG, este parámetro indicaría la presencia de picos o asimetrías en la señal, lo que nos ayudaría para identificar anomalías o patrones específicos de actividad muscular. Por ejemplo, un skewness positivo en las lecturas del bíceps del brazo durante la actividad con oposición puede sugerir una mayor intensidad de contracción en ciertos momentos[2M].

#### *Parámetros temporales*
##### *4.2.4. Estacionalidad*

La estacionalidad se refiere a patrones repetitivos o ciclos en una serie temporal. En los experimentos de EMG, la estacionalidad permite descomponer la señal en componentes de tendencia, estacionalidad y residuo. Esto es útil para analizar la periodicidad y los ciclos de contracción muscular. Por ejemplo, al estudiar la actividad del músculo gemelo de la pantorrilla durante diferentes movimientos, se pueden identificar patrones de activación muscular recurrentes que corresponden a ciclos específicos de movimiento.[2M].

##### *4.2.5. Relación señal-ruido (SNR)*

El SNR mide la relación entre la potencia de la señal y la potencia del ruido presente en la señal. Un SNR alto indica que la señal es mucho más fuerte que el ruido, mientras que un SNR bajo indica que la señal está dominada por el ruido. En los experimentos de EMG, un buen SNR es crucial para asegurar que las medidas de actividad muscular no están contaminadas por ruido externo. Evaluar el SNR en diferentes condiciones (reposo, sin oposición, con oposición) permite determinar la calidad de las grabaciones y la fiabilidad de los datos obtenidos. Un SNR alto en las lecturas del músculo flexor del pulgar, bíceps del brazo y gemelo de la pantorrilla asegura que los cambios observados en la actividad muscular son reales y no artefactos del ruido. En la Imagen 3, se puede observar la formula a utilizar [3M].

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/6441cf4d-8b51-434a-80e4-a923311d864f" alt="Imagen3">
</p>

<p align="center">
  Imagen 3. Fuente: Biosignalnotebook-github
</p>

## *5. Resultados* <a name="id7"></a>

### *5.1. Resultado de elección de filtro para EMG* <a name="id8"></a>

**REPOSO**

|  **Campo**  |  **Señal cruda** |
|:------------:|:---------------:|
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/efeb5453-7a5e-42ff-ad83-88d90a979384)|
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2e1bc986-80fc-4c95-8465-7e7922ffceaa)|
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d0d21558-571e-4aa8-8279-6a2344d19b15)|
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1c97c51d-d3a7-4dbd-a551-19423fb09b4d)|

La señal filtrada con Sym8 muestra una reducción significativa del ruido en comparación con la señal original. La línea naranja sigue de cerca la azul, preservando los picos y las características importantes de la señal. Esto indica que el filtro Sym8 es efectivo para mejorar la relación señal-ruido sin comprometer la integridad de la señal EMG.

La señal filtrada con Db4 muestra una reducción considerable del ruido en comparación con la señal original. Sin embargo, a diferencia del filtro Sym8, la señal filtrada con Db4 no sigue tan de cerca a la señal original, especialmente en los picos. Esto indica que, aunque el filtro Db4 reduce el ruido, puede introducir cierta distorsión y pérdida de detalles en la señal EMG.

La señal filtrada con Rbio3.1 sigue de cerca a la señal original, mostrando una buena reducción del ruido sin distorsionar significativamente los detalles de la señal EMG. Ambos picos y características de la señal original se preservan bien en la señal filtrada, indicando que el filtro Rbio3.1 es efectivo en mantener la integridad de la señal mientras reduce el ruido.

**FLEXIÓN**
|  **Campo**  |  **Señal cruda** |
|:------------:|:---------------:|
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0ef37aca-0736-4642-aa60-e14eb6cd1b4b)|
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2ae0bfe2-cf6b-4710-bbf4-bb8c59f98694)|
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5b7077ad-a84e-4803-890a-934f55b84d39)|
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9acac2d0-e9e6-42e7-8da3-45417fd7f046)|

La señal filtrada con Sym8 muestra una excelente correspondencia con la señal original, indicando una reducción significativa del ruido sin distorsionar la señal. Los picos y las características de la señal original se preservan bien en la señal filtrada, lo que demuestra la efectividad del filtro Sym8 para mantener la integridad de la señal EMG mientras reduce el ruido.

La señal filtrada con Db4 sigue de cerca a la señal original, mostrando una buena reducción del ruido. Los picos y valles de la señal EMG original se preservan bien en la señal filtrada, indicando que el filtro Db4 es eficaz en mantener la integridad de la señal mientras reduce el ruido. Sin embargo, al comparar con el filtro Sym8, Db4 no es tan efectivo en la preservación de los detalles finos de la señal EMG.

La señal filtrada con Rbio3.1 muestra una reducción del ruido, pero la señal filtrada parece más ruidosa en comparación con los otros filtros, como Sym8 y Db4. La línea naranja tiene una mayor dispersión alrededor de la línea azul, lo que indica que el filtro Rbio3.1 no es tan efectivo en la reducción de ruido y preservación de la señal EMG como los otros filtros evaluados.

**CONTRAFUERZA**
|  **Campo**  |  **Señal cruda** |
|:------------:|:---------------:|
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2c101981-8c7f-4d34-b5bb-d9b82e55ff3a)|
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c6172f33-5cef-4bb0-8710-fca36aa51bc4)|
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d46c8f39-f03f-4de0-9134-4bbf96d9c3ad)|
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/889ecfe7-46a2-40cb-8d8e-a1d6c9d879d1)|

La señal filtrada con Db4 sigue de cerca a la señal original, mostrando una buena reducción del ruido. Sin embargo, en las secciones de alta amplitud, la señal filtrada presenta mayor densidad de puntos, lo que puede indicar alguna distorsión o alteración leve en la señal. A pesar de esto, el filtro Db4 es efectivo en mantener la forma general de la señal EMG mientras reduce el ruido.

**Cuadro comparativo de SNR de los filtros**

Según [3M] un SNR mayor indica un mejor rendimiento del filtro para señales EMG.

|  **Filtro**  |  **SNR sym8** | **SNR db4** | **SNR Rbio3.1**|
|:------------:|:---------------:|:---------------: |:---------------:|
|REPOSO|6.42 dB |0.64 dB|0.93 dB|
|FLEXIÓN|17.15 dB|14.45 dB|3.32 dB|
|CONTRAFUERZA| 16.89 dB|23.22 dB |3.10 dB|


**Cuadro comparativo de MSE de los filtros**

Según [] el filtro es más optimo cuando el valor MSE es menor.

|  **Filtro**  |  **MSE sym8** | **MSE db4** | **MSE Rbio3.1**|
|:------------:|:---------------:|:---------------:|:------:|
|REPOSO|8.48|32.09|29.97|
|FLEXIÓN|17.15|14.45|3.32|
|CONTRAFUERZA| 16.89|23.22|3.10|

**Cuadro comparatido de RMS de los filtros**

Según [] el valor RMS es catalogado como uno de los mejores parámetros para analizar la señal EMG ya que refleja mejor el comportamiento del potencial de acción de la unidad motora durante una contracción muscular sostenida. Un menor valor indica que el filtro es más eficiente.

|  **Filtro**  |  **RMS sym8** | **RMS db4** | **RMS Rbio3.1**|
|:------------:|:---------------:|:---------------: |:---------------:|
|REPOSO|2.91|5.67|5.47|
|FLEXIÓN|17.15|14.45|3.32|
|CONTRAFUERZA| 16.89|23.22|3.10|

En el análisis de SNR comparado, el filtro Sym8 emerge como el mejor filtro en general, debido a su rendimiento consistente en todas las condiciones evaluadas. Muestra una SNR de 6,42 dB en reposo, 17,15 dB en flexión y 16,89 dB en contrafuerza, lo que indica una capacidad superior para reducir el ruido y preservar la señal útil en diversas situaciones. La simetría y ortogonalidad del filtro Sym8 contribuyen a su alta eficiencia en la descomposición y reconstrucción de señales, minimizando la distorsión y el ruido introducido. Este filtro es particularmente efectivo en el procesamiento de señales biológicas como las señales EMG, donde la preservación de la integridad de la señal es crucial para un análisis preciso. Además, su capacidad para mantener un alto SNR en múltiples condiciones lo hace especialmente adecuado para aplicaciones en las que se requiere un rendimiento uniforme y confiable. Aunque el filtro Db4 sobresale en condiciones de contrafuerza con una SNR de 23,22 dB, su desempeño es inferior en reposo y flexión comparado con Sym8, haciendo de Sym8 la opción más equilibrada y eficaz para aplicaciones variadas. El filtro Rbio3.1, con SNR de -0,11 dB en reposo, 3,32 dB en flexión y 3,10 dB en contrafuerza, demuestra ser menos eficiente en comparación, resaltando la superioridad del Sym8 en la reducción del ruido y la preservación de la señal en contextos de señales EMG.

### *5.2. Resultado de los parámetros estáticos y temporales para EMG* <a name="id9"></a>

Mediante codigo se hallaron diferentes parametros, los cuales nos permitiran obtener información importante de la señal:


   
|  **Parametro extraido*  |  **Media** |  **Desviación estandar** |  **Varianza** |  **Skewness**
|:------------:|:---------------:| :---------------:| :---------------:| :---------------:|
|REPOSO|-0.19199107348635788  | 5.357137450241598 |28.698921660781043| 0.3716207674774262
|FLEXIÓN|1.0932361025490807 | 80.4462510415022|  6471.599306632392|-1.6457947782683293
|CONTRAFUERZA| 0.8392194236304191|520.4572344851734| 270875.7329279549| -0.4936373536410914







## *6. Conclusiones* <a name="id10"></a>



## *7. Bibliografia* <a name="id11"></a>

[1] Instituto Nacional de Salud del Niño – San Borja. "Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos." Fecha: Octubre 2020. Código: GP-001/INSNSB/UAIE/SUAIEPSE – Neurología Pediátrica V01. Página 1-39.

[2] Akash Kumar Bhoi, Jitendra Singh Tamang, Purnendu Mishra, "Wavelet packet based Denoising of EMG Signal," International Journal of Engineering Research and Development, 2012.

[3]S. Im, S. Rho, "Extraction of parameters from EMG signals for the biofeedback electrical stimulation," in Proceedings of the 2005 IEEE Engineering in Medicine and Biology Society Annual Conference (EMBC), Shanghai, China, Sep. 2005, pp. 2157-2160. DOI: 10.1109/IEMBS.2005.1616926.

[4] G. Zhang, E. Morin, Y. Zhang, and S. Ali Etemad, “Non-invasive detection of low-level muscle fatigue using surface EMG with wavelet decomposition,” PubMed, Jul. 2018, doi: https://doi.org/10.1109/embc.2018.8513588. ‌

[5] T. Sharma and K. Veer, "Comparative study of wavelet denoising in myoelectric control applications," *Journal of Medical Engineering & Technology*, vol. 40, no. 3, pp. 80-86, 2016, doi: 10.3109/03091902.2016.1139200.

[6] S. K. Chowdhury, A. D. Nimbarte, M. Jaridi, and R. C. Creese, "Discrete wavelet transform analysis of surface electromyography for the fatigue assessment of neck and shoulder muscles," *Journal of Electromyography and Kinesiology*, vol. 23, no. 4, pp. 995-1003, 2013, doi: 10.1016/j.jelekin.2013.05.001.

[2M]"temporal_statistical_parameters". [En línea]. Disponible en: http://notebooks.pluxbiosignals.com/notebooks/Categories/Extract/temporal_statistical_parameters_rev.html

[3M] "snr_slow_signals". [En línea]. Disponible en: http://notebooks.pluxbiosignals.com/notebooks/Categories/Pre-Process/snr_slow_signals_rev.html
