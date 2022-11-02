from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import youtube_dl
screen=Tk()
screen.geometry("900x600")
screen.title("Convertidor de archivos")
screen.resizable(0, 0)
#Variables-------------------------------
URL=StringVar()
#Funciones-------------------------------
def convertir():
    if URL.get()=="":
        next=messagebox.askretrycancel(message="¿Desea reiniciar?",title="URL no encontrado")
        if next==False:
            exit()
    else:
        info=youtube_dl.YoutubeDL().extract_info(url=URL.get(),download=False)
        filename = f"{info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([info['webpage_url']])
        print("Download complete.. {}".format(filename))
        messagebox.showinfo(message="Archivo descargado correctamente",title="Finalizado")
#Etiquetas-------------------------------
Label(screen,wraplength=800,text="Convertidor de Archivos",font=("Harlow Solid Italic",60)).pack(side="top")
Label(screen,text="URL:",font=("Bauhaus 93",30)).place(x=300,y=300)
#Entradas--------------------------------
Entry(screen,textvariable=URL,bd=2,width=30).place(x=390,y=318)
#Botones---------------------------------
Button(screen,text="Convertir",font=("Harlow Solid Italic",40),command=convertir,bg="gray",bd=0.5).pack(side="bottom",fill="x")
screen.mainloop()
