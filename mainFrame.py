import serial, threading, time
import tkinter as tk
import os

numb=45
numb1 = 49

class MainFrame(tk.Frame):
    def __init__(self,master=None, timeout = 0.1):
        super().__init__(master,width=1920,height=1080)
        self.numerGlobal = 1
        self.numerR = 0
        self.my_label = tk.Label(master=self, text="esto", bg="white")
        self.place(x=10, y= 10)
        self.master.protocol('WM_DELETE_WINDOW',self.askQuit)
        self.hilo1 = threading.Thread(target=self.getSensorValues,daemon=True)
        self.pack()
        self.arduino = serial.Serial("COM4",9600,timeout=0.1)
        self.img=tk.PhotoImage(file=f"{self.numerGlobal}.png")
        self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
        self.value_dis = tk.StringVar(value=0.0)
        self.value_tac = tk.StringVar(value=0.0)
        self.normal_txt = tk.Label(self, text="distancia")
        self.dato2=tk.Label(self,width=6,textvariable=self.value_dis).place(x=130,y=20)
        self.isRun=True
        self.hilo1.start()


    def cerrar(self):
        self.arduino.close()


    def askQuit(self):
        self.isRun=False
        self.arduino.write('dis:0'.encode('ascii'))
        time.sleep(1.1)
        self.arduino.close()
        self.hilo1.join(0.1)
        self.master.quit()
        self.master.destroy()
        print("*** finalizando...")


    def getSensorValues(self):
        while self.isRun:
            cad =self.arduino.readline().decode('ascii').strip()
            try:
                if cad:         
                    pos=cad.index(":")
                    label=cad[:pos]
                    value=float(cad[pos+1:])
                    if label == 'dis':
                        self.value_dis.set(value)                        
                        if float(self.value_dis.get())<=46:
                            if(float(self.value_tac.get())==0):
                                if(self.numerGlobal<2):
                                    if self.numerR == numb1:
                                        self.numerR = 0
                                    if self.numerR < 10:
                                        self.img=tk.PhotoImage(file= f"R_000{self.numerR}.png")
                                        self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                    if self.numerR >= 10:
                                        self.img=tk.PhotoImage(file= f"R_00{self.numerR}.png")
                                        self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                    print(self.numerR)
                                    self.numerR+=1
                        if float(self.value_dis.get()) > 46:
                            if(float(self.value_tac.get())==0):
                                if(self.numerGlobal<2):
                                    if self.numerR > 0:
                                        if self.numerR == numb1:
                                            self.numerR = 48
                                        if self.numerR < 10:
                                            self.img=tk.PhotoImage(file= f"R_000{self.numerR}.png")
                                            self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                        if self.numerR >= 10:
                                            self.img=tk.PhotoImage(file= f"R_00{self.numerR}.png")
                                            self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                        print(self.numerR)
                                        self.numerR-=1
                       #if float(self.value_dis.get()) > 46:
                            #self.config(bg='blue')
                        #if float(self.value_dis.get()) <= 46:
                            #self.config(bg='yellow')
                            #if float(self.value_tac.get())==1:
                               #self.config(bg='red')
                    if label == 'tac':
                        self.value_tac.set(value)
                        if float(self.value_dis.get())<=46:
                            if(float(self.value_tac.get())==1):
                                if(self.numerGlobal<numb+1):
                                    if(self.numerGlobal==0):
                                        self.numerGlobal=1
                                    self.img=tk.PhotoImage(file= f"{self.numerGlobal}.png")
                                    self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                    self.numerGlobal+=1
                        if(float(self.value_tac.get())==0):
                            if(self.numerGlobal>0):
                                if(self.numerGlobal==numb+1):
                                    self.numerGlobal=numb-1
                                self.img=tk.PhotoImage(file= f"{self.numerGlobal}.png")
                                self.fondo=tk.Label(self, image=self.img).place(x=0,y=0)
                                self.numerGlobal-=1

                        
            except ValueError:
                print(f'Este es el error: ${ValueError}')
            
    def create_widgets(self):
        tk.Label(self,text="distancia").place(x=30,y=20)
        self.dato2=tk.Label(self,width=6,textvariable=self.value_dis).place(x=130,y=20)
        tk.Label(self,text="Toque").place(x=30,y=50)
        self.dato2=tk.Label(self,width=6,textvariable=self.value_tac).place(x=130,y=50)

    