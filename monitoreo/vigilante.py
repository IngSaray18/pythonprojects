import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Ruta del archivo a vigilar
ruta_archivo = "C:/Users/BASE DE DATOS/Desktop/monitoreo/log.txt"

# Palabra a detectar
palabra_a_detectar = "hola"

# Definimos el handler para procesar los eventos
class MiHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Solo si es un archivo y se ha modificado
        if event.is_directory:
            return

        # Abrimos el archivo y leemos su contenido
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            print( contenido )
        # Verificamos si la palabra a detectar está en el contenido
        if palabra_a_detectar in contenido:
            print(f"Se detectó la palabra '{palabra_a_detectar}' en el archivo.")

if __name__ == "__main__":
    event_handler = MiHandler()
    observer = Observer()
    observer.schedule(event_handler, path=ruta_archivo, recursive=False)

    print(f"Vigilando el archivo '{ruta_archivo}' en busca de la palabra '{palabra_a_detectar}'...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
