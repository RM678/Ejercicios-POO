from os import system
import json
import os
import platform
sistema = platform.system()

sistemaop = os.name


class Procesos():
    def __init__(self):
        pass

    def BuscarDatos(Estudiantes,CI, mostrar=False):
    
        system("cls")
    
        pos=0
        posicion = -1
        print (CI)
        for data in Estudiantes:
            
            if (data['Cedula']==CI):
                
                posicion=pos
                break
            pos=pos + 1
        #return posicion
        if (data['Cedula']!=CI):
            data=[]
        return pos,data
    
    # Función utilizada para eliminar un registro por medio de la CI
    # Si CI es encontrada muestra los datos y pregunta si quiere eliminar el usuario
    def EliminarDatos(Estudiantes,posicion):
       
        if (posicion != -1):
        
            Estudiantes.pop(posicion)
       
        return Estudiantes
    
    # Busca el registro por medio de la CI, si es encontrado pregunta si desea modificarlo
    # Si selecciona modificar el Sistema le muestra el valor de cada campo, si escribimos un nuevo valor es agregado a dicho campo, 
    # de lo contrario si solo presionamos enter el campo mantiene su valor anterior
    def ModificarDatos(nuevo,posicion,Estudiantes):
        print('Modificar datos')
      
        if (posicion != -1):
         
                for campo in Estudiantes[posicion].keys():
                   
                    if (nuevo[campo]!=''):
                        Estudiantes[posicion][campo]=nuevo[campo]
        print (Estudiantes)                  
        return Estudiantes
    
    #Con esta función ordenamos el listado por cualquiera de los campos seleccionados por el usuario
    def OrdenarDatos (Estudiantes,r):
        
        system("cls")
        print('----------Ordenar Datos--------')
        cont = 0
        
        for campo in Estudiantes[0].keys():
            cont +=1
            print(campo,': ')
            
        if (r in Estudiantes[0].keys()):
            Estudiantes= sorted(Estudiantes, key=lambda estudiante : estudiante[r])
    
        return Estudiantes
    
    
    def GuardaArchivo(datos):
        with open('datos.json','w') as file:
            json.dump(datos, file, indent=4)    
    
    
    # Función que lee el archivo datos.json
    # Utilizamos try y except FileNotFoundError, para evitar que el programa inicie así exista o no datos.json
    def LeerArchivo():
        try:
            with open('datos.json','r') as file:
                data=json.load(file)
            return data
        except FileNotFoundError:
            print("El archivo datos.json no existe")
            return []