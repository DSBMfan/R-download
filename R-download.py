from pytube import YouTube
import yt_dlp
import pyfiglet
from colorama import *
init()

text = pyfiglet.figlet_format(text="          R/download",
                              font="big")

print(Fore.CYAN+Style.BRIGHT + text)

def descargar_video_youtube(url, destino='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(Fore.RED+Style.BRIGHT + f'Descargando {yt.title}...')
        video.download(destino)
        print(Fore.RED+Style.BRIGHT + 'Descarga completada!')
    except Exception as e:
        print(f'Error al descargar el video de YouTube: {e}')

def descargar_video_otras_plataformas(url, destino='.'):
    try:
        ydl_opts = {
            'outtmpl': f'{destino}/%(title)s.%(ext)s',
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(Fore.RED+Style.BRIGHT + 'Descarga completada!')
    except Exception as e:
        print(Fore.RED+Style.BRIGHT + f'Error al descargar el video: {e}')

def seleccionar_plataforma():
    while True:
        print("\n=== R/download ===\n")
        print("|01| YouTube")
        print("|02| Instagram")
        print("|03| Facebook")
        print("|04| TikTok")
        print("|05| Regresar al menú principal\n")
        opcion = input("Seleccione una plataforma: ")

        if opcion in ['1', '2', '3', '4']:
            url = input("Ingrese la URL del video: ")
            destino = input("Ingrese la ruta al directorio donde quiera guardar el video (déjelo en blanco para el directorio actual): ")
            destino = destino if destino else '.'
            if opcion == '1':
                descargar_video_youtube(url, destino)
            else:
                descargar_video_otras_plataformas(url, destino)
        elif opcion == '5':
            break
        else:
            print(Fore.RED+Style.BRIGHT + "Opción no válida. Por favor, intente de nuevo.")

def menu():
    while True:
        print(Fore.RED +"\n=== R/download ===\n")
        print("|01| Seleccionar plataforma y descargar video\n")
        print("|02| Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            seleccionar_plataforma()
        elif opcion == '2':
            print("Saliendo del programa... Gracias por usar R-download\n")
            print(Fore.CYAN+Style.NORMAL + "          Hecho por Rodrigo Lopez")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
