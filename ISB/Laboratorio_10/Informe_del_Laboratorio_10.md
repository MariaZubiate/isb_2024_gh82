
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

### *4.1. Generar filtro  para ECG* <a name="id5"></a>


### *4.2.Obtener caracteristicas de ECG* <a name="id6"></a>

## *5. Resultados* <a name="id7"></a>


### *5.1. Resultado de señal filtrada* <a name="id8"></a>


### *5.2. Resultado de caracteristicas de ECG* <a name="id9"></a>


## *6. Conclusiones* <a name="id10"></a>


## *7. Bibliografia* <a name="id11"></a>

[1] PLUX – Bioseñales inalámbricas, "BITalino (r)evolution Lab Guide", Lisboa, Portugal, 2020.

[2] Singh, R., Mehta, R., & Rajpal, N. (2018). Efficient wavelet families for ECG classification using neural classifiers. Procedia Computer Science. https://doi.org/10.1016/j.procs.2018.05.054&#8203 

[3] S. Sieciński, P. S. Kostka y E. J. Tkacz, "Heart Rate Variability Analysis on Electrocardiograms, Seismocardiograms and Gyrocardiograms on Healthy Volunteers. 2020. doi: 10.3390/s20164522.




