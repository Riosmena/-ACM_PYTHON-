print('''
Gaddiel Lara Roldán
''')

'''
Este programa sirve para generar referencias en formato APA
El código principal abre un archivo en modo w+ que se usará para escribir las referencias en líneas, también contine 2 listas que se usan en varias funciones y ejecuta la primera función.
En la primera función (paso1()) pide el tipo de referencia que se va a hacer y da varias opciones como libro o página web, para esto, usa la función menú. Ejecuta alguna de las funciones ref1() a ref10() dependiendo del número que ingrese el ususario. Si se ingresa 0 se cierra el programa y el archivo, y lee las referencias si fueron generadas.
Las funciones ref1() a ref10() ejecutan las siguientes funciones dependiendo de los datos que requiera ese tipo de referencia, cada función regresa un string que se guarda en una variable. Estos se concatenan para hacer la referencia completa y escribirla en el archivo.
Las funciones desde la función apellido() hasta la función f_hoy() sirven para ser ejecutadas en varias de las funciones de ref1() a ref10(), ya que la mayoría regresa datos que se usan en diferentes tipos de referencias. Regresan una parte de la referencia completa. Piden al usuario datos numéricos y strings y le dan el formato requerido.

'''

#ELEMENTO NUEVO (Importa la fecha en la que se ejecuta el programa, la cual se usa en unas referencias)
from datetime import date
def apellido():
    ap=str(input('Ingresa primer apellido del autor'))
    while len(ap)<1:
        print('Ingresa al menos un caracter')
        ap=str(input('Ingresa primer apellido del autor'))
    ap=ap.capitalize()+', '
    return ap
def iniciales():
    i=str(input('Ingresa la inicial de cada nombre del autor en el orden correcto'))
    while len(i)<1:
        print('Ingresa al menos un caracter')
        i=str(input('Ingresa la inicial de cada nombre del autor en el orden correcto'))
    i=i.upper()
    i_texto=''
    for x in range(len(i)):
        if x<(len(i)-1):
            i_texto=i_texto+i[x]+'. '
        elif x==(len(i)-1):
            i_texto=i_texto+i[x]
    return i_texto
def menu_autor(tipo):
    if tipo==0:
        print('Selecciona una opción de autor\n0. Sin autor\n1. Autor(es)\n2. Organización')
    elif tipo==1:
        print('Selecciona una opción de autor\n0. Autor(es) con nombre real\n1. Organización o autor sin nombre real')
def f_autores():
    menu_autor(0)
    opcion=int(input())
    while opcion!=0 and opcion!=1 and opcion!=2:
        print('Ingresa una opción válida')
        menu_autor(0)
        opcion=int(input())
    if opcion==0:
        autores_texto=0
    if opcion==1:
        n=int(input('Ingresa el número de autores\n'))
        while n<1:
            print('Ingresa número válido')
            n=int(input('Ingresa el número de autores\n'))
        autores_texto=''
        autores=[]
        for x in range(n):
            ap=apellido()
            i=iniciales()
            autor=ap+i
            autores.append(autor)
        autores=sorted(autores)
        autores[-1]=autores[-1]+'. '
        if n>1:
            autores[-2]=autores[-2]+'. & '
            if n>2:
                for y in range(3,n+1):
                    autores[-y]=autores[-y]+'; '
        for z in range(n):
            autores_texto=autores_texto+autores[z]
    elif opcion==2:
        autores_texto=str(input('Ingresa nombre de la organización'))
        while len(autores_texto)<1:
            print('Ingresa al menos un caracter')
            autores_texto=str(input('Ingresa nombre de la organización'))
        autores_texto=autores_texto+'. '
    return autores_texto
def f_autores_red():
    menu_autor(1)
    opcion=int(input())
    while opcion!=0 and opcion!=1:
        print('Ingresa una opción válida')
        menu_autor(1)
        opcion=int(input())
    if opcion==0:
        n=int(input('Ingresa el número de autores\n'))
        while n<1:
            print('Ingresa número válido')
            n=int(input('Ingresa el número de autores\n'))
        autores_texto=''
        autores=[]
        for x in range(n):
            ap=apellido()
            i=iniciales()
            autor=ap+i
            autores.append(autor)
        autores=sorted(autores)
        autores[-1]=autores[-1]+'. '
        if n>1:
            autores[-2]=autores[-2]+'. & '
            if n>2:
                for y in range(3,n+1):
                    autores[-y]=autores[-y]+'; '
        for z in range(n):
            autores_texto=autores_texto+autores[z]
    elif opcion==1:
        autores_texto=str(input('Ingresa el nombre'))
        while len(autores_texto)<1:
            print('Ingresa al menos un caracter')
            autores_texto=str(input('Ingresa el nombre'))
        autores_texto=autores_texto+'. '
    return autores_texto
def ano():    
    opcion=int(input('Selecciona una opción\n0. Sin fecha\n1. Ingresar año\n'))
    while opcion!=0 and opcion!=1:
        print('Ingresa una opción válida')        
        opcion=int(input('Selecciona una opción\n0. Sin fecha\n1. Ingresar año\n'))
    if opcion==0:
        a=str('(s.f.). ')
    elif opcion==1:        
        an=int(input('Ingresa el año'))
        while an<0:
            print('Ingresa año válido')
            an=int(input('Ingresa el año'))
        a='('+str(an)+'). '
    return a
def fecha():
    opcion=int(input('Selecciona una opción\n0. Sin fecha\n1. Ingresar fecha\n'))
    while opcion!=0 and opcion!=1:
        print('Ingresa una opción válida')        
        opcion=int(input('Selecciona una opción\n0. Sin fecha\n1. Ingresar fecha\n'))
    if opcion==0:
        f=str('(s.f.). ')
    elif opcion==1:
        di=int(input('Ingresa el número de día 1-31'))
        while di<1 or di>31:
            print('Ingresa un día válido')
            di=int(input('Ingresa el número de día 1-31'))
        me=int(input('Ingresa el número de mes 1-12'))
        while me<1 or me>12:
            print('Ingresa un mes válido')
            me=int(input('Ingresa el número de mes 1-12'))
        m=M[me-1]
        an=int(input('Ingresa el año'))
        while an<0:
            print('Ingresa año válido')
            an=int(input('Ingresa el año'))
        f='('+str(di)+' de '+m+' de '+str(an)+'). '
    return f
def titulo():
    ti=str(input('Ingresa el título'))
    while len(ti)<1:
        print('Ingresa al menos un caracter')
        ti=str(input('Ingresa el título'))
    ti=ti.capitalize()+'. '
    return ti
def editorial():
    ed=str(input('Ingresa la editorial'))
    while len(ed)<1:
        print('Ingresa al menos un caracter')
        ed=str(input('Ingresa la editorial'))
    ed=ed.capitalize()+'. '
    return ed
def titulo_revista():
    ti=str(input('Ingresa el título'))
    while len(ti)<1:
        print('Ingresa al menos un caracter')
        ti=str(input('Ingresa el título'))
    ti=ti.capitalize()+', '
    return ti
def periodico():
    pe=str(input('Ingresa el periódico'))
    while len(pe)<1:
        print('Ingresa al menos un caracter')
        pe=str(input('Ingresa el periódico'))
    pe=pe.capitalize()+'. '
    return pe
def articulo():
    ar=str(input('Ingresa el artículo'))
    while len(ar)<1:
        print('Ingresa al menos un caracter')
        ar=str(input('Ingresa el artículo'))
    ar=ar.capitalize()+'. '
    return ar
def volumen():
    vol=str(input('Ingresa el volumen\tENTER. Sin volumen'))
    return vol
def numrevista():
    n=int(input('Ingresa el número de la revista'))
    if n<1:
        print('Ingresa número válido')
        n=int(input('Ingresa el número de la revista'))
    nr='('+str(n)+'), '
    return nr
def num_i_f():
    n0=int(input('Ingresa el número de la primera página del artículo'))
    while n0<1:
        print('Ingresa número válido')
        n0=int(input('Ingresa el número de la primera página del artículo'))
    n1=int(input('Ingresa el número de la última página del artículo'))
    while n1<n0:
        print('Ingresa número válido')
        n1=int(input('Ingresa el número de la última página del artículo'))
    if n1==n0:
        nif=str(n0)+'.'
    else:
        nif=str(n0)+'-'+str(n1)+'.'
    return nif
def nombre_pagina():
    np=str(input('Ingresa el nombre de la página'))
    while len(np)<1:
        print('Ingresa al menos un caracter')
        np=str(input('Ingresa el nombre de la página'))
    np=np+'. '
    return np
def url():
    u=str(input('Pega la url'))
    while len(u)<1:
        print('Ingresa al menos un caracter')
        u=str(input('Ingresa la url'))
    return u
def usuario_yt():
    us=str(input('Ingresa el nombre de usuario'))
    while len(us)<1:
        print('Ingresa al menos un caracter')
        us=str(input('Ingresa el nombre de usuario'))
    us='['+us+'] '
    return us
def video():
    v=str(input('Ingresa el título del video'))
    while len(v)<1:
        print('Ingresa al menos un caracter')
        v=str(input('Ingresa el título del video'))
    v=v+' [Video]. Youtube. '
    return v
def contenido():
    cont=str(input('Pega el texto de la publicación\tENTER. Sin texto'))    
    palabras=[]
    palabra=''
    if len(cont>0):
        cont=cont+' '
        for x in cont:
            palabra=palabra+x
            if x==' ':
                palabras.append(palabra)
                palabra=''
        y=0
        cont=''
        while y<len(palabras) and y<20:
            cont=cont+palabras[y]
            y=y+1
    cont=cont+'[Descripción audiovisual]. '
    return cont
def usuario_red():
    us=str(input('Ingresa el nombre de usuario'))
    while len(us)<1:
        print('Ingresa al menos un caracter')
        us=str(input('Ingresa el nombre de usuario'))
    us='[@'+us+'] '
    return us
def f_hoy():
    hoy=date.today()
    dd=hoy.strftime('%d')
    nm=hoy.strftime('%m')
    aa=hoy.strftime('%Y')    
    x=int(nm)-1
    hoy_texto=dd+' de '+M[x]+' de '+aa
    return hoy_texto
def ref1():
    print('Referencia:',L1[1])
    a=f_autores()
    b=ano()
    c=titulo()
    d=editorial()
    if a!=0:
        ref='\n'+a+b+c+d
    elif a==0:
        ref='\n'+c+b+d
    file.writelines(ref)
def ref2():
    print('Referencia:',L1[2])
    a=f_autores()
    b=ano()
    c=articulo()
    d=titulo_revista()
    e=volumen()
    f=numrevista()
    g=num_i_f()
    if a!=0:
        ref='\n'+a+b+c+d+e+f+g
    elif a==0:
        ref='\n'+c+b+d+e+f+g
    file.writelines(ref)
def ref3():
    print('Referencia:',L1[3])
    a=f_autores()
    b=fecha()
    c=articulo()
    d=periodico()
    if a!=0:
        ref='\n'+a+b+c+d
    elif a==0:
        ref='\n'+c+b+d
    file.writelines(ref)
def ref4():
    print('Referencia:',L1[4])
    a=f_autores()
    b=fecha()
    c=titulo()
    d=nombre_pagina()
    e=url()
    if a!=0:
        ref='\n'+a+b+c+d+e
    elif a==0:
        ref='\n'+c+b+d+e
    file.writelines(ref)
def ref5():
    print('Referencia:',L1[5])
    a=f_autores()
    b=ano()
    c=titulo()
    if a!=0:
        ref='\n'+a+b+c
    elif a==0:
        ref='\n'+c+b
    file.writelines(ref)
def ref6():
    print('Referencia:',L1[6])
    a=f_autores_red()
    b=usuario_yt()
    c=fecha()
    d=video()
    e=url()
    ref='\n'+a+b+c+d+e
    file.writelines(ref)
def ref7():
    print('Referencia:',L1[7])
    a=f_autores_red()
    b=usuario_red()
    c=fecha()
    d=contenido()
    e=url()
    ref='\n'+a+b+c+d+'Twitter. '+e
    file.writelines(ref)
def ref8():
    print('Referencia:',L1[8])
    a=f_autores_red()
    b=usuario_red()
    c=fecha()
    d=contenido()
    e=url()
    ref='\n'+a+b+c+d+'Facebook. '+e
    file.writelines(ref)
def ref9():
    print('Referencia:',L1[9])
    a=f_autores_red()
    b=usuario_red()
    c=fecha()
    d=contenido()
    e=url()
    ref='\n'+a+b+c+d+'Instagram. '+e
    file.writelines(ref)
def ref10():
    print('Referencia:',L1[10])
    a=titulo()
    b=fecha()
    c=f_hoy()
    d=url()
    if b!='(s.f.). ':
        ref='\n'+a+b+'En Wikipedia. '+d
    elif b=='(s.f.). ':
        ref='\n'+a+b+'En Wikipedia. Recuperado el '+c+' de '+d
    file.writelines(ref)
def menu():
    print('Selecciona tipo de referencia\n1.',L1[1],'\n2.',L1[2],'\n3.',L1[3],'\n4.',L1[4],'\n5.',L1[5],'\n6.',L1[6],'\n7.',L1[7],'\n8.',L1[8],'\n9.',L1[9],'\n10.',L1[10],'\n\n0.',L1[0])

def paso1():
    continuar=True
    while continuar:
        menu()
        opcion_r=int(input())
        if opcion_r not in range(len(L1)):
            print('Ingresa opción válida')
        elif opcion_r==1:
            ref1()
        elif opcion_r==2:
            ref2()
        elif opcion_r==3:
            ref3()
        elif opcion_r==4:
            ref4()
        elif opcion_r==5:
            ref5()
        elif opcion_r==6:
            ref6()
        elif opcion_r==7:
            ref7()
        elif opcion_r==8:
            ref8()
        elif opcion_r==9:
            ref9()
        elif opcion_r==10:
            ref10()
        elif opcion_r==0:
            continuar=False
            file.seek(0)
            referencias=file.read()
            file.close()
            print('Lista de referencias:'+referencias)       
file=open('archivo.txt','w+')
L1=['Salir y mostrar referencias','Libro','Revista','Periódico','Página Web','Diccionario','Youtube','Twitter','Facebook','Instagram','Wikipedia']
M=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
paso1()
