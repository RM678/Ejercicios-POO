may=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

min=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num=['0','1','2','3','4','5','6','7','8','9']

listaA=[{'Cedula':'cedula', 'Nombre': 'nombre', 'Apellido':'apellido','Direccion':'direccion', 'Telefono':'telefono','TelefonoO':'telefonoO'},{'Cedula':'cedula', 'Nombre': 'nombre', 'Apellido':'apellido','Direccion':'direccion', '918r7':'t8ejrno','2838ud':'te9385'}]

def TomarDatosE(lista,may=may,min=min,num=num):
 #   print (lista)
    listaN=[]
    listaD={}
    datosE=''
    valueE=''
    
    pos=-1
    
    listaK=['','','','','','']
    listaV=['','','','','','']
         
    
    for datosD in lista:
        for datos in datosD:
      
            pos=pos+1
               
            value=datosD[datos]
 
            for letra in datos:
                       
        
                if (letra>='a' and letra<='z'):
                    datosE=datosE+Encrypt(letra,min)
                elif (letra>='A' and letra<='Z'):
                    datosE=datosE+Encrypt(letra,may)
                elif (letra>='0' and letra<='9'):
                    datosE=datosE+Encrypt(letra,num,n=4)
                if (letra not in may and letra not in min and letra not in num):
                    datosE=datosE+letra
        
            for letra in value:         
        
                if (letra>='a' and letra<='z'):
                    valueE=valueE+Encrypt(letra,min)  
                if (letra >='A' and letra<='Z'):
                    valueE=valueE+Encrypt(letra,may)    
                if (letra>='0' and letra<='9'):
                    valueE=valueE+Encrypt(letra,num,n=4)        
                if (letra not in may and letra not in min and letra not in num):
                    valueE=valueE+letra
                
            listaK[pos]=datosE
            listaV[pos]=valueE
            
            datosE=''
            valueE=''
                
            if (pos==5):
                
                valueE=''
                datosE=''
            
                listaA={listaK[0]:listaV[0], listaK[1]: listaV[1], listaK[2]:listaV[2],listaK[3]:listaV[3], listaK[4]:listaV[4],listaK[5]:listaV[5]}
                
                listaN.append(listaA)
                pos=-1
           
    return listaN
    
def Encrypt(dato,listaC,n=7):
    datoN=''
    Tl=len(listaC)
    Tc=0
    C=0
    
    for L in listaC:
        if (L==dato):
            Tc=Tl-n
            if (C<Tc):
                datoN=datoN+listaC[C+n]
                
            if (C>Tc):
                C=C-Tl
                datoN=datoN+listaC[C+n]            
                
            if (C==Tc):
                C=C-Tl
                datoN=datoN+listaC[C+n]
                
        C=C+1
    
    return datoN
    
#TomarDatos(D,may,min,num)


def TomarDatosD(lista,may=may,min=min,num=num):

    listaN=[]
    listaD={}
    datosE=''
    valueE=''
    
    pos=-1
   
    listaK=['','','','','','']
    listaV=['','','','','','']
    
    for datosD in lista:
        for datos in datosD:
      
            pos=pos+1
               
            value=datosD[datos]
 
            for letra in datos:
                       
        
                if (letra>='a' and letra<='z'):
                    datosE=datosE+Desencrypt(letra,min)
                elif (letra>='A' and letra<='Z'):
                    datosE=datosE+Desencrypt(letra,may)
                elif (letra>='0' and letra<='9'):
                    datosE=datosE+Desencrypt(letra,num,n=4)
                if (letra not in may and letra not in min and letra not in num):
                    datosE=datosE+letra
        
            for letra in value:         
        
                if (letra>='a' and letra<='z'):
                    valueE=valueE+Desencrypt(letra,min)  
                if (letra >='A' and letra<='Z'):
                    valueE=valueE+Desencrypt(letra,may)    
                if (letra>='0' and letra<='9'):
                    valueE=valueE+Desencrypt(letra,num,n=4)        
                if (letra not in may and letra not in min and letra not in num):
                    valueE=valueE+letra
           
            listaK[pos]=datosE
            listaV[pos]=valueE
            
            datosE=''
            valueE=''
                
            if (pos==5):
                
                valueE=''
                datosE=''
            
                listaA={listaK[0]:listaV[0], listaK[1]: listaV[1], listaK[2]:listaV[2],listaK[3]:listaV[3], listaK[4]:listaV[4],listaK[5]:listaV[5]}
                
                listaN.append(listaA)
                pos=-1
   
    return listaN
    
def Desencrypt(dato,listaC,n=7):
    datoN=''
    Tl=len(listaC)
    Tc=0
    C=0
    
    for L in listaC:
        if (L==dato):
            Tc=Tl-n
     #       print (C,' ',Tc,' ',L)
            if (C<Tc):
                datoN=datoN+listaC[C-n]
                
            if (C>Tc):
                C=C-Tl
                datoN=datoN+listaC[C-n]            
                
            if (C==Tc):
                C=C-Tl
                datoN=datoN+listaC[C-n]
                
        C=C+1
    
    return datoN

if __name__ == "__main__":
    
    estudiantesE=TomarDatosE(listaA)
    print (estudiantesE)
    estudiantesD=TomarDatosD(estudiantesE)
    print('')
    print (estudiantesD)