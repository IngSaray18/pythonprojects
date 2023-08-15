import requests
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
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Mensaje enviado con éxito.")
    else:
        print(f"Error al enviar el mensaje. Código de respuesta: {response.status_code}")
        print(response.text)

# Sustituye 'TU_TOKEN' con el token de tu bot y 'TU_CHAT_ID' con el ID del chat donde quieras enviar el mensaje.

mensaje = "ESTO ES UNA PRUEBA. "+hora_formateada 

enviar_mensaje(mensaje)



