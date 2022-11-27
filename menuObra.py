import threading as hilo
import serial
import tkinter as tk
#creacion de arduino
ard = serial.Serial("COM4",9600)
#variables de dartos
dato1,dato2=0.0,0.0
valor, valor2, = [],[]
#ventana o pantalla
ventana= tk.Tk()
ventana.title("CAJA NEGRA")
#reprducion
while True:
    if(ard.inWaiting()>0):
        datos=ard.readline().decode('ascii')
        #print(datos)
        if(datos.split(sep='$')[0]!='0'):
            dato1=float(datos.split(sep='$')[0])
            valor.append(dato1)
        dato2=float(datos.split(sep='$')[1])
        valor2.append(dato1)
        print(dato1,'$',dato2,'\n')
