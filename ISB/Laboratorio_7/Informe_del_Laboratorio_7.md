

# Laboratorio 7
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
     4.1 [Generar filtro FIR e IIR para ECG](#id5)\
     4.2 [Generar filtro FIR e IIR para EMG](#id6)\
     4.3 [Generar filtro FIR e IIR para EEG](#id7) 
5. [Resultados](#id8)\
     5.1 [Resultado de señal filtrada con filtro FIR e IIR para ECG](#id9)\
     5.2 [Resultado de señal filtrada con filtro FIR e IIR para EMG](#id10)\
     5.3 [Resultado de señal filtrada con filtro FIR e IIR para EEG](#id11) 
7.  [Bibliografia](#id12)
   
## *1. Introducción* <a name="id1"></a>

## *2. Objetivos* <a name="id2"></a>
ECG:
- Diseñar 1 filtros IIR, deben elegir si es Bessel, Butterworth, Chebyshev o Eliptico. 
- Diseñar 1 filtros FIR, elegir 2 métodos de ventana pueden ser: Hanning, Hamming, Bartlett, rectangular o Blackman
  
EMG:
- Eliminar frecuencias altas que correspondan a ruido eléctrico y artefactos de movimiento
- Aislar la banda de frecuencia de interés que corresponde a la actividad muscular.
  
EEG
- Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas
cerebrales específicas.

## *3. Materiales y equipos* <a name="id3"></a>

| Cantidad |	Material o equipo |	Uso
|:------------:|:---------------:|:------------:|
| 1	| Laptop	| Visualización y procesamiento de las señales con lenguaje de programación

## *4. Metodologia* <a name="id4"></a>

### *4.1. Generar filtro FIR e IIR para ECG* <a name="id5"></a>

#### 4.1.1. Filtro IIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)

#### 4.1.1. Filtro FIR (Bessel, Butterworth, Chebyshev o Eliptico)


### *4.2. Generar filtro FIR e IIR para EMG* <a name="id6"></a>

#### 4.2.1. Filtro IIR (2 métodos de ventana pueden ser:  Hamming,Bartlett o Blackman)

#### 4.2.1. Filtro FIR ( Bessel, Butterworth, Chebyshev o Eliptico)


### *4.3. Generar filtro FIR e IIR para EEG* <a name="id7"></a>

#### 4.3.1. Filtro IIR (2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman)

#### 4.3.1. Filtro FIR (Bessel, Butterworth, Chebyshev o Eliptico)


## *5. Resultados* <a name="id8"></a>

### *5.1. Resultado de señal filtrada con filtro FIR e IIR para ECG* <a name="id9"></a>

|  **Campo**  |  **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|BASAL |              |             |              |
|RESPIRACIÓN |              |             |              |
|POST-EJERCICIO |              |             |              |


### *5.2. Resultado de señal filtrada con filtro FIR e IIR para EMG* <a name="id10"></a>

|  **Campo**  | **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|DESCANSO |              |             |              |
|CONTRACCIÓN LEVE |              |             |              |
|CONTRACCIÓN FUERTE |              |             |              |

### *5.3. Resultado de señal filtrada con filtro FIR e IIR para EEG* <a name="id11"></a>


|  **Campo**  | **Señal cruda** | **Señal filtrada con IIR** |  **Señal filtrada con FIR** |
|:------------:|:---------------:|:------------:| :------------:|
|REPOSO | ![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/3cdcd4b2-5044-40db-901c-0ffc6681cdd5)|             |              |
|PARPADEO |![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/999f8e54-e518-4279-bcda-4034d63fa96e)|             |              |
|REPOSO DESPUES DEL PARPADEO|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/5eb427eb-cc41-48f1-a77b-a583dc587240)|             |              |
|RESOLUCIÓN MENTAL DE EJERCICIO DE MATEMATICAS|![image](https://github.com/MariaZubiate/isb_2024_gh82/assets/164455359/a92defc5-6f50-4fc3-a07d-b31dae541698)|             |              |



## *6. Bibliografia* <a name="id12"></a>
[1] “A-15 Dispositivos y Circuitos Electrónicos II Ingeniería Electrónica Filtros Activos.” Available: https://www.fceia.unr.edu.ar/dce2/Files/Apuntes/FILTROS ACTIVOS - Notas de Clase (v-2019-1).pdf
