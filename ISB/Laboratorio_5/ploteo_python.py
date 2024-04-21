#Colab: https://colab.research.google.com/drive/1LaV0_U16Gzb0AwwZkRcST7dJQutWNATs?usp=sharing
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')

# Cargar los datos de la señal EKG desde el archivo de texto

#En reposo
ekg_data_1 = np.loadtxt('1D_muñeca_reposo.txt')

#Respiración profunda antes del ejercicio
ekg_data_2 = np.loadtxt('1D_muñeca_deep_breath.txt')

#Después del ejercicio
ekg_data_3 = np.loadtxt('1D_muñeca_burpees.txt')

#Respiración profunda después del ejercicio
ekg_data_4 = np.loadtxt('1D_muñeca_deepbreath_after_ex.txt')

#Paro cardiaco
ekg_data_5 = np.loadtxt('prosim_cardiac_death.txt')

# Seleccionar la última columna que contiene los valores de la señal EKG
for x in [ekg_data_1, ekg_data_2, ekg_data_3, ekg_data_4]:
    columna_ekg = x[:, -1]
    """Debido a que la señal muestreada por el EKG del BiTalino son del ADC de 10 bits; entonces esta data oscila
    de 0-1023. Pero considerando que el voltaje de operación es de 3.3V, se debe hacer una conversión de 0-1023 a 0-3.3V"""
    columna_Volt = ((columna_ekg-507)/1023)*3.3*1000
    """Dado que el BiTalino te brinda el total de datos y no el tiempo, podemos obtener
    la duración del muestreo gracias a la frecuencia de meustreo del BiTalino: 1000 Hz"""
    fs = 1000
    total_data = len(columna_Volt)
    time_total = total_data/fs
    """Teniendo la duración y la cantidad de muestreo, se realizó otra lista para el eje X
    que equivale al Tiempo, con intervalos iguales para obtener un tamaño de lista igual al del Eje Y"""
    time_data = np.linspace(0, time_total, total_data)
    #Para visulaizar solo una porción del gráfico
    t_start = 8.5 # @param {type:"number"}
    t_end = 9.2  # @param {type:"number"}
    index_start = round(t_start*(total_data-1)/time_total)
    index_end = round(t_end*(total_data-1)/time_total)
    #Plotear la señal EKG en el dominio del tiempo
    plt.plot(time_data, columna_Volt)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    if x is ekg_data_1:
        plt.title('Señal EKG en Reposo')
    elif x is ekg_data_2:
        plt.title('Señal EKG Respiración Profunda antes del Ejercicio')
    elif x is ekg_data_3:
        plt.title('Señal EKG después del Ejercicio')
    else:
        plt.title('Señal EKG Respiración Profunda después del Ejercicio')
    plt.grid()
    plt.show()
    plt.plot(time_data, columna_Volt)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    if x is ekg_data_1:
        plt.title('Intervalo de la Señal EKG en Reposo')
    elif x is ekg_data_2:
        plt.title('Intervalo de la Señal EKG Respiración Profunda antes del Ejercicio')
    elif x is ekg_data_3:
        plt.title('Intervalo de la Señal EKG después del Ejercicio')
    else:
        plt.title('Intervalo de la Señal EKG Respiración Profunda después del Ejercicio')
    plt.xlim([10, 20])
    plt.grid()
    plt.show()
    plt.plot(time_data, columna_Volt)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    if x is ekg_data_1:
        plt.title('Un Ciclo de la Señal EKG en Reposo')
    elif x is ekg_data_2:
        plt.title('Un Ciclo de la Señal EKG Respiración Profunda antes del Ejercicio')
    elif x is ekg_data_3:
        plt.title('Un Ciclo de la Señal EKG después del Ejercicio')
    else:
        plt.title('Un Ciclo de la Señal EKG Respiración Profunda después del Ejercicio')
    plt.xlim([11.5, 12.5])
    plt.grid()
    plt.show()
columna_ekg = ekg_data_5[:, -1]
"""Debido a que la señal muestreada por el EKG del BiTalino son del ADC de 10 bits; entonces esta data oscila
de 0-1023. Pero considerando que el voltaje de operación es de 3.3V, se debe hacer una conversión de 0-1023 a 0-3.3V"""
columna_Volt = ((columna_ekg-507)/1023)*3.3*1000
"""Dado que el BiTalino te brinda el total de datos y no el tiempo, podemos obtener
la duración del muestreo gracias a la frecuencia de meustreo del BiTalino: 1000 Hz"""
fs = 1000
total_data = len(columna_Volt)
time_total = total_data/fs
"""Teniendo la duración y la cantidad de muestreo, se realizó otra lista para el eje X
que equivale al Tiempo, con intervalos iguales para obtener un tamaño de lista igual al del Eje Y"""
time_data = np.linspace(0, time_total, total_data)
#Para visulaizar solo una porción del gráfico
t_start = 8.5 # @param {type:"number"}
t_end = 9.2  # @param {type:"number"}
index_start = round(t_start*(total_data-1)/time_total)
index_end = round(t_end*(total_data-1)/time_total)
#Plotear la señal EKG en el dominio del tiempo
plt.plot(time_data, columna_Volt)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal EKG del Prosim')
plt.grid()
plt.show()
plt.plot(time_data, columna_Volt)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal EKG del Prosim')
plt.grid()
plt.xlim([0, 40])
plt.show()
plt.plot(time_data, columna_Volt)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal EKG del Prosim')
plt.grid()
plt.xlim([40, 70])
plt.show()
plt.plot(time_data, columna_Volt)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal EKG del Prosim')
plt.grid()
plt.xlim([70, 100])
plt.show()
plt.plot(time_data, columna_Volt)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal EKG del Prosim')
plt.grid()
plt.xlim(left=100)
plt.show()
