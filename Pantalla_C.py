import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
import Funciones_C
import EncryptBD
import Funciones_C



class Principal_window:
    def __init__(self,ancho=450, alto=350, titulo_pantalla="Ventana principal", titulo='MENU', opciones=[]):
        # Crear la ventana principal.
        self.ventana_principal = tk.Tk()
        
        self.ventana_principal.title(titulo_pantalla)
        
        frame=Frame(self.ventana_principal)
        frame.pack()      
        frame.config(bg="dark blue") 
        Label(frame, text=titulo).place(relx=0.02, rely=0.02,relwidth=0.95, relheight=0.1)
        
        pos=0.14
        siguiente = 0.12
        for opcion in opciones:
    
            boton_abrir = ttk.Button(
                frame,
                **opcion
            )
            boton_abrir.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
            pos+=siguiente
        
        
        boton_abrir1 = ttk.Button(
            frame,
            text="Salir",
            command=self.ventana_principal.destroy
        )
        
        boton_abrir1.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
        self.ventana_principal.config(width=ancho, height=alto)
        frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.centrar(self.ventana_principal)
        self.ventana_principal.mainloop()
        
    
    def centrar(self,r):
        altura = r.winfo_reqheight()
        anchura = r.winfo_reqwidth()
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla = r.winfo_screenwidth()
        # print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
        x = (anchura_pantalla // 2) - (anchura//2)
        y = (altura_pantalla//2) - (altura//2)
        r.geometry(f"+{x}+{y}")
        
        
class Data_Windows:
    def __init__(self, ancho=430, alto=330, lista = [], data=[], Lista_C=[], color="deep sky blue", Accion=""):
        self.lista=lista
        self.ancho=ancho
        self.alto=alto
        self.color=color
        self.Lista_C=Lista_C
        data=Funciones_C.Procesos.LeerArchivo()
        data=EncryptBD.TomarDatosD(data)
        
        self.Datos=data
        
    
        if (Accion=="Formulario"):
            self.Formulario (Accion=Accion)

        elif (Accion=="Mostrar"):
            self.Mostrar (datos=self.Datos)
            
        elif (Accion=="Buscar"):
            self.Formulario (Accion=Accion)            
            
        elif (Accion=="Eliminar"):
            self.Formulario (Accion=Accion)         
        
        elif (Accion=="Modificar"):
            self.Formulario (Accion=Accion) 
            
    def Mostrar (self, datos = [], Mostrar_C=False ):
        print (datos)
        lista=self.lista
        
        if ( Mostrar_C==True):
            lista=self.Lista_C
            
        self.Ventana = tk.Toplevel()
        self.Ventana.title('Datos')
        self.Ventana.geometry('600x500')
        # self.Ventana['bg']='#fb0'
        campos = []
        for data in lista:
            campos.append(data['label'])
            
        tabla = ttk.Treeview(self.Ventana, columns=campos)
        tabla.column("#0",width=30)
        tabla.heading("#0", text="Item", anchor=CENTER)
        for data in campos:
            tabla.column(data,width=100, anchor=CENTER)
            tabla.heading(data, text=data, anchor=CENTER)
        
        for i, data in enumerate(datos):
            valor = []
            for val in campos:
            
                if (val in data.keys()):
                    valor.append(data[val])
                else:
                    valor.append('')
            tabla.insert("",END, text=str(i+1), values=valor)
        
        tabla.place(relx=0.02, rely=0.02,relwidth=0.96, relheight=0.7)
        boton_cerrar = ttk.Button(
            self.Ventana,
            text="Salir", 
            command=self.Ventana.destroy
        )
        boton_cerrar.place(relx=0.02, rely=0.75, relwidth=0.95, relheight=0.1)        
        
        
    
    def Formulario (self, Accion=""):
        lista= self.lista
        
        if (Accion=="Modificando"):
            lista=self.Lista_C              
        
        self.Ventana = tk.Toplevel()
        self.Ventana.title("Ingresar Datos")
        self.Ventana.config(width= self.ancho, height= self.alto)
        self.Ventana.config(bg=self.color)
        
        # Crear un botón dentro de la ventana secundaria
        # para cerrar la misma.
        
        if (Accion=="Formulario"):
            Botones=[{'text': 'Guardar', 'command':self.Guardar},
        ]
            
        elif (Accion=="Buscar"):
            Botones=[{'text': 'Verificar', 'command':self.Verificar},
]
            
        elif (Accion=="Eliminar"):
            Botones= [{'text': 'Eliminar', 'command':partial(self.Verificar,Eliminar=True)},
]
            
        elif (Accion=="Modificar"):
            Botones= [{'text': 'Modificar', 'command':partial(self.Verificar,Modificar=True)},
]        

        
        pos=0.02
        siguiente = 0.12
        for data in lista:
            Label(self.Ventana, text=data['label']).place(relx=0.02, rely=pos,relwidth=0.4, relheight=0.1)
            entry = Entry(self.Ventana)
            entry.place(relx=0.45, rely=pos,relwidth=0.52, relheight=0.1)
            data['input'] =entry 
            pos+=siguiente
        
        if (Accion=="Modificando"):
            
            Botones=[{'text': 'Modificar', 'command':partial (Funciones_C.Procesos.ModificarDatos, posicion=self.pos, Estudiantes=self.Datos_C, nuevo= lista) },
            ]              
        
        
        for boton in Botones:
            boton = ttk.Button(self.Ventana, **boton)
            boton.place(relx=0.02, rely=pos,relwidth=0.95, relheight=0.1)
            pos+=siguiente
        
        boton_cerrar = ttk.Button(
            self.Ventana,
            text="Salir", 
            command=self.Ventana.destroy
        )
        boton_cerrar.place(relx=0.02, rely=pos, relwidth=0.95, relheight=0.1)
        
        lista=self.lista
        Ingresar=self.Ventana
        

        self.Ventana.mainloop()
        #return (Ingresar, lista)
    
    
    
    def Verificar(self,Eliminar=False,Modificar=False):
        print ("Verificando")
        global CI,Estudiantes,DatosB,nuevo
        DatosB=[]
        DatosR=[]
        pos=-1
        data = {}
        
        Datos_C=Funciones_C.Procesos.LeerArchivo()
        Datos_C=EncryptBD.TomarDatosD(Datos_C)
        self.Datos_C=Datos_C
        
        print ("H")  
        
        
        for dato in self.lista:
            data[dato['label']] = dato['input'].get()
        
        print(data)
        
        CedulaB=data['Cedula']
        
        pos,DatosR= Funciones_C.Procesos.BuscarDatos(Estudiantes=Datos_C,CI=CedulaB)
        DatosB.append(DatosR)
        
        print(DatosB)
        
        print(pos)
        print (DatosB)
        self.pos=pos
        
        if (DatosB!=[[]] and Eliminar==False and Modificar==False):
            self.Mostrar(datos = DatosB, Mostrar_C=True)
            #ingresar.destroy()
          
        elif (DatosB!=[[]] and Eliminar==True):
       
            Text='Usuario Eliminado'
            #pantallas.Mensaje_en_pantalla(Text,DatosB,Estudiantes)
            #ingresar.destroy()
            
            
            nuevo=Funciones_C.Procesos.EliminarDatos(Datos_C,pos)
            nuevoG=EncryptBD.TomarDatosE(nuevo)
            Funciones_C.Procesos.GuardaArchivo(nuevoG)
            
            Eliminar=False
           
        elif (DatosB!=[[]] and Modificar==True):
            print ('Modificado')
            #ingresar.destroy()
            #ingresarM , DatosM = pantallas.Ingresar_Datos(ancho=630, alto=460,lista=formulario,color="orange")
            print ("En Mantenimiento")
            self.Formulario(Accion= "Modificando")
            print (DatosM)
        else:
            Text='Datos no encontrados'
            #pantallas.Mensaje_en_pantalla(Text)
            print (Text)
        #return DatosB   """     
    
    def Modificando():
        global ingresarM, DatosM,pos
            
        dataM={}
        for datoM in DatosM:
                dataM[datoM['label']] = datoM['input'].get()
        
        Mod=funciones.ModificarDatos(nuevo=dataM,posicion=pos, Estudiantes=Estudiantes)
            
        ModG=EncryptBD.TomarDatosE(Mod)
        funciones.GuardaArchivo(ModG)    
    
    
    def Guardar(self):
        
        print ("HHHHHHHHHH")
        print (self.lista)
        data = {}
        for dato in self.lista:
            data[dato['label']] = dato['input'].get()
        #----------------------------------------------    
        Estudiantes=Funciones_C.Procesos.LeerArchivo()
        Estudiantes=EncryptBD.TomarDatosD(Estudiantes)        
        #----------------------------------------------    
        for CIV in Estudiantes:
     
            if (CIV['Cedula']==data['Cedula']):
                #ingresar.destroy()
                Text='¡Usuario Existente!'
                #pantallas.Mensaje_en_pantalla(Text)
                return 0
        print (Estudiantes)
        Estudiantes.append(data)
        print ('Guardando')
        print (Estudiantes)
        EstudiantesG=EncryptBD.TomarDatosE(Estudiantes)
       # funciones.GuardaArchivo(EncryptBD.TomarDatosE(Estudiantes))
        Funciones_C.Procesos.GuardaArchivo(EstudiantesG)

    




def Funcion1():
    Ventana= Data_Windows(lista=formulario, Botones=botones, Accion="Formulario")
def Funcion2():
    Ventana= Data_Windows(lista=formulario, data=Datos, Accion="Mostrar")
def Funcion3():
    print('Funcion3....')   
        





if __name__ == "__main__":
    
    Datos=[{'Cedula':'1', 'Nombre': '2', 'Apellido':'3', 'Direccion':'4', 'Telefono':'5' }, {'Cedula':'12', 'Nombre': '23', 'Apellido':'34', 'Direccion':'45', 'Telefono':'56' }]
        
    formulario=[
            {'label':'Cedula'},
            {'label':'Nombre'},
            {'label':'Apellido'},
            {'label':'Direccion'},
            {'label':'Telefono'},
        
    ]   
    
    
    botones = [{'text': 'Boton 1', 'command':Funcion1},
                {'text': 'Boton 2', 'command':Funcion2},
                {'text': 'Boton 3', 'command':Funcion3}
        ]
    Pantalla= Principal_window(600, 600,'Prueba','Ejemplo 1',botones)




"""
Ventana= Data_Windows(lista=formulario)
Ventana.Formulario (Botones=botones)"""