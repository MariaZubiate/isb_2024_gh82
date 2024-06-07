
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
4. [Metodologia](#id4)\
     4.1 [Generar filtro para ECG](#id5)\
     4.2 [Obtener caracteristicas de ECG](#id6)
6. [Resultados](#id7)\
     5.1 [Resultado de señal filtrada](#id8)\
     5.2 [Resultado de caracteristicas de ECG](#id9)
8. [Conclusiones](#id10)
9. [Bibliografia](#id11)
   
## *1. Introducción* <a name="id1"></a>

El electrocardiograma (ECG) es una herramienta de diagnóstico utilizada para medir la actividad del corazón. Consiste en colocar electrodos en partes específicas del cuerpo, las cuales tienen contacto con la piel. Estos detectan impulsos eléctricos generados por el corazón. Esta información se registra como ondas en un gráfico.
La señal ECG contiene diferentes componentes, entre ellos esta la onda P, el complejo QRS y la onda T; los cuales representan la despolarización auricular, despolarización ventricular y repolarización ventricular, respectivamente.
El ECG posee 12 derivadas, las cuales permiten visualizar el corazón desde diferentes ángulos. Estas derivaciones se pueden utilizar para detectar attirmias y transtornos cardíacos. Entre las derivaciones tenemos: derivaciones bipolares(I,II,III), derivaciones unipolares(aVR, aVL,aVF) y derivaciones precordiales(V1-V6)[1].


Luego de que las señales ECG sean leídas, se procederá a eliminar el ruido y los artefactos que interfieren en la señal. Para ello, se utilizan filtros que se encargan de reducir el ruido y proporcionar una lectura de señal más limpia. Entre estos filtros, los filtros Wavelet son especialmente eficaces y se dividen en varias familias: Daubechies (db), Symlet (sym), Coiflet (coif), Biorthogonal (bior) y Reverse Biorthogonal (rbio), cada una con características particulares. Las wavelets Daubechies son conocidas por su compacidad y ortogonalidad, mientras que las Symlet son una versión más simétrica de las Daubechies. Las Coiflet son útiles para analizar señales con variaciones lentas, y las Biorthogonal permiten una reconstrucción perfecta de las señales utilizando diferentes filtros para análisis y síntesis. Las Reverse Biorthogonal, similares a las Biorthogonal pero con filtros invertidos, también permiten una reconstrucción precisa. Estas características hacen que los filtros Wavelet sean muy eficaces para la eliminación de ruido en las señales ECG, mejorando significativamente la precisión y la calidad del análisis de estas señales[2].

La variabilidad de la frecuencia cardíaca (HRV) es una medida de las fluctuaciones en los intervalos entre latidos consecutivos del corazón, conocida como intervalos RR. Este análisis es fundamental para evaluar la actividad del sistema nervioso autónomo y el estado de salud cardiovascular. Los picos de la onda R en los electrocardiogramas (ECG) son cruciales para identificar estos intervalos RR. Mediante algoritmos como el de Pan-Tompkins, se pueden detectar con precisión los picos R, lo que permite calcular los intervalos entre latidos y realizar un análisis detallado de HRV [3]. 

## *2. Objetivos* <a name="id2"></a>

1. Elección del mejor filtro Wavelet para ECG
2. Segmentación de la señal.
3. Extracción de parámetros estáticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

En este laboratorio, nos enfocaremos en la detección de los picos R en señales de electrocardiograma (ECG) y en el análisis de la variabilidad de la frecuencia cardíaca (HRV).

### *4.1. Generar filtro* <a name="id5"></a>

Emplearemos un filtro pasa banda que consiste en un filtro pasa bajo seguido de un filtro pasa alto para eliminar el ruido y las interferencias. Este filtro recursivo de tiempo real, diseñado con coeficientes enteros, tiene polos situados para cancelar ceros en el círculo unitario del plano z. Para nuestro diseño, tomamos como referencia el artículo "A Real-Time QRS Detection Algorithm"[4] y el codigo proporcionado en clase.


### *4.2.Obtener caracteristicas de ECG* <a name="id6"></a>

**4.2.1. Obtener los picos R**

Para identificar las ondas R de nuestr señal, se utilizó el algoritmo de Pan-Tompkins, que incluye varios pasos: aplicar un filtro pasabanda,diferenciación, cuadratura de muestras, suavizado con un filtro de media móvil, y análisis de correlación y umbralización. Los umbrales necesarios para detectar los picos se determinaron a partir de los valores máximos y promedios de los picos identificados durante la fase de entrenamiento. Finalmente, se reconocieron como picos R aquellos que superaban estos umbrales, marcando así los puntos en la señal original [3].

- Filtro Pasabanda: Se aplicó un filtro pasabanda para eliminar el ruido de alta frecuencia y las variaciones lentas en la línea de base, manteniendo únicamente las frecuencias relevantes para la señal ECG, típicamente en el rango de 5-15 Hz.

- Diferenciación: Esta etapa realza las pendientes de la señal ECG, facilitando la identificación de las ondas R. La diferenciación resalta los cambios rápidos en la señal, que corresponden a los picos R.

- Cuadratura de Muestras: Se cuadran las muestras para amplificar las diferencias entre los picos R y las otras partes de la señal. Esta etapa asegura que las características de los picos R sean más prominentes.

- Suavizado con Filtro de Media Móvil: Un filtro de media móvil se utiliza para suavizar la señal diferenciada y cuadrada, lo que ayuda a reducir el ruido y a hacer más evidentes los picos R. Este filtro promedia un conjunto de valores de la señal para generar cada punto suavizado.

- Análisis de Correlación y Umbralización: Finalmente, se aplica un análisis de correlación para determinar la semejanza entre la señal procesada y un modelo de onda R. Los umbrales necesarios para detectar los picos R se establecen basándose en los valores máximos y promedio de los picos identificados durante una fase de entrenamiento. Se reconocen como picos R aquellos que superan estos umbrales, marcando así los puntos en la señal original.

**4.2.2. Obtener el RHV(variabilidad de la frecuencia cardíaca)**

El análisis de HRV se realizará en los dominios del tiempo y la frecuencia. Para nuestro analisis análisis en el dominio del tiempo, se considerarán índices como el intervalo medio entre latidos (AVNN), la desviación estándar de los intervalos NN (SDNN), la raíz cuadrada de la media de las diferencias sucesivas de los intervalos NN (RMSSD) y la proporción de intervalos NN adyacentes que difieren más de 50 ms (pNN50). En el dominio de la frecuencia, se calculará la potencia de las bandas de frecuencia muy baja (VLF), baja (LF) y alta (HF), y se determinará la relación LF/HF. 
Estos valores nos permitiran comprender el estado cardiovascular del paciente. Los índices en el dominio del tiempo, como AVNN, SDNN, RMSSD y pNN50, proporcionan información sobre la variabilidad y estabilidad de los intervalos entre latidos.  
En el dominio de la frecuencia, los valores de VLF, LF y HF representan diferentes componentes del espectro de frecuencia de la HRV. VLF está relacionada con la termorregulación, LF se asocia con la actividad simpática y parasimpática, y HF está vinculada con la actividad parasimpática y la respiración. La relación  (LF/HF) evalúa el balance entre las influencias simpáticas y parasimpáticas sobre el corazón[3].


## *5. Resultados* <a name="id7"></a>


### *5.1. Resultado de señal filtrada* <a name="id8"></a>


### *5.2. Resultado de caracteristicas de ECG* <a name="id9"></a>

**5.2.1.**

**5.2.2. Cuadro comparativo de resultados de los índices HRV**

Se comparara los resultados obtenidos mediante codigos del repertorio Biosignalsnotebook y los resultados que nos del articulo "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers"[3]. Con el fin de validar que nuestros valores se asemenjen.

| INDICE DE HVR  |	RESULTADOS DEL ARTICULO |	RESULTADO OBTENIDOS
|:------------:|:---------------:|:------------:|
|AVNN [ms]|954,90 (113,36)||
|SDNN [ms]|84,18 (33,41)||
|RMSSD [ms]|75,84 (41,16)||
|pNN50|0,30 (0,19)||
|VLF[ms^2]|1860,90 (1369,11)||
|BF[ms^2]|2570,18 (2251,61)||
|AF[ms^2]|2774,35 (2378,19)||
|BF/HF|1,2659 (0,8454)||



## *6. Conclusiones* <a name="id10"></a>


## *7. Bibliografia* <a name="id11"></a>

[1] PLUX – Bioseñales inalámbricas, "BITalino (r)evolution Lab Guide", Lisboa, Portugal, 2020.

[2] Singh, R., Mehta, R., & Rajpal, N. (2018). Efficient wavelet families for ECG classification using neural classifiers. Procedia Computer Science. https://doi.org/10.1016/j.procs.2018.05.054&#8203 

[3] S. Sieciński, P. S. Kostka y E. J. Tkacz, "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers. 2020. doi: 10.3390/s20164522.https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472094/

[4] J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm". IEEE Transactions on Biomedical Engineering. 1985, doi: 10.1109/TBME.1985.325532.



