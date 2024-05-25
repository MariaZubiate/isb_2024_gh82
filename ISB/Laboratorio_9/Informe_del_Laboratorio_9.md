
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

Llevaremos a cabo una comparación de 3 diferentes filtros que encontramos optimos en la busqueda de información que realizamos para la eliminación de ruido en señales EMG. El objetivo de este estudio es determinar cuál de estos filtros ofrece el mejor rendimiento en la eliminación de ruido de señales EMG con visualización de eliminación de ruido y analisis de señal ruido (SNR). 

### *4.1. Filtros para EMG* <a name="id5"></a>
En este inciso haremos una discusión de los 3 filtros a analizar. 

**1.Primer filtro**

En primera instancia usaremos la referencia ya usada en el trabajo anterior "Detección no invasiva de fatiga muscular de bajo nivel mediante EMG de superficie con descomposición wavelet" donde se determino que el filtro mas eficiente era la función Wavelet Sym8, debido a que con ello obtuvo un rendimiento superior a comparación de los demás Symmlets. Así como, en ello utilizaron 9 niveles de procesamiento, asi como se eliminaron los niveles 1,8 y 9 debido a la presencia de artefactos de baja frecuencia como artefactos de movimientos. quedandose solo con los niveles 2,3,4,5,6 y 7 [4]. 

Por lo que para nuestro primer filtro realizaremos:

1.Descomposición de 8 coeficientes.
2.Eliminación de coeficiente 1,8,9.
3.Reconstrucción de la señal filtrada. 


**2. Segundo filtro**

Para el segundo filtros utilizamos el articulo "Comparative study of wavelet denoising in myoelectric control applications", en el cual se investigó el uso de diferentes wavelets para la mejora de la calidad de la señal miográfica antes de su uso en diseños protésicos. En este estudio, se evaluaron varias funciones wavelet, y se encontró que la wavelet Daubechies (db4) era la más efectiva para la eliminación de ruido en señales EMG. En este articulo se utilizó un análisis de dominio de tiempo y frecuencia para evaluar la relación entre la contracción muscular y la señal, encontrando que durante las contracciones sostenidas, la frecuencia media (MNF) y la frecuencia mediana (MDF) aumentaban con los niveles de fuerza muscular[5].

Para nuestro segundo filtro, utilizaremos el Daubechies (db4). La implementación de este filtro seguirá este paso:

1. Descomposición de la señal utilizando las funciones wavelet db4.
2. Aplicación de métodos de umbral para la eliminación de ruido en los coeficientes descompuestos.
3. Reconstrucción de la señal utilizando los coeficientes modificados.

**3. Tercer filtro**

Para el ultimo filtro usaremos el articulo "Discrete wavelet transform analysis of surface electromyography for the
fatigue assessment of neck and shoulder muscles",se utilizó la transformada wavelet discreta (DWT) para evaluar la fatiga muscular en el cuello y los hombros bajo condiciones dinámicas repetitivas. Se probaron diez funciones wavelet comunes, y se encontró que la wavelet "Rbio3.1" era la más sensible a los cambios espectrales inducidos por la fatiga en la banda de frecuencia de 12–23 Hz. Se realizo el análisis DWT en datos SEMG recogidos durante 40 minutos de ejercicios repetitivos de brazos y cuello, descomponiendo la señal en siete niveles para analizar el poder en diferentes bandas de frecuencia[6]. 

Para el tercer filtro utilizaremos estos pasos:

1. Descomposición de la señal en 7 niveles utilizando Rbio3.1.
2. Reconstrucción de la señal utilizando los coeficientes de detalle seleccionados.
   
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

[4] G. Zhang, E. Morin, Y. Zhang, and S. Ali Etemad, “Non-invasive detection of low-level muscle fatigue using surface EMG with wavelet decomposition,” PubMed, Jul. 2018, doi: https://doi.org/10.1109/embc.2018.8513588. ‌

[5] T. Sharma and K. Veer, "Comparative study of wavelet denoising in myoelectric control applications," *Journal of Medical Engineering & Technology*, vol. 40, no. 3, pp. 80-86, 2016, doi: 10.3109/03091902.2016.1139200.

[6] S. K. Chowdhury, A. D. Nimbarte, M. Jaridi, and R. C. Creese, "Discrete wavelet transform analysis of surface electromyography for the fatigue assessment of neck and shoulder muscles," *Journal of Electromyography and Kinesiology*, vol. 23, no. 4, pp. 995-1003, 2013, doi: 10.1016/j.jelekin.2013.05.001.


[2M] https://github.com/pluxbiosignals/biosignalsnotebooks/blob/master/biosignalsnotebooks_notebooks/Categories/Extract/temporal_statistical_parameters.ipynb
