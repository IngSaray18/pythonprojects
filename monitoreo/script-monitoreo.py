import os
import sys
import requests
import time
import datetime

# Obtenemos la hora actual
hora_actual = datetime.datetime.now()

# Formateamos la hora para imprimir solo la hora y los minutos
hora_formateada = hora_actual.strftime('%H:%M')


def enviar_mensaje(texto):
    url = "https://api.telegram.org/bot5887613867:AAFYM8v_hZZTgF59d9gDRREJc-TT0BsCZ-k/sendMessage"
    params = {
        'chat_id': '-1001804132514',
        'text': texto
    }
    response = requests.post(url, params=params,verify=False)
    if response.status_code == 200:
        print("Mensaje enviado con éxito.")
    else:
        print(f"Error al enviar el mensaje. Código de respuesta: {response.status_code}")
        print(response.text)

def find_file(file_name, folder_path):
    """
    Monitorea constantemente la carpeta especificada en busca del archivo deseado.
    """
    while True:
        files = os.listdir(folder_path)
        if file_name in files:
            file_path = os.path.join(folder_path, file_name)
            print(f"Se encontró el archivo '{file_name}' en la ruta: {file_path}")
            archivo = open('log.txt', 'a')    
            contenido_nuevo = "\nOcaso Finalizó con exito"+hora_formateada
            archivo.write(contenido_nuevo)
            archivo.close()
            #mensaje = "Ocaso Finalizó con exito"+hora_formateada 
            #enviar_mensaje(mensaje)
            sys.exit()
        else:
            print("buscando....")

        time.sleep(5)  # Intervalo de tiempo para verificar la carpeta nuevamente (en segundos).

if __name__ == "__main__":
    target_file_name = "ISR-00000000.TXT"  # Reemplaza "archivo_buscado.txt" con el nombre del archivo que deseas encontrar.
    #folder_path = folder_path = "//192.168.2.176/CajaAhorro/Procesos_Batch/Archivos"  
    folder_path = folder_path = "/home/pedro/Documents/Archivos19"  
    find_file(target_file_name, folder_path)

