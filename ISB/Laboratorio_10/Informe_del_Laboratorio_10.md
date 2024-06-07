
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


Los filtros se utilizar para a eliminar el ruido y los artefactos que interfieren en la señal. Para ello, se puede utilizr diferentes tipos de filtros que con el fin de que nos proporcionen una lectura de señal más limpia. Entre estos filtros, se encuentran los filtros Wavelet, estos son especialmente eficaces y se dividen en varias familias: Daubechies (db), Symlet (sym), Coiflet (coif), Biorthogonal (bior) y Reverse Biorthogonal (rbio), cada una con características particulares. Las wavelets Daubechies son conocidas por su compacidad y ortogonalidad, mientras que las Symlet son una versión más simétrica de las Daubechies. Las Coiflet son útiles para analizar señales con variaciones lentas, y las Biorthogonal permiten una reconstrucción perfecta de las señales utilizando diferentes filtros para análisis y síntesis. Las Reverse Biorthogonal, similares a las Biorthogonal pero con filtros invertidos, también permiten una reconstrucción precisa. Estas características hacen que los filtros Wavelet sean muy eficaces para la eliminación de ruido en las señales ECG, mejorando significativamente la precisión y la calidad del análisis de estas señales[2].

### Introducción

La variabilidad de la frecuencia cardíaca (HRV) es un indicador clave de la salud cardiovascular y la función del sistema nervioso autónomo. Este análisis mide las fluctuaciones en los intervalos entre latidos consecutivos del corazón, conocidos como intervalos RR. La HRV proporciona información sobre la regulación autónoma del ritmo cardíaco, reflejando el equilibrio entre las influencias simpáticas y parasimpáticas. Utilizando algoritmos como el de Pan-Tompkins para detectar los picos de la onda R en electrocardiogramas (ECG), es posible calcular con precisión los intervalos RR y realizar un análisis detallado de HRV. Este análisis se realiza tanto en el dominio del tiempo como en el dominio de la frecuencia, permitiendo una comprensión del estado cardiovascular del paciente. Los índices de HRV en el dominio del tiempo, como AVNN, SDNN, RMSSD y pNN50, y en el dominio de la frecuencia, como VLF, LF, HF y la relación LF/HF, nos permiten evaluar la estabilidad y variabilidad del ritmo cardíaco y diagnosticar diversas condiciones clínicas, incluyendo enfermedades cardíacas, estrés y disfunción autonómica[3]. 

## *2. Objetivos* <a name="id2"></a>

1. Elección del mejor filtro Wavelet para ECG
2. Segmentación de la señal.
3. Extracción de parámetros estáticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

En este laboratorio, nos enfocaremos en la detección de los picos R en señales de electrocardiograma (ECG) y en el análisis de la variabilidad de la frecuencia cardíaca (HRV). Para ello usaremos de guia el articulo "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers"[3].

### *4.1. Generar filtro* <a name="id5"></a>

En este inciso emplearemos un filtro pasa banda que consiste en un filtro pasa bajo seguido de un filtro pasa alto para eliminar el ruido y las interferencias. Este filtro recursivo de tiempo real, diseñado con coeficientes enteros, tiene polos situados para cancelar ceros en el círculo unitario del plano z. Para nuestro diseño, tomamos como referencia el artículo "A Real-Time QRS Detection Algorithm"[4] y el codigo proporcionado en clase.
El filtro pasa banda estara compuesto por un filtro pasa bajo y un filtro pasa alto en cascada. Esto nos permitira reducir el ruido y  la interferencia electrica de 60 Hz. El filtro pasa bajo es de segundo orden, con una frecuencia de 11Hz; mientras que el filtro pasa alto tiene una frecuencia de corte de 5Hz. Esta combinación nos permite tener un filtro pasa banda de 5-15Hz[4].


### *4.2.Obtener caracteristicas de ECG* <a name="id6"></a>

**4.2.1. Obtener los picos R**

Para identificar las ondas R de nuestra señal, se utilizara el algoritmo de Pan-Tompkins, que incluye varios pasos: aplicar un filtro pasabanda,diferenciación, cuadratura de muestras, suavizado con un filtro de media móvil, y análisis de correlación y umbralización. Los umbrales necesarios para detectar los picos se obtendra del articulo, estos fueron hallados a partir de los valores máximos y promedios de los picos identificados durante su fase de entrenamiento. Finalmente, se reconoceran como picos R aquellos que superan estos umbrales, marcando así los puntos en la señal original [3].

- Filtro Pasabanda: Se aplicó un filtro pasabanda para eliminar el ruido de alta frecuencia y las variaciones lentas en la línea de base, manteniendo únicamente las frecuencias relevantes para la señal ECG. En este caso, la banda deseable para mazimixar la energía del complejo QRS se encuentra típicamente en el rango de 5-15 Hz; sin embargo, el artículo utilizó el rango 5-12 Hz. [4]

- Diferenciación: Esta etapa realkza las pendientes de la señal ECG, facilitando la identificación de las ondas R. La diferenciación resalta los cambios rápidos en la señal, que corresponden a los picos R.

- Cuadratura de Muestras: Se cuadran las muestras para amplificar las diferencias entre los picos R y las otras partes de la señal. Esta etapa asegura que las características de los picos R sean más prominentes.

- Suavizado con Filtro de Media Móvil: Un filtro de media móvil se utiliza para suavizar la señal diferenciada y cuadrada, lo que ayuda a reducir el ruido y a hacer más evidentes los picos R. Este filtro promedia un conjunto de valores de la señal para generar cada punto suavizado.

- Análisis de Correlación y Umbralización: Finalmente, se aplica un análisis de correlación para determinar la semejanza entre la señal procesada y un modelo de onda R. Se reconocen como picos R aquellos que superan estos umbrales, marcando así los puntos en la señal original.

**4.2.2. Obtener el RHV(variabilidad de la frecuencia cardíaca)**

El análisis de HRV se realizará en los dominios del tiempo y la frecuencia. Para nuestro analisis análisis en el dominio del tiempo, se considerarán índices como el intervalo medio entre latidos (AVNN), la desviación estándar de los intervalos NN (SDNN), la raíz cuadrada de la media de las diferencias sucesivas de los intervalos NN (RMSSD) y la proporción de intervalos NN adyacentes que difieren más de 50 ms (pNN50). En el dominio de la frecuencia, se calculará la potencia de las bandas de frecuencia muy baja (VLF), baja (LF) y alta (HF), y se determinará la relación LF/HF. 
Estos valores nos permitiran comprender el estado cardiovascular del paciente. Los índices en el dominio del tiempo,  proporcionan información sobre la variabilidad y estabilidad de los intervalos entre latidos.  
En el dominio de la frecuencia, los valores de VLF, LF y HF representan diferentes componentes del espectro de frecuencia de la HRV. VLF está relacionada con la termorregulación, LF se asocia con la actividad simpática y parasimpática, y HF está vinculada con la actividad parasimpática y la respiración. La relación  (LF/HF) evalúa el balance entre las influencias simpáticas y parasimpáticas sobre el corazón[3].


## *5. Resultados* <a name="id7"></a>


### *5.1. Resultado de la señal filtrada* <a name="id8"></a>

| |	SEÑAL ORIGINAL |	SEÑAL FILTRADA|
|:------------:|:---------------:|:------------:|
|En reposo|![Captura de pantalla 2024-06-07 112731](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/4b8b303e-1b09-443f-8b03-85b77a9949eb)|![Captura de pantalla 2024-06-07 112810](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/a0ef7532-9bc6-4756-a8e9-53361926e750)|
|Respiración profunda antes del ejercicio|![Captura de pantalla 2024-06-07 122611](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/eb439e27-4316-4766-b815-538ecadb723c)|![Captura de pantalla 2024-06-07 122632](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9b204dbb-a046-40fa-a898-cecba7c15ce1)|
|Burpees|![Captura de pantalla 2024-06-07 122844](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/ba7cf9b4-23b9-4125-a214-bb450da9916d)|![Captura de pantalla 2024-06-07 122911](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/50423663-564e-4329-b48a-14f19be624fa)|
|Respiración profunda después del ejercicio| | |


### *5.2. Resultado de caracteristicas de ECG* <a name="id9"></a>

**5.2.1.Resultados de los picos R**

| |	SEÑALIZACIÓN DE UMBRALES | IDENTIFICACIÓN DE PICOS RR|
|:------------:|:---------------:|:------------:|
|En reposo|![Captura de pantalla 2024-06-07 113139](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0fdd4098-67d5-44f1-b1ac-db7637391842)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/f48fac12-a3df-474a-933a-1540b03ca517)|
|Respiración profunda antes del ejercicio|![Captura de pantalla 2024-06-07 122128](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0a352195-8e02-47a0-89ca-0974403a431d)|![Captura de pantalla 2024-06-07 122153](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/26e846d2-63ac-4dc9-b763-5e428c67c355)|
|Burpees|![Captura de pantalla 2024-06-07 122945](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/1c819994-5360-4eb7-87ef-6488bbbfade0)|![Captura de pantalla 2024-06-07 123014](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/cfd1d72b-e0de-43d1-8181-a4a70bb1a385)|
|Respiración profunda después del ejercicio| | |

**5.2.2. Cuadro comparativo de resultados de los índices HRV**

Se comparara los resultados obtenidos mediante codigos del repertorio Biosignalsnotebook[5] y los resultados del articulo "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers"[3]. Con el fin de validar que nuestros valores y analizar nuestros resultados de las pruebas que realizamos. 

| INDICE DE HVR  |	EN REPOSO |RESPIRACIÓN PROFUNDA_ANTES DEL EJERCICIO|DESPUÉS DEL EJERCICIO|
|:------------:|:---------------:|:------------:|:-------:|
|AVNN [ms]|963.20|813.82|713.59|
|SDNN [ms]|60.36|71.99|41.76|
|RMSSD [ms]|74.61|46.34|47.89|
|pNN50 [%]|16.33|34.09|40.00|
|VLF[ms^2]|0.00|0.00|0.00|
|LF[ms^2]|0.00|0.00|0.00|
|HF[ms^2]|146.52||1947.00|142.00|
|LF/HF|0.00|0.00||


## *6. Conclusiones* <a name="id10"></a>


## *7. Bibliografia* <a name="id11"></a>

[1] PLUX – Bioseñales inalámbricas, "BITalino (r)evolution Lab Guide", Lisboa, Portugal, 2020.

[2] Singh, R., Mehta, R., & Rajpal, N. (2018). Efficient wavelet families for ECG classification using neural classifiers. Procedia Computer Science. https://doi.org/10.1016/j.procs.2018.05.054&#8203 

[3] S. Sieciński, P. S. Kostka y E. J. Tkacz, "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers. 2020. doi: 10.3390/s20164522.https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472094/

[4] J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm". IEEE Transactions on Biomedical Engineering. 1985, doi: 10.1109/TBME.1985.325532.

[5] "Indices de HRV". [En línea]. Disponible en:

