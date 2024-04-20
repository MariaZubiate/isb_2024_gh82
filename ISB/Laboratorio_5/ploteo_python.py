# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

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
for x in [ekg_data_1, ekg_data_2, ekg_data_3, ekg_data_4, ekg_data_5]:
    
    columna_emg = x[:, -1]
    
    """Debido a que la señal muestreada por el EMG del BiTalino son del ADC de 10 bits; entonces esta data oscila
    de 0-1023. Pero considerando que el voltaje de operación es de 3.3V, se debe hacer una conversión de 0-1023 a 0-3.3V"""
    columna_Volt = ((columna_emg-507)/1023)*3.3*1000
    """Dado que el BiTalino te brinda el total de datos y no el tiempo, podemos obtener
    la duración del muestreo gracias a la frecuencia de meustreo del BiTalino: 1000 Hz"""
    fs = 1000
    total_data = len(columna_Volt)
    time_total = total_data/fs
    """Teniendo la duración y la cantidad de muestreo, se realizó otra lista para el eje X
    que equivale al Tiempo, con intervalos iguales para obtener un tamaño de lista igual al del Eje Y"""
    time_data = np.linspace(0,time_total, total_data)
    #Para visulaizar solo una porción del gráfico
    t_start = 8.5 # @param {type:"number"}
    t_end = 9.2  # @param {type:"number"}
    index_start = round(t_start*(total_data-1)/time_total)
    index_end = round(t_end*(total_data-1)/time_total)
    #Plotear la señal EMG en el dominio del tiempo
    plt.plot(time_data, columna_Volt)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (mV)')
    
    if x == ekg_data_1:
    
        plt.title('Señal EKG en reposo')
    
    elif x == ekg_data_2:
    
        plt.title('Señal EKG respiración profunda antes del ejercicio')
    
    elif x == ekg_data_3:
    
        plt.title('Señal EKG después del ejercicio')
    
    elif x == ekg_data_4
    
    plt.title('Señal EKG respiración profunda después del ejercicio')
    
    elif x == ekg_data_5:
    
        plt.title('Señal EKG en reposo')
    
    plt.grid(True)
    plt.show()

# Plotear la señal EKG en solo un intervalo del tiempo
plt.plot(time_data[index_start:index_end],columna_Volt[index_start:index_end])
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Intervalo del EKG')
plt.grid(True)
plt.show()
