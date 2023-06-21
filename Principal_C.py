import Pantalla_C
import Funciones_C
import EncryptBD
from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial



def Verificar(Eliminar=False,Modificar=False):
    global CI,Estudiantes,DatosB,nuevo
    DatosB=[]
    DatosR=[]
    pos=-1
    data = {}
    
    print ("H")
    print (CI)    
    
    for dato in CI:
        data[dato['label']] = dato['input'].get()
    
    print(data)
    CedulaB=data['Cedula']
    
    pos,DatosR= funciones.BuscarDatos(Estudiantes=Estudiantes,CI=CedulaB)
    DatosB.append(DatosR)
    
    print(DatosB)
    
    print(pos)
    
    if (DatosB!=[[]] and Eliminar==False and Modificar==False):
        pantallas.Mostrar_Datos(lista=formulario, datos = DatosB)
        ingresar.destroy()
        
    elif (DatosB!=[[]] and Eliminar==True):
   
        Text='Usuario Eliminado'
        pantallas.Mensaje_en_pantalla(Text,DatosB,Estudiantes)
        ingresar.destroy()
        
        
        nuevo=funciones.EliminarDatos(Estudiantes,pos)
        print(nuevo)
        funciones.GuardaArchivo(nuevo)
        
        Eliminar=False
        
    elif (DatosB!=[[]] and Modificar==True):
        print ('Modificado')
        ingresar.destroy()
        ingresarM , DatosM = pantallas.Ingresar_Datos(ancho=630, alto=460,lista=formulario,color="orange")   
        print (DatosM)
    else:
        Text='Datos no encontrados'
        pantallas.Mensaje_en_pantalla(Text)
    return DatosB




Estudiantes=Funciones_C.Procesos.LeerArchivo()
print (Estudiantes)
Estudiantes=EncryptBD.TomarDatosD(Estudiantes)
print(Estudiantes)
#nuevo=[]
ingresar=None
DatosB=[]
pos=0





"""

boton= [{'text': 'Aceptar', 'command':partial(funciones.ModificarDatos,posicion=pos,Estudiantes=Estudiantes)},
]

BotonO= [{'text': 'Modificar', 'command':partial(Almacenar_orden)},
]

"""

Formulario=[
        {'label':'Cedula'},
        {'label':'Nombre'},
        {'label':'Apellido'},
        {'label':'Direccion'},
        {'label':'Telefono'},
        {'label':'Telefono otro'},
    
    ]

    



def Datos():
    global ingresar, nuevo
    
    ingresar , nuevo = Pantalla_C.Data_Windows(lista=Formulario, Accion="Formulario")



def Mostrar():
    Pantalla_C.Data_Windows(lista=Formulario, Accion="Mostrar")

def Buscar():
    global CI,DatosB,ingresar
    ingresar , CI = Pantalla_C.Data_Windows(lista=[{'label':'Cedula'}], Lista_C=Formulario , Accion="Buscar",color="purple") 
    #ingresar , CI = pantallas.Ingresar_Datos(ancho=630, alto=460,lista=[{'label':'Cedula'}], botones=BotonV,color="purple")    

def EliminarD():
    global CI,DatosB,ingresar
    ingresar , CI = Pantalla_C.Data_Windows(lista=[{'label':'Cedula'}], Accion="Eliminar",color="dark red")
    #ingresar , CI = pantallas.Ingresar_Datos(ancho=630, alto=460,lista=[{'label':'Cedula'}], botones=BotonE,color="dark red")

def ModificarD():
    global CI,DatosB,ingresar
    ingresar , CI = Pantalla_C.Data_Windows(lista=[{'label':'Cedula'}],Lista_C=Formulario, Accion="Modificar",color="orange")
    #ingresar , CI = pantallas.Ingresar_Datos(ancho=630, alto=460,lista=[{'label':'Cedula'}], botones=BotonM,color="orange")

def Ordenar():
    global ingresar,O
    print ('En mantenimiento')
    #ingresar, O= pantallas.Ingresar_Datos(ancho=630, alto=460,lista=[{'label':'Criterio de orden'}],botones=BotonO)
    
        




opciones=[
        {'text':'Ingresar datos', 'command':Datos},#partial(pantallas.Ingresar_Datos, lista=formulario, botones=botones)},
        {'text':'Mostrar datos', 'command':Mostrar},
        {'text':'Buscar datos', 'command':Buscar},
        {'text':'Eliminar datos', 'command':EliminarD},
        {'text':'Modificar datos', 'command':ModificarD},
        {'text':'Ordenar datos', 'command':Ordenar},
]
    
    
    

    
#Pantalla=Pantalla_C.Principal_window(opciones=opciones)






if __name__ == "__main__":
    pass
    #Patalla = Pantalla(opciones=opciones)
    Pantalla=Pantalla_C.Principal_window(opciones=opciones)