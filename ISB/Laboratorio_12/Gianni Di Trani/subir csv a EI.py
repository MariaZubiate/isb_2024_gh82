import pandas as pd
import requests
import os
import time
import hmac
import hashlib
import json
import requests
import csv

def txt_to_csv(txt_file):
    with open(txt_file, "r") as txt:
        lines = txt.readlines()
        txt_data = pd.DataFrame(map(lambda x: map(int, x.split()), lines[lines.index("# EndOfHeader\n")+1:])).iloc[:10000] #primeros 10 segundos
    txt_data = txt_data.loc[:, txt_data.iloc[0] != 0].iloc[:, 0] #obteniendo la señal
    #t = nTs = n/fs = n/(1kHz) = nms
    timestamp = pd.Series(range(0, 10000)) #tiempo en milisegundos
    txt_data = pd.concat([timestamp, txt_data], axis=1)
    txt_data.columns = ["timestamp", "signal"]
    txt_data.to_csv(txt_file.replace("txt", "csv"), header=True, index=False) #timestamp in miliseconds

def read_csv(file_path):
    values = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            try:
                ecg_value = float(row[1])
                values.append([ecg_value])
            except ValueError as e:
                print(f"Skipping row due to error: {e}")
    return values

def upload_ei(_name_label, _values, hmac_key, api_key):
    HMAC_KEY = hmac_key
    API_KEY = api_key
    emptySignature = ''.join(['0'] * 64)

    data = {
        "protected": {
            "ver": "v1",
            "alg": "HS256",
            "iat": time.time()
        },
        "signature": emptySignature,
        "payload": {
            "device_name": "ac:87:a3:0a:2d:1b",
            "device_type": "BiTalino",
            "interval_ms": 1,
            "sensors": [
                { "name": "ECG", "units": "mV" }
            ],
            "values": _values
        }
    }

    encoded = json.dumps(data)

    signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg=encoded.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    data['signature'] = signature
    encoded = json.dumps(data)

    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
                        data=encoded,
                        headers={
                            'Content-Type': 'application/json',
                            'x-file-name': _name_label,
                            'x-api-key': API_KEY
                        })
    if (res.status_code == 200):
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)

pathsEMG = ["biceps_contrafuerza.txt", "pulgar_contrafuerza.txt", "pulgar_flexion.txt"]
hmac_key_EMG = "78c4e277c05ee7365235227000da2bd7"
api_key_EMG = "ei_ed873fc70b4af287ff0b82a8ca3cbe94cf3de590114bb140ea4a497c63d72682"

pathsECG = ["Respiración Profunda Antes del Ejercicio.txt", "Después del Ejercicio.txt", "Respiración Profunda Después del Ejercicio.txt"]
hmac_key_ECG = "608f92986e90cb287dbe23acfdcfaabd"
api_key_ECG = "ei_4a2ee7852d500c640cae73e2dac57a902de0644ffd424d4856d246ed4104b306"

pathsEEG = ["Ejercicio de Parpadeo.txt", "Reposo Luego del Parpadeo.txt", "Resolución Mental de Problemas Matemáticos.txt"]
hmac_key_EEG = "732befd4f6f8a02b1024ee28e29aa5eb"
api_key_EEG = "ei_afe201a424e06a67cde4bcfdfb055d7ec73dd11ae557e59f59958a778e7557fd"

for file_path in pathsEMG:
    txt_to_csv(file_path)
    values = read_csv(file_path.replace("txt", "csv"))
    upload_ei("EMG."+file_path.replace(".txt", ""), values, hmac_key_EMG, api_key_EMG)

for file_path in pathsECG:
    txt_to_csv(file_path)
    values = read_csv(file_path.replace("txt", "csv"))
    upload_ei("ECG."+file_path.replace(".txt", ""), values, hmac_key_ECG, api_key_ECG)

for file_path in pathsEEG:
    txt_to_csv(file_path)
    values = read_csv(file_path.replace("txt", "csv"))
    upload_ei("EEG."+file_path.replace(".txt", ""), values, hmac_key_EEG, api_key_EEG)
