
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
     4.1. [Parametros estáticos y temporales para EMG](#id6)
6. [Resultados](#id7)\
     5.1 [Resultado de elección de filtro para EMG](#id8)\
     5.1 [Resultado de los parametros estáticos y temporales para EMG](#id9) 
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
   
5. Extracción de parametros estáticos y temporales de la señal.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

Llevaremos a cabo una comparación de 3 diferentes filtros que encontramos optimos en la busqueda de información que realizamos para la eliminación de ruido en señales EMG. El objetivo de este estudio es determinar cuál de estos filtros ofrece el mejor rendimiento en la eliminación de ruido de señales EMG con visualización de eliminación de ruido y analisis de señal ruido (SNR). 

**Los tres filtros encontrados en la literatura y candidatos para su aplicación fueron wavelets Symmlets, Daubechies y Bio-ortogonal(RBio3.1), respectivamente.*

### *4.1. Filtros para EMG* <a name="id5"></a>

*Wavelets Daubechies*

Son compactamente soportados, lo que significa que son no nulos solo en una región finita del dominio, proporcionando eficiencia computacional en la transformada wavelet de una señal. Una de sus características más destacadas es el alto número de momentos de anulación, lo que les permite capturar detalles finos y eliminar tendencias de baja frecuencia sin perder información crucial. Estas propiedades son esenciales para descomponer señales no estacionarias y con características transitorias, como las señales EMG. En el análisis de señales EMG, los wavelets Daubechies ofrecen una localización precisa en el dominio tiempo-frecuencia, importante para capturar y analizar componentes transitorias, como los potenciales de acción de unidades motoras (MUAPs). Además, la capacidad de estos wavelets para filtrar el ruido de alta frecuencia mientras se preservan las características importantes de la señal mejora la calidad de la descomposición y el análisis de la señal EMG, facilitando una interpretación precisa.

*Wavelets Symlets*

Al igual que los Daubechies, son compactamente soportados, proporcionando eficiencia en la descomposición de señales. Sin embargo, los Symlets se destacan por tener la menor asimetría posible y una fase casi lineal, lo que minimiza la distorsión de la señal durante la descomposición y la reconstrucción. Esta característica es especialmente importante en nuestro análisis de señales EMG, donde la preservación de la forma de la señal es crítica para el diagnóstico preciso de la actividad muscular y neuromuscular. La capacidad de los Symlets para manejar transitorios con mínima distorsión permite una descomposición precisa de componentes transitorias en las señales EMG, facilitando la identificación y el análisis de los MUAPs. 

*Wavelet Biortogonal Inverso*

Este wavelet mantiene la ortogonalidad durante las transformaciones, con una reconstrucción precisa de la señal original. Su diseño simétrico evita la distorsión de fase, lo cual es crucial para preservar las características transitorias de la señal EMG. Además, su soporte compacto facilita una buena localización temporal, y su número específico de momentos de anulación le permite filtrar el ruido de eficazmente y resaltar las características significativas de la señal. Este wavelet es especialmente efectivo para señales EMG debido a su capacidad para proporcionar una excelente localización en el dominio tiempo-frecuencia, para identificar rápidamente los cambios relacionados con la actividad muscular y la fatiga. 

En este inciso haremos una discusión de los 3 filtros a analizar. 

**1.Primer filtro: Symlets Wavelets**

En primera instancia usaremos la referencia ya usada en el trabajo anterior "Detección no invasiva de fatiga muscular de bajo nivel mediante EMG de superficie con descomposición wavelet" donde se determino que el filtro mas eficiente era la función Wavelet Sym8, debido a que con ello obtuvo un rendimiento superior a comparación de los demás Symmlets. Así como, en ello utilizaron 9 niveles de procesamiento, asi como se eliminaron los niveles 1,8 y 9 debido a la presencia de artefactos de baja frecuencia como artefactos de movimientos. quedandose solo con los niveles 2,3,4,5,6 y 7 [4]. 

Por lo que para nuestro primer filtro realizaremos:

1.Descomposición de 8 coeficientes.

2.Eliminación de coeficiente 1,8,9.

3.Reconstrucción de la señal filtrada. 


**2. Segundo filtro: Daubechies Wavelets**

Para el segundo filtros utilizamos el articulo "Comparative study of wavelet denoising in myoelectric control applications", en el cual se investigó el uso de diferentes wavelets para la mejora de la calidad de la señal miográfica antes de su uso en diseños protésicos. En este estudio, se evaluaron varias funciones wavelet, y se encontró que la wavelet Daubechies (db4) era la más efectiva para la eliminación de ruido en señales EMG. En este articulo se utilizó un análisis de dominio de tiempo y frecuencia para evaluar la relación entre la contracción muscular y la señal, encontrando que durante las contracciones sostenidas, la frecuencia media (MNF) y la frecuencia mediana (MDF) aumentaban con los niveles de fuerza muscular [5].

Para nuestro segundo filtro, utilizaremos el Daubechies (db4). La implementación de este filtro seguirá este paso:

1. Descomposición de la señal utilizando las funciones wavelet db4.
   
3. Aplicación de métodos de umbral para la eliminación de ruido en los coeficientes descompuestos.
   
5. Reconstrucción de la señal utilizando los coeficientes modificados.

**3. Tercer filtro: Wavelet biortogonal inversa**

Para el ultimo filtro usaremos el articulo "Discrete wavelet transform analysis of surface electromyography for the
fatigue assessment of neck and shoulder muscles",se utilizó la transformada wavelet discreta (DWT) para evaluar la fatiga muscular en el cuello y los hombros bajo condiciones dinámicas repetitivas. Se probaron diez funciones wavelet comunes, y se encontró que la wavelet "Rbio3.1" era la más sensible a los cambios espectrales inducidos por la fatiga en la banda de frecuencia de 12–23 Hz. Se realizo el análisis DWT en datos SEMG recogidos durante 40 minutos de ejercicios repetitivos de brazos y cuello, descomponiendo la señal en siete niveles para analizar el poder en diferentes bandas de frecuencia [6]. 

Para el tercer filtro utilizaremos estos pasos:

1. Descomposición de la señal en 7 niveles utilizando Rbio3.1.
2. Reconstrucción de la señal utilizando los coeficientes de detalle seleccionados.
   
### *4.2. Parametros estáticos y temporales para EMG* <a name="id6"></a>


#### *Parametros estáticos*
##### *4.2.1. Media* 

La media representa el valor promedio de la señal [2M]. En la Imagen 1, se puede observar la formula a utilizar.

<p align="center">
  <img src=https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/ee08dca9-040c-4900-a031-caaabe5181c5 alt="Imagen1">
</p>
<p align="center">
  Imagen1. Fuente: Biosignalnotebook-github
</p>

##### *4.2.2. Varianza y desviación estandar*

Varianza: Mide la dispersión de los datos respecto a la media. Indica cuánto varían los datos en torno a su valor promedio.

Desviación Estándar: Es la raíz cuadrada de la varianza, proporcionando una medida de dispersión en las mismas unidades que los datos originales [2M]. En la Imagen 2, se puede observar la formula a utilizar.

<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/65fa30e8-ee5d-40e9-8edc-a8180c363262" alt="Imagen2">
</p>

<p align="center">
  Imagen2. Fuente: Biosignalnotebook-github
</p>

##### *4.2.3. Skewness*

Skewness: Mide la asimetría de la distribución de los datos. Una distribución normal tiene un skewness de 0. Un valor positivo indica que la cola derecha de la distribución es más larga, mientras que un valor negativo indica una cola izquierda más larga [2M].

#### *Parametros temporales*
##### *4.2.4. Estacionalidad* 

La estacionalidad se refiere a patrones repetitivos o ciclos que ocurren a intervalos regulares en una serie temporal. La descomposición estacional permite dividir la serie temporal en componentes de tendencia, estacionalidad y residuo [2M].

## *5. Resultados* <a name="id7"></a>

### *5.1. Resultado de elección de filtro para EMG* <a name="id8"></a>

**REPOSO**

|  **Campo**  |  **Señal cruda** | **Coeficientes de eliminación**
|:------------:|:---------------:|:---------------:
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/efeb5453-7a5e-42ff-ad83-88d90a979384)|---------
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2e1bc986-80fc-4c95-8465-7e7922ffceaa)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/001eb900-b0eb-465c-97e8-fb49c109e53b)
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d0d21558-571e-4aa8-8279-6a2344d19b15)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/550b31ea-3768-4623-9712-98b95cfb59fd)
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/1c97c51d-d3a7-4dbd-a551-19423fb09b4d)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/f8d2b850-a74d-480a-aec9-b0b5b2f247ed)

**FLEXIÓN**
|  **Campo**  |  **Señal cruda** | **Coeficientes de eliminación**
|:------------:|:---------------:|:---------------:
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0ef37aca-0736-4642-aa60-e14eb6cd1b4b)|---------
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2ae0bfe2-cf6b-4710-bbf4-bb8c59f98694)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/6696bebf-320f-42f5-b8f7-08f3df97f903)
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5b7077ad-a84e-4803-890a-934f55b84d39)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0a0b39f8-d16a-42c3-95f7-6daceeb66ba5)
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9acac2d0-e9e6-42e7-8da3-45417fd7f046)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/8e074d24-33b4-41e2-ab18-afa4bbedbe63)



**CONTRAFUERZA**
|  **Campo**  |  **Señal cruda** | **Coeficientes de eliminación**
|:------------:|:---------------:|:---------------:
|Señales |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/2c101981-8c7f-4d34-b5bb-d9b82e55ff3a)|---------
|Señal filtrada 1|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/c6172f33-5cef-4bb0-8710-fca36aa51bc4)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/15193891-7158-4b0a-8389-70610bbdd51e)
|Señal filtrada 2|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d46c8f39-f03f-4de0-9134-4bbf96d9c3ad)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/d085b012-59e4-43ab-9ce6-2e8174d634fe)
|Señal filtrada 3|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/889ecfe7-46a2-40cb-8d8e-a1d6c9d879d1)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/da043110-0d63-4e94-bada-ab8e4de2d46f)


**Cuadro comparatido de SNR de los filtros**

Se realizo un cuadro comparativo de los valores de SNR de cada filtro, con el fin de poder determinar cual es el mas optimo para nuestras señales EMG.

   
|  **Filtro**  |  **SNR Sym8** | **SNR Db4** | **SNR Rbio3.1**
|:------------:|:---------------:|:---------------: |:---------------:
|REPOSO|6.42 dB |0.64 dB|-0.11 dB
|FLEXIÓN|17.15 dB|14.45 dB|3.32 dB
|CONTRAFUERZA| 16.89 dB|23.22 dB |3.10 dB

En el análisis de SNR comparado, el filtro Sym8 emerge como el mejor filtro en general, debido a su rendimiento consistente en todas las condiciones evaluadas. Muestra una SNR de 6,42 dB en reposo, 17,15 dB en flexión y 16,89 dB en contrafuerza, lo que indica una capacidad superior para reducir el ruido y preservar la señal útil en diversas situaciones. La simetría y ortogonalidad del filtro Sym8 contribuyen a su alta eficiencia en la descomposición y reconstrucción de señales, minimizando la distorsión y el ruido introducido. Este filtro es particularmente efectivo en el procesamiento de señales biológicas como las señales EMG, donde la preservación de la integridad de la señal es crucial para un análisis preciso. Además, su capacidad para mantener un alto SNR en múltiples condiciones lo hace especialmente adecuado para aplicaciones en las que se requiere un rendimiento uniforme y confiable. Aunque el filtro Db4 sobresale en condiciones de contrafuerza con una SNR de 23,22 dB, su desempeño es inferior en reposo y flexión comparado con Sym8, haciendo de Sym8 la opción más equilibrada y eficaz para aplicaciones variadas. El filtro Rbio3.1, con SNR de -0,11 dB en reposo, 3,32 dB en flexión y 3,10 dB en contrafuerza, demuestra ser menos eficiente en comparación, resaltando la superioridad del Sym8 en la reducción del ruido y la preservación de la señal en contextos de señales EMG.

### *5.2. Resultado de los parametros estáticos y temporales para EMG* <a name="id9"></a>

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

[2M] «biosignalsnotebooks/biosignalsnotebooks_notebooks/Categories/Extract/temporal_statistical_parameters.ipynb at master · pluxbiosignals/biosignalsnotebooks», GitHub. [En línea]. Disponible en: https://github.com/pluxbiosignals/biosignalsnotebooks/blob/master/biosignalsnotebooks_notebooks/Categories/Extract/temporal_statistical_parameters.ipynb
