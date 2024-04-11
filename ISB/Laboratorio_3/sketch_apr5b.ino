unsigned long lastMsg = 0;
float F = 1000;          // Frecuencia de la señal en Hz
double Fs = 10 * F;      // Frecuencia de muestreo en Hz (10 veces la frecuencia de la señal)
double Ts_ms = (1 / Fs) * 1000;  // Período de muestreo en milisegundos (recíproco de la frecuencia de muestreo)

void setup() {
  Serial.begin(9600);
  while (!Serial);  // Esperar hasta que se inicie la comunicación serial
}

void loop() {
  unsigned long now = millis();  

 
  if (now - lastMsg > Ts_ms) {
    lastMsg = now;  

    double signal_analogica = analogRead(A0);  
    Serial.println(signal_analogica);                                 
  }
}
