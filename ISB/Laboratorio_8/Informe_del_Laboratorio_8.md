
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
     4.1 [Generar filtro Walete para ECG](#id5)\
     4.2 [Generar filtro Walete para EMG](#id6)\
     4.3 [Generar filtro Walete para EEG](#id7)
5. [Resultados](#id8)\
     5.1 [Resultado de señal filtrada con filtro Walete para ECG](#id9)\
     5.2 [Resultado de señal filtrada con filtro Walete para EMG](#id10)\
     5.3 [Resultado de señal filtrada con filtro Walete para EEG](#id11)
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



## *2. Objetivos* <a name="id2"></a>

Preprocesar señales EEG, EMG y ECG para reducir el ruido y extraer características de interés, con el uso de filtros Walete.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Generar filtro Walete para ECG* <a name="id5"></a>



### *4.2. Generar filtro Walete para EMG* <a name="id6"></a>




### *4.3. Generar filtro Walete para EEG* <a name="id7"></a>
Para la elaboración de este filtro se tomo en cuenta el artículo "Ocular Artifact Removal Method Based on the Wavelet and ICA Transform" Este nos permitio poder escoger la familia, el nivel de descomposición y los coeficientes necesarios para realizar el filtro Wavelet[1M]. 

En este caso se usaran los siguientes parametros:

1. Se utilizara el wavelets Symlet por ser casi simétrica, ortogonal y adecuada para la eliminación de artefactos oculares. Por ellos posee una alta correlación con los artefactos de parpadeo, lo que permite una eliminación eficaz de estos artefactos sin afectar significativamente nuestras señales.
2. El nivel de descomposición sera de 8 lo cual permite descomponer la señal en componentes y aproximados en diferentes escalas de tiempo. Con ello podremos identificar y eliminar artefactos en en bandas de frecuencia que deseamos.Como son los artefactos de parpadeo que se encuentran en la banda de 0.5 a 3.5Hz
3. Se eliminara los coeficientes D1 y D8, así como el coeficiente de aproximación A8 debido a que contiene componentes de artefactos oculares, segun el artículo.





## *5. Resultados* <a name="id8"></a>

### *5.1. Resultado de señal filtrada con filtro Walete para ECG* <a name="id9"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada ** |  
|:------------:|:---------------:|:------------:
|BASAL |![descarga (20)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/81677ad1-ccd6-474e-ac63-8acddc17fd10)| ---------
|FFTS EN BASAL |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/9cb53059-f74e-4523-9aa2-3e66c824a403)| ---------  
|RESPIRACIÓN | ![descarga (21)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/6b3fdf15-fe55-4830-8dbb-57ee7cc6ec86) | ---------
|FFTS PARA RESPIRACIÓN |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/89bfd2ef-aae1-4d4f-aa1c-280494c8a01f)| ---------   
|POST-EJERCICIO | ![descarga (22)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/c54ed6a5-9a23-49a8-8e1f-0956ad76132e) | ---------  
|FFTS POST-EJERCICIO | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/2917ffb0-fa18-4224-a96a-39ee38a4239f) | ---------
|RESPIRACIÓN PROFUNDA POST-EJERCICIO |![descarga (23)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/a684930a-f559-4256-8099-b2e4764da05a)| ---------
|FFTS RESPIRACIÓN PROFUNDA POST-EJERCICIO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164538247/7d22bcce-7237-4384-9e57-3af6d0e833a0)| ---------

### *5.2. Resultado de señal filtrada con filtro Walete para EMG* <a name="id10"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada ** |  
|:------------:|:---------------:|:------------:
|REPOSO |![Captura de pantalla 2024-05-04 163706](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/161761df-f746-4a7b-be6a-45a583bf073a)| ---------
|FFTS EN REPOSO |![Captura de pantalla 2024-05-04 165546](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/083e4128-2e7f-45eb-a885-aa00f8c2def3)| ---------  
|FLEXIÓN | ![Captura de pantalla 2024-05-04 172935](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/e1116ccf-37ba-4d18-b726-19fdd4f948d5)| ---------
|FFTS PARA FLEXIÓN |![Captura de pantalla 2024-05-04 173201](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/085fd781-2ce0-4b6f-a08e-b05a43a87e14)| ---------   
|CONTRAFUERZA | ![Captura de pantalla 2024-05-04 225121](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/b90adc10-e045-42c7-98aa-5fa5b1111199) | ---------  
|FFTS CONTRAFUERZA |![Captura de pantalla 2024-05-04 225256](https://github.com/MariaZubiate/isb_2024_gh82/assets/164566714/0ab9aa19-2850-4731-8d84-6080f9511dc7) | ---------



### *5.3. Resultado de señal filtrada con filtro Walete para EEG* <a name="id11"></a>

|  **Campo**  | **Señal cruda** | **Señal filtrada ** |  
|:------------:|:---------------:|:------------:
|REPOSO | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3cdcd4b2-5044-40db-901c-0ffc6681cdd5)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/0b8830a8-0e1e-47b0-a374-d2087356d02b)
|FFTS DEL REPOSO |![descarga (4)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/69ad7621-c340-4797-9c4e-3596f8ef7a5b)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/f42ceb2b-ce41-4ec9-af23-fbccf4665687)
|PARPADEO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/999f8e54-e518-4279-bcda-4034d63fa96e)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/23028e8f-e64b-4a04-9b00-909c7fed1d34)
|FFTS DEL PARPADEO |![descarga (5)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/579bde96-5db5-47f2-b4e8-d88fe0843fd7)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/65874fb0-4bed-4a5e-9837-12cb504c5e76)
|REPOSO DESPUES DEL PARPADEO| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5eb427eb-cc41-48f1-a77b-a583dc587240)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/374bb29e-a069-44d6-8583-90f8c728a82c)
|FFTS DEL REPOSO DESPUES DEL PARPADEO | ![descarga (6)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/8228f968-755c-44a7-9725-532f70311187) | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/62aa61de-f586-4d3a-83c7-bf2038629b40)
|RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a92defc5-6f50-4fc3-a07d-b31dae541698)| ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/6dee0631-2d53-42b7-924d-2b35c7e27ee6)
|FFTS DE LA RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS | ![descarga (7)](https://github.com/MariaZubiate/isb_2024_gh82/assets/43424450/0552020e-a55e-47d9-9b1e-e872b3216ac1)|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/b3b446e4-4987-44cc-abde-72173160bb03)





## *6. Conclusiones* <a name="id12"></a>



## *7. Bibliografia* <a name="id13"></a>
[1] Samir Kouro R, Rodrigo Musalem M. "Tutorial introductorio a la Teoróa de Wavelet".2002. Available: http://www2.elo.utfsm.cl/~elo377/documentos/Wavelet.pdf



[1M] E. Erkan y Y. Erkan, "Ocular Artifact Removal Method Based on the Wavelet and ICA Transform," Chaos Theory and Applications, vol. 5, no. 2, pp. 111-117, 2023, doi: 10.51537/chaos.1268949. Available: https://dergipark.org.tr/en/download/article-file/3026859
