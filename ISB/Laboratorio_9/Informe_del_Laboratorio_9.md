
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


## *2. Objetivos* <a name="id2"></a>

1. Eleccion del mejor filtro Wavelet para EMG (SNS, visualización, perdida de información).
2. Segmentación de la señal.
3. Extracción de parametros estaticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Filtros para EMG* <a name="id5"></a>
Usando el artículo "EMG Signal Analysis By Using Various Wavelet And A Comparative Study" como referencia, llevaremos a cabo una comparación de diferentes tipos de wavelets. El objetivo de este estudio es determinar cuál de estos filtros ofrece el mejor rendimiento en la eliminación de ruido de señales EMG. Para este laboratorio, hemos seleccionado tres de los filtros wavelet evaluados en el artículo mencionado, los cuales serán sometidos a un análisis detallado para evaluar su efectividad. [1M]
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
##### *4.2.4. Estacionalidad 

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

[1M]Saleh Ahmed, Mahboob Qaosar, Dr. Shamim Ahmad. "EMG Signal Analysis By Using Various Wavelet And A Comparative Study." Journal of Multidisciplinary Engineering Science and Technology (JMEST). 2019.
[2M] https://github.com/pluxbiosignals/biosignalsnotebooks/blob/master/biosignalsnotebooks_notebooks/Categories/Extract/temporal_statistical_parameters.ipynb
