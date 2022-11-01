'''
==== Descripción ====
Nombre: Jorge Martínez López 
Matrícula: A0704518
Programa para descargar videos de youtube
=====================
'''
'''
==== LIBRERÍAS ====
Importamos la librería pytube
https://pytube.io/en/latest/
pytube es una biblioteca liviana, Pythonic, libre de dependencias (y una utilidad de línea de comandos) para descargar videos de YouTube.
Importamos la libería progessbar 
https://progressbar-2.readthedocs.io/en/latest/
Una barra de progreso de texto generalmente se usa para mostrar el progreso de una operación de ejecución prolongada,
lo que brinda una indicación visual de que el procesamiento está en marcha.
===================
'''
from pytube import YouTube # pip install pytube
import progressbar # pip install progressbar 

'''
==== FUNCIÓN ====
La función iteración tiene la finalidad de actualización de los chunk para poder
mostrar el progbreso de la barra.
=================
'''
chunks=0
def iteracion(stream=None,chunk=None,file_handle=None,remaining=None):
    global bar, chunks
    chunks+=len(chunk)
    bar.update(chunks)
'''
==== LOOP ====
La función de este loop es estar repitiendo la intrucciones 
==============
'''
print('''
╭━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
╰╮╭╮┃╭━━┫╭━╮┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃
╱┃┃┃┃╰━━┫╰━━┫┃╱╰┫┃╱┃┃╰━╯┃┃╱╰┫┃╱┃┃
╱┃┃┃┃╭━━┻━━╮┃┃╱╭┫╰━╯┃╭╮╭┫┃╭━┫╰━╯┃
╭╯╰╯┃╰━━┫╰━╯┃╰━╯┃╭━╮┃┃┃╰┫╰┻━┃╭━╮┃
╰━━━┻━━━┻━━━┻━━━┻╯╱╰┻╯╰━┻━━━┻╯╱╰╯
''')
while True:

    # Intriduce la URL
    link = input('URL de YOUTUBE >>> ')
    print('CARGANDO...')
    # Si escribes break rompe el loop
    if link == "break":
        print('FINALIZADO')
        break
    
    try: # Descarga el video 
        # 
        video=YouTube(link,on_progress_callback=iteracion)
        # Carga el video de youtube y lo guarda en la variable video_descarga 
        '''
        Se descargan los video con una resolución 720p
        https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/
        '''
        video_descarga=video.streams.filter(resolution='720p').first()

        # Barra de descarga 
        '''
        Llamos las fucniones y la sintaxis adecuada señalizar bar 
        -> Se toma como parametro de maxval= video_descarga.filesize, toma el valor de video 
        -> widgets: es el formato para mostra como va estar el bar 
            DESCARGANDO... Nombre del video Porcentaje de la descarga | | Velocidad de transferencia de datos
        Video para imlementacion de diferentes barras de descarga -> https://www.youtube.com/playlist?list=LL 
        '''
        bar=progressbar.ProgressBar(maxval=video_descarga.filesize,widgets=['\nDESCARGANDO...',video_descarga.default_filename," ",progressbar.Percentage(),' ',progressbar.Bar('#'),progressbar.FileTransferSpeed()])
        # Inicia la barra 
        bar.start()
        # Descarga el video
        video_descarga.download()
        # Termina la barra
        bar.finish()

        print('DESCARGA COMPLETA')
    except:  # Si falla la descarga del link printea lo siguiente
        print('Intenta escribir de nuevo')
    
import KOKAS as p__q
p__q.Kokas().H0()
