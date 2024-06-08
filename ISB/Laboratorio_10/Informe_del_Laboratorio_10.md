
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
4. [Metodología](#id4)\
     4.1 [Generar filtro para ECG](#id5)\
     4.2 [Obtener características de ECG](#id6)
6. [Resultados](#id7)\
     5.1 [Resultado de señal filtrada](#id8)\
     5.2 [Resultado de características de ECG](#id9)
8. [Conclusiones](#id10)
9. [Bibliografía](#id11)
   
## *1. Introducción* <a name="id1"></a>

El electrocardiograma (ECG) es una herramienta de diagnóstico utilizada para medir la actividad del corazón. Consiste en colocar electrodos en partes específicas del cuerpo, las cuales tienen contacto con la piel, para detectar impulsos eléctricos generados por el corazón. Esta información se registra como ondas en un gráfico.
La señal ECG contiene diferentes componentes como la onda P, el complejo QRS y la onda T; los cuales representan la despolarización auricular, despolarización ventricular y repolarización ventricular, respectivamente.
El ECG posee 12 derivadas que permiten visualizar el corazón desde diferentes ángulos. Estas derivaciones se pueden utilizar para detectar arritmias y transtornos cardíacos. Entre las derivaciones tenemos: derivaciones bipolares (I, II, III), derivaciones unipolares (aVR, aVL, aVF) y derivaciones precordiales (V1-V6) [1].


Los filtros se utilizar para a eliminar el ruido y los artefactos que interfieren en la señal; para así obtener una lectura de señal más limpia. Un ejemplo de estos filtros, como se observó en laboratorios pasados, es el filtro Wavelet; la cual utiliza diversas familias: Daubechies (db), Symlet (sym), Coiflet (coif), Biorthogonal (bior) y Reverse Biorthogonal (rbio), cada una con características particulares. Las wavelets Daubechies son conocidas por su compacidad y ortogonalidad, mientras que las Symlet son una versión más simétrica de las Daubechies. Las Coiflet son útiles para analizar señales con variaciones lentas, y las Biorthogonal permiten una reconstrucción perfecta de las señales utilizando diferentes filtros para análisis y síntesis. Las Reverse Biorthogonal, similares a las Biorthogonal pero con filtros invertidos, también permiten una reconstrucción precisa. Estas características hacen que los filtros Wavelet sean muy eficaces para la eliminación de ruido en las señales ECG, mejorando significativamente la precisión y la calidad del análisis de estas señales [2].

### HRV

La variabilidad de la frecuencia cardíaca (HRV, por sus siglas en inglés) es un indicador clave de la salud cardiovascular y la función del sistema nervioso autónomo. Este análisis mide las fluctuaciones en los intervalos entre latidos consecutivos del corazón, conocidos como intervalos RR. La HRV proporciona información sobre la regulación autónoma del ritmo cardíaco, reflejando el equilibrio entre las influencias simpáticas y parasimpáticas. Utilizando algoritmos como el de Pan-Tompkins, para detectar los picos de la onda R en electrocardiogramas (ECG), es posible calcular con precisión los intervalos RR y realizar un análisis detallado de HRV. Este análisis se realiza tanto en el dominio del tiempo como en el dominio de la frecuencia, permitiendo una comprensión del estado cardiovascular del paciente. Los índices de HRV en el dominio del tiempo como AVNN, SDNN, RMSSD y pNN50; y en el dominio de la frecuencia como VLF, LF, HF y la relación LF/HF; nos permiten evaluar la estabilidad y variabilidad del ritmo cardíaco y diagnosticar diversas condiciones clínicas, incluyendo enfermedades cardíacas, estrés y disfunción autonómica [3]. 

## *2. Objetivos* <a name="id2"></a>

1. Filtrado de la señal
2. Obtención de características del complejo QRS del ECG (picos R, intervalos RR)
3. Obtención de parámetros para evaluar el HRV

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodología* <a name="id4"></a>

En este laboratorio, nos enfocaremos en la detección de los picos R en señales de electrocardiograma (ECG) y en el análisis de la variabilidad de la frecuencia cardíaca (HRV). Para ello usaremos de guia el articulo "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers" [3].

### *4.1. Generar filtro* <a name="id5"></a>

En este inciso emplearemos un filtro pasa banda que consiste en un filtro pasa bajo seguido de un filtro pasa alto para eliminar el ruido y las interferencias. Este filtro recursivo de tiempo real, diseñado con coeficientes enteros, tiene polos situados para cancelar ceros en el círculo unitario del plano z. Para nuestro diseño, tomamos como referencia el artículo "A Real-Time QRS Detection Algorithm" [4] y el codigo proporcionado en clase.
El filtro pasa banda estara compuesto por un filtro pasa bajo y un filtro pasa alto en cascada. Esto nos permitirá reducir el ruido y  la interferencia electrica de 60 Hz. El filtro pasa bajo es de segundo orden, con una frecuencia de corte de 11 Hz; mientras que el filtro pasa alto tiene una frecuencia de corte de 5 Hz. Esta combinación nos permite tener un filtro pasa banda de 5-12Hz [4].


### *4.2.Obtener características de ECG* <a name="id6"></a>

**4.2.1. Obtener los picos R**

Para identificar las ondas R de nuestra señal, se utilizará el algoritmo de Pan-Tompkins, que incluye varios pasos descritos a continuación. Pero antes, cabe mencionar que los valores utilizados en cada paso se obtendrán del artículo, tales como valores máximos y promedios de los picos identificados durante su fase de entrenamiento; así como diversas ecuaciones matemáticas empleada en cada etapa [3, 4].

- Filtro Pasabanda: Se aplicó un filtro pasabanda para eliminar el ruido de alta frecuencia y las variaciones lentas en la línea de base, manteniendo únicamente las frecuencias relevantes para la señal ECG. En este caso, la banda deseable para maximizar la energía del complejo QRS se encuentra típicamente en el rango de 5-15 Hz; sin embargo, el artículo utilizó el rango 5-12 Hz [4].

- Diferenciación: Esta etapa realiza las pendientes de la señal ECG, facilitando la identificación de las ondas R. La diferenciación resalta los cambios rápidos en la señal, que corresponden a los picos R.

- Cuadratura de Muestras: Las muestras se elevan al cuadrado para amplificar las diferencias entre los picos R y las otras partes de la señal. Esta etapa asegura que las características de los picos R sean más prominentes.

- Suavizado con Filtro de Media Móvil: Un filtro de media móvil se utiliza para suavizar la señal diferenciada y cuadrada, lo que ayuda a reducir el ruido y a hacer más evidentes los picos R. Este filtro promedia un conjunto de valores de la señal para generar cada punto suavizado.

- Análisis de Correlación y Umbralización: Finalmente, se aplica un análisis de correlación para determinar la semejanza entre la señal procesada y un modelo de onda R. Finalmente, se reconocen como picos R aquellos que superan estos umbrales, marcando así los puntos en la señal original.

**4.2.2. Obtener el HRV (variabilidad de la frecuencia cardiaca)**

El análisis de HRV se realizará en los dominios del tiempo y la frecuencia. Para nuestro análisis en el dominio del tiempo, se considerarán índices como el intervalo medio entre latidos (AVNN), la desviación estándar de los intervalos NN (SDNN), la raíz cuadrada de la media de las diferencias sucesivas de los intervalos NN (RMSSD) y la proporción de intervalos NN adyacentes que difieren más de 50 ms (pNN50); estos índices proporcionan información sobre la variabilidad y estabilidad de los intervalos entre latidos. En el dominio de la frecuencia, se calculará la potencia de las bandas de frecuencia muy baja (VLF), baja (LF) y alta (HF), y se determinará la relación LF/HF. Estos valores permitirán comprender el estado cardiovascular del paciente. Los valores de VLF, LF y HF representan diferentes componentes del espectro de frecuencia de la HRV. VLF está relacionada con la termorregulación, LF se asocia con la actividad simpática y parasimpática, y HF está vinculada con la actividad parasimpática y la respiración. La relación LF/HF evalúa el balance entre las influencias simpáticas y parasimpáticas sobre el corazón [3].


## *5. Resultados* <a name="id7"></a>


### *5.1. Resultado de la señal filtrada* <a name="id8"></a>

Como se explicó anteriormente, el presente filtrado corresponde a un filtro pasabanda en el rango de 5-12 Hz. Para una mejor visualización de cada señal, solo se muestran los intervalos de 0-10 segundos.

| |	SEÑAL ORIGINAL |	SEÑAL FILTRADA|
|:------------:|:---------------:|:------------:|
|En reposo|![Captura de pantalla 2024-06-07 112731](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/4b8b303e-1b09-443f-8b03-85b77a9949eb)|![Captura de pantalla 2024-06-07 112810](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/a0ef7532-9bc6-4756-a8e9-53361926e750)|
|Respiración profunda antes del ejercicio|![Captura de pantalla 2024-06-07 122611](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/eb439e27-4316-4766-b815-538ecadb723c)|![Captura de pantalla 2024-06-07 122632](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9b204dbb-a046-40fa-a898-cecba7c15ce1)|
|Burpees|![Captura de pantalla 2024-06-07 122844](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/ba7cf9b4-23b9-4125-a214-bb450da9916d)|![Captura de pantalla 2024-06-07 122911](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/50423663-564e-4329-b48a-14f19be624fa)|
|Respiración profunda después del ejercicio|![Captura de pantalla 2024-06-07 123521](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/5d7a063d-d68a-472f-8c9c-5472158313d6)|![Captura de pantalla 2024-06-07 123547](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/6c0d5f5b-3cbc-421b-b551-30f410ed631c)|


### *5.2. Resultado de características de ECG* <a name="id9"></a>

**5.2.1.Resultados de los picos R**

Luego de seguir los pasos del algoritmo Pan-Tompkins aplicado en el artículo [4], se obtienen las siguientes gráficas; donde se muestra los umbrales hallados y, en base a ello, la identificación de los complejos QRS y los picos R.

| |	SEÑALIZACIÓN DE UMBRALES | IDENTIFICACIÓN DE PICOS RR|
|:------------:|:---------------:|:------------:|
|En reposo|![Captura de pantalla 2024-06-07 113139](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0fdd4098-67d5-44f1-b1ac-db7637391842)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/f48fac12-a3df-474a-933a-1540b03ca517)|
|Respiración profunda antes del ejercicio|![Captura de pantalla 2024-06-07 122128](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0a352195-8e02-47a0-89ca-0974403a431d)|![Captura de pantalla 2024-06-07 122153](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/26e846d2-63ac-4dc9-b763-5e428c67c355)|
|Burpees|![Captura de pantalla 2024-06-07 122945](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/1c819994-5360-4eb7-87ef-6488bbbfade0)|![Captura de pantalla 2024-06-07 123014](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/cfd1d72b-e0de-43d1-8181-a4a70bb1a385)|
|Respiración profunda después del ejercicio|![Captura de pantalla 2024-06-07 123625](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c4318088-94e1-4e59-bec1-13ced3f5eae0)|![Captura de pantalla 2024-06-07 123647](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/9c313fae-fc11-40be-9d41-47354f30bbd0)|



**5.2.2. Cuadro comparativo de resultados de los índices HRV**

Se comparará los resultados obtenidos mediante códigos del repertorio Biosignalsnotebook [5] y los resultados del articulo "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers" [3]. Con el fin de validar nuestros valores y analizar los resultados de las pruebas que realizamos. Cabe mencionar que en el artículo se tomaron muestras que duraron 260 min, que incluyeron diversas actividades que se le pidió a cada paciente como respiración normal por 2 min, sostener la respiración por 30 s, respiración normal por 30 s, respiración en posición supina por 10 min y así recurrentemente hasta alcanzar el tiempo establecido. Es decir, el artículo analizó la data de diversas actividades en conjunto; no como las medidas que se tomaron en nuestro laboratorio para cada actividad.

| ÍNDICE DE HVR  |	EN REPOSO |RESPIRACIÓN PROFUNDA ANTES DEL EJERCICIO|BURPEES|RESPIRACIÓN PROFUNDA DESPUÉS DEL EJERCICIO||RESULTADOS DEL ARTÍCULO BASE|
|:------------:|:---------------:|:------------:|:-------:|:-----:|:--:|:--:|
|AVNN [ms]|963.20|813.82|713.59|830.31||954.90
|SDNN [ms]|60.36|71.99|41.76|90.68||84.18|
|RMSSD [ms]|74.61|46.34|47.89|55.50||75.84|
|pNN50 [%]|16.33|34.09|40.00|28.57||30.00|
|VLF[ms^2]|0.00|0.00|0.00|0.00||1860.90|
|LF[ms^2]|0.00|0.00|0.00|0.00||2570.18|
|HF[ms^2]|146.52|1947.00|142.00|0.00||2774.35|
|LF/HF|0.00|0.00|0.00|0.00||1.27|

### DISCUSIÓN

El intervalo medio entre latidos(AVNN), es mayor en reposo (963.20 ms) y disminuye durante el ejercicio intenso (713.59 ms), recuperándose parcialmente después de la respiración profunda post-ejercicio (830.31 ms). Estos hallazgos están en línea con el estudio de  García G. et al. que nos dice que el intervalo medio entre latidos (AVNN) es mayor en reposo y disminuye durante el ejercicio intenso debido a la activación del sistema nervioso simpático. El AVNN se recupera parcialmente después del ejercicio gracias a la reactivación parasimpática. Esto coincide con lo obtenido en donde el AVNN se redujo durante el ejercicio intenso y se recupera parcialmente después de la respiración profunda post-ejercicio[7].

La desviación estándar de los intervalos NN (SDNN) muestra una mayor variabilidad en condiciones de recuperación (90.68 ms) y menor durante el ejercicio (41.76 ms). Lo obtenido se alinea a los resultados evaluados en el estudio de El-Malahi O. et al. en donde se obtuvo que la SDNN es significativamente mayor durante los períodos de recuperación post-ejercicio y menor durante el ejercicio, reflejando fluctuaciones de ritmo más estables en reposo. Además, se destaca que la SDNN es un marcador robusto de la variabilidad total de la frecuencia cardíaca y está asociada con una mejor capacidad de recuperación autónoma post-ejercicio[8]. 

La RMSSD, una medida de la variabilidad a corto plazo, es mayor en reposo (74.61 ms) y disminuye con la respiración profunda y el ejercicio. Según lo presentado por M. You et al., durante una sesión de respiración lenta (SPB) se observa un aumento significativo en la RMSSD en todas las condiciones en comparación con la condición de control, confirmando su sensibilidad a los cambios en la actividad vagal. Estudios recientes han demostrado que la RMSSD disminuye significativamente durante el estrés fisiológico y aumenta durante períodos de descanso, lo que respaldó su uso como un marcador fiable de la variabilidad de la frecuencia cardíaca y su relación con la regulación autónoma[9]"

El pNN50, que mide la proporción de intervalos sucesivos que difieren en más de 50 ms, es significativamente alto durante la respiración profunda antes del ejercicio (34.09%), sugiriendo una mayor influencia parasimpática. Investigaciones recientes indican que el pNN50 es un buen indicador de la actividad parasimpática y su aumento durante la respiración profunda es consistente con una mayor activación vagal [4].

Los valores de VLF y LF son nulos debido a la corta duración de los registros (40-50 segundos), lo que resulta insuficiente para un análisis adecuado de estas bandas de frecuencia, en contraste con los resultados más robustos obtenidos con registros de 260 minutos. Estudios han resaltado la importancia de registros más prolongados para obtener mediciones precisas de las bandas de frecuencia VLF y LF, ya que estas reflejan diferentes componentes de la regulación autónoma [5].

La banda HF muestra un incremento significativo durante la respiración profunda antes del ejercicio (1947.00 ms²) y disminuye a cero post-ejercicio, destacando la fluctuación en la actividad parasimpática. Estudios recientes confirman que la banda HF es un marcador fiable de la actividad parasimpática y su variabilidad durante el ejercicio y la recuperación proporciona información valiosa sobre la modulación vagal [6].

La relación LF/HF es nula en nuestro experimento, subrayando nuevamente la necesidad de registros más prolongados para obtener una evaluación completa de la HRV. La relación LF/HF es ampliamente utilizada para evaluar el balance simpático-vagal, pero estudios recientes recomiendan cautela en su interpretación, especialmente en registros de corta duración [7].


## *6. Conclusiones* <a name="id10"></a>

En este laboratorio, hemos explorado técnicas avanzadas para el procesamiento y análisis de señales electrocardiográficas (ECG), con un enfoque particular en el filtrado y la extracción de características clave. Se logró un filtrado efectivo de la señal ECG mediante la implementación de un filtro pasabanda compuesto por un filtro pasa bajo y un filtro pasa alto en cascada. Esta combinación permitió eliminar el ruido y las interferencias, conservando las frecuencias relevantes de la señal ECG y mejorando la calidad para el análisis posterior.

La aplicación del algoritmo de Pan-Tompkins fue exitosa en la identificación precisa de los picos R en la señal ECG. Este proceso involucró etapas de diferenciación, cuadratura y suavizado, lo que facilitó la detección de los picos R, esenciales para el análisis de la variabilidad de la frecuencia cardíaca (HRV). El análisis de HRV en los dominios del tiempo y la frecuencia proporcionó información valiosa sobre la salud cardiovascular y la función autonómica de los sujetos. Sin embargo, la duración limitada de nuestros registros (40-50 segundos) afectó la capacidad de calcular adecuadamente los parámetros de frecuencia, especialmente las bandas VLF y LF. Esto destaca la importancia de contar con registros más prolongados para un análisis completo y preciso.

Al comparar nuestros resultados con los del artículo base, se observó una diferencia significativa, especialmente en los índices de HRV en el dominio de la frecuencia. La mayor duración de los registros en el estudio base permitió obtener datos más robustos y confiables, lo que subraya la necesidad de registros de mayor duración para estudios comparables. Los diferentes experimentos realizados (reposo, respiración profunda antes y después del ejercicio, y ejercicio intenso) mostraron variaciones claras en los índices de HRV, reflejando cambios fisiológicos. Estos resultados demuestran cómo las actividades físicas y las técnicas de respiración pueden influir significativamente en la variabilidad de la frecuencia cardíaca.

## *7. Bibliografía* <a name="id11"></a>

[1] PLUX – Bioseñales inalámbricas, "BITalino (r)evolution Lab Guide", Lisboa, Portugal, 2020.

[2] Singh, R., Mehta, R., & Rajpal, N. (2018). Efficient wavelet families for ECG classification using neural classifiers. Procedia Computer Science. https://doi.org/10.1016/j.procs.2018.05.054&#8203 

[3] S. Sieciński, P. S. Kostka y E. J. Tkacz, "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers. 2020. doi: 10.3390/s20164522.https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7472094/

[4] J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm". IEEE Transactions on Biomedical Engineering. 1985, doi: 10.1109/TBME.1985.325532.

[5] "Indices de HRV". [En línea]. Disponible en:

[6] J. A. J. Heathers, “Everything Hertz: methodological issues in short-term frequency-domain HRV”, Front Physiol, vol. 5, p. 177, may 2014, doi: 10.3389/fphys.2014.00177.

[7] G. L. Garcia, L. G. G. Porto, C. J. G. da Cruz, and G. E. Molina, "Can resting heart rate explain the heart rate and parasympathetic responses during rest, exercise, and recovery?," PLOS ONE, vol. 17, no. 12, p. e0277848, Dec. 2022. [Online]. https://doi.org/10.1371/journal.pone.0277848

[8] O. El-Malahi, D. Mohajeri, R. Mincu, A. Bäuerle, K. Rothenaicher, R. Knuschke, C. Rammos, T. Rassaf, and J. Lortz, "Beneficial impacts of physical activity on heart rate variability: A systematic review and meta-analysis," PLOS ONE, vol. 19, no. 4, p. e0299793, Apr. 2024. [Online]. Available: https://doi.org/10.1371/journal.pone.0299793

[9] M. You, S. Laborde, N. Zammit, M. Iskra, U. Borges, and F. Dosseville, "Single Slow-Paced Breathing Session at Six Cycles per Minute: Investigation of Dose-Response Relationship on Cardiac Vagal Activity," Int. J. Environ. Res. Public Health, vol. 18, no. 23, p. 12478, Nov. 2021. [Online]. Available: https://doi.org/10.3390/ijerph182312478



