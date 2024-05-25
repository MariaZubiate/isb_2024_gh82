
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
     4.1. [Parametros estaticos y temporales para EMG](#id6)
6. [Resultados](#id7)\
     5.1 [Resultado de elección de filtro para EMG](#id8)\
     5.1 [Resultado de los parametros estaticos y temporales para EMG](#id9) 
8. [Conclusiones](#id10)
9. [Bibliografia](#id11)
   
## *1. Introducción* <a name="id1"></a>

La electromiografía (EMG) y la velocidad de conducción nerviosa son procedimientos fundamentales en el diagnóstico y seguimiento de patologías que afectan el sistema nervioso periférico en pacientes pediátricos. La Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos, elaborada por el Instituto Nacional de Salud del Niño – San Borja, proporciona un marco técnico estandarizado para la realización de estos estudios[1].

**Filtrado de Señales EMG con Transformada Wavelet**

Las señales EMG obtenidas necesitan ser filtradas para eliminar los ruidos presentes. Una técnica efectiva para esta tarea es el uso de la transformada Wavelet, que permite la eliminación de ruido y partes no deseadas de la señal EMG. Los filtros Wavelet se utilizan con una descomposición de niveles para separar las señales EMG en componentes de diferentes resoluciones. Mediante métodos de umbralización, se evalúa su efectividad en la reducción de ruido. Según el estudio "Wavelet packet based Denoising of EMG Signal", ambos métodos de umbralización (suave y duro) mejoraron significativamente la calidad de las señales EMG, manteniendo la integridad de la señal. Para evaluar el desempeño de estos filtros, se utilizaron medidas estadísticas como la media, desviación estándar y desviación media absoluta, alcanzando valores óptimos[2]. 

**Importancia de la Extracción de Parámetros EMG**

La extracción precisa de parámetros de las señales EMG es crucial para el desarrollo de sistemas inteligentes de biofeedback EMG, utilizados para monitorizar y mejorar la recuperación muscular en pacientes. Los parámetros extraídos, como la media, desviación estándar y desviación media absoluta, proporcionan información importante sobre la actividad muscular, facilitando diagnósticos más precisos y tratamientos personalizados. La investigación ha demostrado que estos parámetros extraídos de las señales EMG son vitales para el diseño de terapias de biofeedback eficientes y personalizadas[3].

## *2. Objetivos* <a name="id2"></a>

1. Elección del mejor filtro Wavelet para EMG 
2. Segmentación de la señal.
3. Extracción de parametros estaticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Filtros para EMG* <a name="id5"></a>
En el último laboratorio presentado, utlizamos como referencia el trabajo de G. Zhang et al con la aplicación del filtrado wavelet tipo Symlet 8 con resultados buenos para el filtrado de ruido no óptimos en términos de [falta completar]. Ahora guiándonos del artículo "EMG Signal Analysis By Using Various Wavelet And A Comparative Study" por S. Ahmed & S. Mahboob, levaremos a cabo una comparación de diferentes tipos de wavelets daubechies, symlets y coiflets. El objetivo de este estudio es determinar cuál de estos filtros ofrece el mejor rendimiento en la eliminación de ruido de señales EMG y, sobre todo, la mejor localización de energía. Para este laboratorio, hemos seleccionado tres de los filtros wavelet evaluados en el artículo mencionado, los cuales serán sometidos a un análisis detallado para evaluar su efectividad. [1M]
Hemos seleccionado tres de los filtros wavelet evaluados en el artículo: Daubechies (db4), Symlets (sym4) y Coiflets (coif5).


### *4.2. Parametros estaticos y temporales para EMG* <a name="id6"></a>

#### *Parametros estaticos*
##### *4.2.1. Mediana* 

La mediana es el valor que separa la mitad superior e inferior en un conjunto de datos ordenados. Es una medida robusta de tendencia central y es menos sensible a los valores atípicos comparado con la media. En la Imagen 1, se puede observar la formula a utilizar.

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/58bd089d-6d9d-4b84-8e81-7b8ee8c7980f" alt="Imagen1">
</p>
<p align="center">
  Imagen1. Fuente: Biosignalnotebook-github
</p>

##### *4.2.2. Varianza y desviación estandar*

Varianza: Mide la dispersión de los datos respecto a la media. Indica cuánto varían los datos en torno a su valor promedio.

Desviación Estándar: Es la raíz cuadrada de la varianza, proporcionando una medida de dispersión en las mismas unidades que los datos originales[2M]. En la Imagen 2, se puede observar la formula a utilizar.

### Imagen2. Fuente: Biosignalnotebook-github

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/65fa30e8-ee5d-40e9-8edc-a8180c363262" alt="Imagen2">
</p>

<p align="center">
  Imagen2. Fuente: Biosignalnotebook-github
</p>

##### *4.2.3. Skewness and kurtosis*

Skewness: Mide la asimetría de la distribución de los datos. Un valor positivo indica que la cola derecha de la distribución es más larga, mientras que un valor negativo indica una cola izquierda más larga[2M].

Kurtosis: Mide la forma de la distribución, especialmente el "apuntalamiento". Una alta kurtosis indica una distribución con picos más pronunciados y colas más gruesas, lo que sugiere la presencia de valores atípicos[2M].

#### *Parametros temporales*
##### *4.2.4. Estacionalidad* 

La estacionalidad se refiere a patrones repetitivos o ciclos que ocurren a intervalos regulares en una serie temporal. La descomposición estacional permite dividir la serie temporal en componentes de tendencia, estacionalidad y residuo[2M].

## *5. Resultados* <a name="id7"></a>

### *5.1. Resultado de elección de filtro para EMG* <a name="id8"></a>


|  **Campo**  |  **Señal cruda** | **Señal filtrada 1** |  **Señal filtrada 2** |  **Señal filtrada 3** | 
|:------------:|:---------------:|:------------:| :------------:| :------------:|
|REPOSO |------|-------|-------|-------
|FFTS EN REPOSO |------|-------|-------|-------
|FLEXIÓN |------|-------|-------|-------
|FFTS PARA FLEXIÓN |------|-------|-------|-------
|CONTRAFUERZA |------|-------|-------|-------
|FFTS CONTRAFUERZA |------|-------|-------|-------

**Análisis descriptivo:**



### *5.2. Resultado de los parametros estaticos y temporales para EMG* <a name="id9"></a>






**Análisis descriptivo:**





## *6. Conclusiones* <a name="id10"></a>



## *7. Bibliografia* <a name="id11"></a>

[1] Instituto Nacional de Salud del Niño – San Borja. "Guía de Procedimiento de Electromiografía y Velocidad de Conducción de Nervios Periféricos." Fecha: Octubre 2020. Código: GP-001/INSNSB/UAIE/SUAIEPSE – Neurología Pediátrica V01. Página 1-39.

[2] Akash Kumar Bhoi, Jitendra Singh Tamang, Purnendu Mishra, "Wavelet packet based Denoising of EMG Signal," International Journal of Engineering Research and Development, 2012.

[3]S. Im, S. Rho, "Extraction of parameters from EMG signals for the biofeedback electrical stimulation," in Proceedings of the 2005 IEEE Engineering in Medicine and Biology Society Annual Conference (EMBC), Shanghai, China, Sep. 2005, pp. 2157-2160. DOI: 10.1109/IEMBS.2005.1616926.

[1M]Saleh Ahmed, Mahboob Qaosar, Dr. Shamim Ahmad. "EMG Signal Analysis By Using Various Wavelet And A Comparative Study." Journal of Multidisciplinary Engineering Science and Technology (JMEST). 2019.
[2M] https://github.com/pluxbiosignals/biosignalsnotebooks/blob/master/biosignalsnotebooks_notebooks/Categories/Extract/temporal_statistical_parameters.ipynb
