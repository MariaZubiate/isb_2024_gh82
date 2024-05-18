
# Laboratorio 8
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
     4.1 [Generar filtro Wavelet para ECG](#id5)\
     4.2 [Generar filtro Wavelet para EMG](#id6)\
     4.3 [Generar filtro Wavelet para EEG](#id7)
5. [Resultados](#id8)\
     5.1 [Resultado de señal filtrada con filtro Wavelet para ECG](#id9)\
     5.2 [Resultado de señal filtrada con filtro Wavelet para EMG](#id10)\
     5.3 [Resultado de señal filtrada con filtro Wavelet para EEG](#id11)
   
7. [Conclusiones](#id12)
8. [Bibliografia](#id13)
   
## *1. Introducción* <a name="id1"></a>

Un filtro Wavelet es una herramienta utilizada en el procesamiento de señales que se basa en la teoría de Wavelet. Las Wavelets son funciones matemáticas que permiten analizar señales en diferentes escalas de tiempo y frecuencia, lo que las hace ideales para detectar cambios locales en una señal. Los filtros Wavelet se utilizan para descomponer una señal en sus componentes de alta y baja frecuencia, lo que facilita el análisis de detalles finos y gruesos por separado. Estos filtros son fundamentales en aplicaciones como la eliminación de ruido, la compresión de datos y la detección de bordes en imágenes. En este laboratorio, exploraremos cómo utilizar los filtros Wavelet para mejorar la calidad de la reconstrucción de señales y optimizar el proceso de análisis de datos[1].


<p align="center">
  <img src="https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/9faae516-3603-4289-b428-41ea51108c3a" alt="Esquema de la Transformada Wavelet" width="50%">
</p>
<p align="center">
Figura 1. Esquema de la Transformada Wavelet[1]
</p>

Los filtros wavelet pertenecer a diversas familias que se distinguen por sus propiedades matemáticas y aplicaciones específicas. Algunas de ellas son[2]:

1. Vavelets de Haar:
   Este es el wavelet más simple y primera en ser introducida, se caracteriza por su forma        escalonada, ideal para aplicaciones simples de compresión y procesamiento de señales. Con      propiedades ortogonales y simetricas

2. Wavelets de Daubechies:
   Estas tienen una longitud de soporte compacta y una alta regularidad. Se denominan             comúnmente como DN, donde N indica el número de coeficientes. Utilizadas en aplicaciones       que requieren una alta precisión en la reconstrucción de la señal.

3. Wavelets de Coiflet:
   Tiene  buenas propiedades de localización en el dominio del tiempo y frecuencia. Adecuadas     para el análisis multirresolución y aplicaciones de compresión de imagenes.

4. Wavelets de Symlet:
   Es una modificacion de las wavelets de Daubechies para mejorar la simetría. Manteniendo las    propiedades de ortogonalidad y longitud de soporte compacta.

5. Wavelets B-Spline:
   Estas son usadas en gráficos computacionales y procesamiento de imágenes. Ofreciendo una       buena representación suave de la señal.

Los niveles de descomposición en la transfomración wavelet determinan la cantidad de detalle que se puede extraer de una señal. Cada nivel representa una escala diferente de la señal orginal. Cada nivel proporciona una descomposición más detallada de la señal. La señal se analiza en bandas de frecuencia cada vez más bajas, lo que permite visualizar mejor la señal[2].

## *2. Objetivos* <a name="id2"></a>

Preprocesar señales EEG, EMG y ECG para reducir el ruido y extraer características de interés, con el uso de filtros Wavelet.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Generar filtro Wavelet para ECG* <a name="id5"></a>
La wavelet Daubechies (db4) con un nivel de descomposición de 8 proporciona los resultados más eficientes para la clasificación de señales ECG [3].

### *4.2. Generar filtro Wavelet para EMG* <a name="id6"></a>
Para realizar el filtrado se tomó en cuenta el artículo "Non-invasive detection of low-level muscle fatigue using surface EMG with wavelet decomposition", de donde se obtuvo la elección de la familia, niveles de descomposición y coeficientes necesarios a utilizar.
Se usó la función Wavelet Sym8, debido a que con ello obtuvieron un rendimiento superior a comparación de los demás Symmlets. Asimismo, utilizaron 9 niveles de descomposición. Y para el posprocesamiento, debido al bajo contenido de potencia y la presencia de artefactos de baja frecuencia como artefactos de movimiento, se eliminaron los niveles 1, 8 y 9; quedándose solo con los  niveles de la siguiente tabla [4].

![Captura de pantalla 2024-05-17 180143](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/4a548785-5ac7-4b82-9574-9db7e11d3f95)

### *4.3. Generar filtro Wavelet para EEG* <a name="id7"></a>
Para la elaboración de este filtro se tomo en cuenta el artículo "Ocular Artifact Removal Method Based on the Wavelet and ICA Transform" Este nos permitio poder escoger la familia, el nivel de descomposición y los coeficientes necesarios para realizar el filtro Wavelet[5]. 

En este caso se usaran los siguientes parametros:

1. Se utilizara el wavelets Symlet por ser casi simétrica, ortogonal y adecuada para la eliminación de artefactos oculares. Por ellos posee una alta correlación con los artefactos de parpadeo, lo que permite una eliminación eficaz de estos artefactos sin afectar significativamente nuestras señales.
2. El nivel de descomposición sera de 8 lo cual permite descomponer la señal en componentes y aproximados en diferentes escalas de tiempo. Con ello podremos identificar y eliminar artefactos en en bandas de frecuencia que deseamos.Como son los artefactos de parpadeo que se encuentran en la banda de 0.5 a 3.5Hz
3. Se eliminara los coeficientes D1 y D8, así como el coeficiente de aproximación A8 debido a que contiene componentes de artefactos oculares, segun el artículo.

## *5. Resultados* <a name="id8"></a>

En el siguiente inciso se podrán visualizar los filtros utilizados en los diferentes ensayos realizados en los laboratorios, así como el uso del filtro wavelet para filtrar las señales y realizar un análisis detallado.

### *5.1. Resultado de señal filtrada con filtro Wavelet para ECG* <a name="id9"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada** |  
|:------------:|:---------------:|:------------:
|BASAL |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/0ecbdc0b-81ce-4433-8f35-cb51b049f907)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/6e087175-54a7-47bf-83bd-1133a7761d7e)|FFTS EN BASAL |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/6fa7fdc3-9c6e-45cd-80dc-913647971f98)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/4f99ab33-920c-451b-804d-072e60b8367e)|RESPIRACIÓN |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/76799d56-03e5-4de9-8a2e-f1632c4c5c38)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/8f5eb3c8-8e21-4b5c-b546-69df59cbcf8b)|FFTS PARA RESPIRACIÓN |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/0f356748-c6de-4126-a2b5-894975c3faf0)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/07b596bb-fdfc-41ca-be10-3083e152d781)|POST-EJERCICIO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/854a1351-8a49-4b4c-864a-e124e921eecc)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/fc2cddf0-bac6-452b-b1f5-f6ef684b44ca)|FFTS POST-EJERCICIO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/9fb0653b-22bb-4e6b-b5b6-e26fff313096)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/8f2afe92-2027-4984-86c7-7c648a5ee0ef)|RESPIRACIÓN PROFUNDA POST-EJERCICIO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/84f637fc-670d-4fc2-abcc-a3d5922edcd1)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/aa8d0437-3149-429e-a674-a38817d6ab25)|FFTS RESPIRACIÓN PROFUNDA POST-EJERCICIO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/09623992-35e6-45bd-bb43-30ac58db40c3)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/2744d0c0-1065-4da2-a7bb-bbf2bc6d5c60)


### *5.2. Resultado de señal filtrada con filtro Wavelet para EMG* <a name="id10"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada** |  
|:------------:|:---------------:|:------------:|
|REPOSO |![Captura de pantalla 2024-05-17 180251](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/d06ebc6e-afe8-4a94-8a61-36c8f438cd19)|![Captura de pantalla 2024-05-17 180432](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/651a07f2-b618-40b2-983c-0b8f246a783a)|
|FFTS EN REPOSO |![Captura de pantalla 2024-05-17 180501](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/69900781-f7cf-459d-b199-62f6001a165d)|![Captura de pantalla 2024-05-17 180525](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/86a6a634-185a-4d10-b6cb-a1fbff9abbae)|
|FLEXIÓN |![Captura de pantalla 2024-05-17 181030](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/aedb92be-4333-4aa2-8752-c0ddfc640a87)|![Captura de pantalla 2024-05-17 181057](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/b0b50d0c-1ec6-4dc6-a98e-3e4889a5df0d)|
|FFTS PARA FLEXIÓN |![Captura de pantalla 2024-05-17 180607](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e1034de8-01f4-4e40-9892-a3d54941f2a5)|![Captura de pantalla 2024-05-17 180638](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/1cc8424d-7cf0-4d40-8771-4bc4db185843)|
|CONTRAFUERZA |![Captura de pantalla 2024-05-17 181350](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/3ff9322e-2a95-4af8-a30d-96ba5a5bdb6d)|![Captura de pantalla 2024-05-17 181414](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/00203b3b-cb4f-42b5-ac8b-ac1085828a72)|
|FFTS CONTRAFUERZA |![Captura de pantalla 2024-05-17 180712](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/843027f0-270c-4385-ae0b-0a82d806fe10)|![Captura de pantalla 2024-05-17 180733](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/90b38afc-d934-4e67-b164-bec727191764)|

### *5.3. Resultado de señal filtrada con filtro Wavelet para EEG* <a name="id11"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada por Wavelet** |  **Descripción** |
|:------------:|:---------------:|:------------:|:------------:|
|REPOSO |![descarga (28)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/9592f000-7a45-45b4-aade-b5280910f64b)| ![descarga (36)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/b46b82ea-223a-4d64-985c-9081820bae87)|Amplitud de señal original: ±1500 mV, Amplitud de señal filtrada: ±500 mV, Amplitud del ruido eliminado: ±200 mV |
|FFTS EN REPOSO |![descarga (29)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/51a91047-e409-47a4-9817-d5f3597f2ecb)|![descarga (37)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/e7e7a4e0-361c-4c74-b748-e1d1314507e7)| |
|EJERCICIO DE PARPADEO |![descarga (30)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/f04196af-1997-472b-9672-dd03a5f03878)|![descarga (38)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/87ed8b1c-25cf-4608-8045-70086ae4332c)| Amplitud de señal original: ±600 mV, Amplitud de señal filtrada: ±200 mV y Amplitud del ruido eliminado: ±75 mV|
|FFTS PARA EJERCICIO DE PARPADEO | ![descarga (31)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/24c15dc5-354d-420b-ae86-899e6f8a0844)|![descarga (39)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6d0d8cf6-b680-4f6e-bac3-0b2afcb8f969)| |
|REPOSO LUEGO DEL PARPADEO | ![descarga (32)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/8d18a2fc-741a-4ffb-aed7-fa59f2253b6d)|![descarga (40)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/e281702e-e1c1-443f-96de-29d205be8a07)| Amplitud de señal original: ±1500 mV, Amplitud de señal filtrada: ±500 mV y Amplitud del ruido eliminado: ±200 mV|
|FFTS REPOSO LUEGO DEL PARPADEO |![descarga (33)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/68d62c20-2c7a-4727-b962-6526011b20c2)|![descarga (41)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/98be4b60-e3bd-44f8-a0ef-b476f22974c0)| |
|RESOLUCIÓN MENTAL DE PROBLEMAS MATEMÁTICOS |![descarga (34)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/33a8e1fc-f2fa-45d3-937b-8cf5d635eed3)|![descarga (42)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/8dabeed1-560a-4d34-8bc2-9a045e46799c)|Amplitud de señal original: ±1500 mV, Amplitud de señal filtrada: ±500 mV y Amplitud del ruido eliminado: ±200 mV |
|FFTS RESOLUCIÓN MENTAL DE PROBLEMAS MATEMÁTICOS | ![descarga (35)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/671b7b3a-96b9-4a96-a20b-9a5bcad03689)|![descarga (43)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/a4d9cdd4-f52f-4bd8-8398-5729a00b1de9)| |





A continuación se mostrará un ejemplo de la obtención de los niveles obtenidos para una de las señales. En este caso, se tomó como ejemplo la Señal EMG en Contrafuerza, teniendo en cuenta 9 niveles:

![Captura de pantalla 2024-05-17 184437](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/c50d7965-c8dd-4bbe-aabb-bd426eea5bee)


## *6. Conclusiones* <a name="id12"></a>
ECG

EMG

En el filtrado de señales EEG, para los tres experimentos de reposo, reposo luego del parpadeo y la resolución de problemas matemáticos se logró una reducción significativa del ruido(aproximadamente un 67% respecto a la amplitud máxima) y, además, se mantuvieron las componentes en baja frecuencia cruciales para analizar señales EEG, lo que demuestra un filtrado selectivo. En el caso del ejercicio de parpadeo, aún se observan picos lo que nos indica es difícil eliminarla por completo con la metodología propuesta. Para todos los experimentos se obtuvo un promedio de reducción de entre 10%-21% en la amplitud de los picos de la FFT.



## *7. Bibliografia* <a name="id13"></a>
[1] Samir Kouro R, Rodrigo Musalem M. "Tutorial introductorio a la Teoróa de Wavelet".2002. Available: http://www2.elo.utfsm.cl/~elo377/documentos/Wavelet.pdf

[2] Daubechies. "Ten Lectures of Wavelets". 1992. Available: https://jqichina.wordpress.com/wp-content/uploads/2012/02/ten-lectures-of-waveletsefbc88e5b08fe6b3a2e58d81e8aeb2efbc891.pdf

[3] Singh, R., Mehta, R., & Rajpal, N. (2018). Efficient wavelet families for ECG classification using neural classifiers. Procedia Computer Science, 132, 11–21. https://doi.org/10.1016/j.procs.2018.05.054

[4] G. Zhang, E. Morin, Y. Zhang, and S. Ali Etemad, “Non-invasive detection of low-level muscle fatigue using surface EMG with wavelet decomposition,” PubMed, Jul. 2018, doi: https://doi.org/10.1109/embc.2018.8513588.
‌

[5] E. Erkan y Y. Erkan, "Ocular Artifact Removal Method Based on the Wavelet and ICA Transform," Chaos Theory and Applications, vol. 5, no. 2, pp. 111-117, 2023, doi: 10.51537/chaos.1268949. Available: https://dergipark.org.tr/en/download/article-file/3026859
