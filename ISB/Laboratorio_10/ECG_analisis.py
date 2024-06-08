import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import freqz, iirfilter, find_peaks, lfilter, welch

Archivo = "deepbreath_after_exercise.txt"
data = (np.loadtxt(Archivo)[:, -1])
voltaje = (data-512)*3.3/1024*1000
fs = 1000
t = np.linspace(0, len(voltaje)/fs, len(voltaje))
plt.figure(figsize=(20,5))
plt.plot(t, voltaje)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.xlim(0, 10) 
plt.title('Señal ECG - '+Archivo.replace('.txt', '')+' ORIGINAL')
plt.grid()
plt.show()

#ANALIZANDO LA SEÑAL EN FRECUENCIA
# Analizar el Fourier
ecg_senal = voltaje
# Periodo de 2ms (0.002s) o frecuencia de 1000 Hz
T = 0.001
N = len(ecg_senal)
yf = fft(ecg_senal)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
#plt.figure(figsize=(20,10))
#plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
#plt.grid()
#plt.xlabel("Frecuencia")
#plt.ylabel("Magnitud")
#plt.show()

# 2. filtro pasa banda
# Sub filtro pasa bajo
b, a = iirfilter(2, 11.0, btype='lowpass', rs=3, ftype='butter', fs=500)
w, h = freqz(b, a, fs=500)
fpb_signal = lfilter(b, a, ecg_senal)
#plt.figure(figsize=(20,5))
#plt.plot(t,fpb_signal)
#plt.xlim(0, 10) 
#plt.show()

# Sub filtro pasa alto
b, a = iirfilter(1, 5.0, btype='highpass', rs=3, ftype='butter', fs=500)
w, h = freqz(b, a, fs=500)
fpa_signal = lfilter(b, a, fpb_signal)
plt.figure(figsize=(20,5))
plt.plot(t,fpa_signal)
plt.xlim(0, 10)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.title('Señal ECG - '+Archivo.replace('.txt', '')+' FILTRADA')
plt.show()

# Filtro derivativo
b = np.array([-1, -2, 0, 2, 1])
b = (1/8)*b
w, h = freqz(b, 1, fs=500)
fd_signal = lfilter(b, 1, fpa_signal)

# Filtro cuadrado
f_sq = np.square(fd_signal)

# Moving-Window Integration
N = 75
b = np.ones(N-1)
b = (1/N)*b
fi_signal = lfilter(b, 1, f_sq)

# Fiducial Marks
peaks, _ = find_peaks(fi_signal, distance=100)

# Training Part to set Threshold I1 and Threshold I2
# Para las primeras muestras en 2 segundos
# Para efectos del ejercicio vamos a analizar toda la señal
f_samples = len(peaks)
th_I1 = np.max(fi_signal[peaks[:f_samples]])*0.25
th_I2 = 0.5*np.mean(fi_signal[peaks[:f_samples]])
print ("El valor del umbral de pico R de entrada es ", th_I1)
print ("El valor del umbral de ruido de entrada es ", th_I2)
plt.figure(figsize=(20,5))
plt.plot(fi_signal)
plt.plot(peaks, fi_signal[peaks], "x")
plt.hlines(th_I1, 0, len(fi_signal), colors='green')
plt.hlines(th_I2, 0, len(fi_signal), colors='red')
plt.show()

end_qrs = fi_signal > th_I1
roll_qrs_r = np.roll(end_qrs, 1)
roll_qrs_l = np.roll(end_qrs, -1)
end_qrs = np.logical_xor(end_qrs ,roll_qrs_r)
end_qrs = np.logical_and(end_qrs ,roll_qrs_l)

start_qrs = fi_signal < th_I2
roll_qrs_l = np.roll(start_qrs, -1)
roll_qrs_r = np.roll(start_qrs, 1)
start_qrs = np.logical_xor(start_qrs ,roll_qrs_l)
start_qrs = np.logical_and(start_qrs ,roll_qrs_r)

qrs = np.logical_or(start_qrs, end_qrs)
plt.figure(figsize=(20,5))
plt.plot(ecg_senal)
plt.plot(qrs*np.max(ecg_senal))
#plt.xlim(50,10000)
plt.show()


distance = int(0.6 * fs)  # Intervalo mínimo entre picos R (~0.6 segundos)
peaks, _ = find_peaks(qrs, distance=distance)
rr_intervals = np.diff(peaks) / fs * 1000

avnn = np.mean(rr_intervals)
sdnn = np.std(rr_intervals, ddof=1)
diff_rr_intervals = np.diff(rr_intervals)
rmssd = np.sqrt(np.mean(diff_rr_intervals**2))
nn50 = np.sum(np.abs(diff_rr_intervals) > 50)
pnn50 = (nn50 / len(diff_rr_intervals)) * 100

def calculate_psd(rr_intervals, fs=4.0):
    nperseg = min(25, len(rr_intervals) // 2) 
    fxx, pxx = welch(rr_intervals, fs, nperseg=nperseg)
    return fxx, pxx

# Calcular las bandas de frecuencia (VLF, LF, HF)
fxx, pxx = calculate_psd(rr_intervals)

vlf_band = (0.003, 0.04)
lf_band = (0.04, 0.15)
hf_band = (0.15, 0.4)

def bandpower(fxx, pxx, band):
    band_idx = np.logical_and(fxx >= band[0], fxx <= band[1])
    return np.trapz(pxx[band_idx], fxx[band_idx])

vlf = bandpower(fxx, pxx, vlf_band)
lf = bandpower(fxx, pxx, lf_band)
hf = bandpower(fxx, pxx, hf_band)
ratio = lf/hf

# Imprimir resultados
print(f"AVNN: {avnn:.2f} ms")
print(f"SDNN: {sdnn:.2f} ms")
print(f"RMSSD: {rmssd:.2f} ms")
print(f"pNN50: {pnn50:.2f} %")
print(f"VLF: {vlf:.2f} ms^2")
print(f"LF: {lf:.2f} ms^2")
print(f"HF: {hf:.2f} ms^2")
print(f"LF/HF: {ratio:.2f}")

# Graficar PSD
plt.plot(fxx, pxx)
plt.title('Densidad espectral de potencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad de potencia (ms^2/Hz)')
plt.show()