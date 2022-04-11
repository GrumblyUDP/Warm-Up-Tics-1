import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser
from functools import partial

import coneccion_bdd

class Main:

    def inicioSesion(self):
        self.gui_sesion = Toplevel(root)
        self.gui_sesion.title("Inicio sesion")
        self.gui_sesion.geometry("300x250")

        self.rut = StringVar()
        self.nombre = StringVar()

        Label(self.gui_sesion, text="Ingresar datos: ").pack()

        Label(self.gui_sesion, text="Rut").pack()
        Entry(self.gui_sesion, textvariable=self.rut).pack()

        Label(self.gui_sesion, text="nombre * ").pack()
        Entry(self.gui_sesion, textvariable=self.nombre).pack()

        Label(self.gui_sesion, text="").pack()

        Button(self.gui_sesion, text="Iniciar sesión", width=10, height=1, command=self.iniciar_sesion).pack()

    def iniciar_sesion(self):
        self.sesion1 = coneccion_bdd.main() #Crear archivo que inicie sesion en la bdd
        self.datos_sesion = (self.rut.get(), self.nombre.get())
        self.verificador = self.sesion1.consulta(self.datos_sesion)

        if (self.verificador == None):
            mb.showinfo("Información", "Inicio incorrecto  ")

        else:
            self.rut_sesion = self.verificador[0]
            self.nombre_sesion = self.verificador[1]
            mb.showinfo("Información", "Inicio correcto")
            #print("mail: " + self.rut_sesion + " contra: " + self.nombre_sesion)
            self.rut_usuario = self.verificador[0]
            self.nombre_usuario = self.verificador[1]

            self.button_proyeccion.config(
                state="normal"
            )
            self.gui_sesion.destroy()

    def registro(self):
        self.gui_registro = Toplevel(root)
        self.gui_registro.title("Registro")
        self.gui_registro.geometry("300x250")

        self.rut = StringVar()
        self.username = StringVar()

        Label(self.gui_registro, text="Ingresar datos: ").pack()

        Label(self.gui_registro, text="Rut * ").pack()
        Entry(self.gui_registro, textvariable=self.rut).pack()

        Label(self.gui_registro, text="Username * ").pack()
        Entry(self.gui_registro, textvariable=self.username).pack()

        Label(self.gui_registro, text="").pack()

        Button(self.gui_registro, text="Registro", width=10, height=1, command=self.registrar_usuario).pack()

    def registrar_usuario(self):
        self.registro1 = coneccion_bdd.main()
        self.tupla = ( self.rut.get(), self.username.get())
        self.registro1.alta(self.tupla)
        mb.showinfo("Información", "Usuario registrado  ")
        self.rut.set("")
        self.username.set("")

    def new_window(self):

        w2 = Tk()
        w2.title("Tax Help")
        matrix = [[0 for x in range(4)] for y in range(12)]
        rows = []
        cols = []

        l = Label(w2, text="Sueldo Imponible", font= 'Helvetica 12 bold')
        l.grid(row=0, column=0)
        cols.append(l)

        l = Label(w2, text="Impuestos Retenidos", font= 'Helvetica 12 bold')
        l.grid(row=0, column=1)
        cols.append(l)

        l = Label(w2, text="Honorarios Brutos", font= 'Helvetica 12 bold')
        l.grid(row=0, column=2)
        cols.append(l)

        l = Label(w2, text="Impuestos Retenidos", font= 'Helvetica 12 bold')
        l.grid(row=0, column=3)
        cols.append(l)

        lista_entries = []

        for i in range(12):
            for j in range(4):
                e = ttk.Entry(w2 ,font = ('courier', 15, 'bold'))
                e.grid(row=i+1, column=j, pady=2, padx =6 ,sticky=NSEW)
                cols.append(e.get())
                matrix[i][j] = e.get()


                lista_entries.append(e)


    #Función que agarre los datos (idea: crear lista que tenga las entries, luego usamos el get para obtener su valor)
        def calcular():



            self.calculo1 = coneccion_bdd.main()  # objeto que ingresa al archivo coneccion_bdd y va al metodo main
            self.datos_sesion = (self.rut.get(), self.nombre.get()) #obtiene datos usuario en caso se necesite para consultar

            #con el objeto calculo1 se pueden usar las funciones que consulten la bdd

            '''for x in lista_entries:
                print(x.get())'''

            #honorarios_brutos = ingreso_honorarios_brutos(self)
            #print("honorarios brutos: {honorarios_brutos}")

            decimal_honorario = obtencion_porcentaje_honorario(self)
            print(f"decimal_honorario: {float(decimal_honorario)}") #11,5


            honorario_bruto_anual = obtencion_honorario_bruto_anual(self)
            print(f"honorario_bruto_anual: {honorario_bruto_anual}")

            retenido_anual_estipulado = obtencion_retenido_anual_estipulado(self, honorario_bruto_anual, decimal_honorario)
            print(f" retenido anual estipulado: {retenido_anual_estipulado}")

            sueldo_anual = obtencion_sueldo_anual(self)
            print(f"sueldo_anual: {sueldo_anual}")

            gastos_presuntos = obtencion_gastos_presuntos(self,honorario_bruto_anual)
            print(f"gastos presuntos: {gastos_presuntos}")

            afecto_impuesto_global = obtencion_afecto_impuesto_global(self,honorario_bruto_anual,gastos_presuntos)
            print(f"Afecto impuesto global: {afecto_impuesto_global}")

            renta_imponible_anual = obtencion_renta_imponible_anual(self,sueldo_anual, afecto_impuesto_global)
            print(f"renta_imponible_anual: {renta_imponible_anual}")

            impuesto_total = obtencion_impuesto_total(self,renta_imponible_anual)
            print(f"impuesto_total: {impuesto_total}")

            impuesto_final = obtencion_impuesto_final(self, impuesto_total, retenido_anual_estipulado)
            print(f"impuesto final: {impuesto_final}")

            w3 = Tk()
            w3.title("Tax Help")
            w3['bg'] = '#6495ED'
            if impuesto_final >0:
                label =Label(w3 ,text= f"Impuesto a pagar: {impuesto_final}", font=("Helvetica", 40), bg="#6495ED").pack(padx=(30,30), pady=(160,160))
            if impuesto_final <0:
                label = Label(w3, text=f"Monto a devolver: {abs(impuesto_final)}", font=("Helvetica", 40),bg="#6495ED").pack(padx=(30,30), pady=(160,160))
            if impuesto_final ==0:
                label = Label(w3, text=f"No hay impuesto a pagar ni devolver", font=("Helvetica", 40),bg="#6495ED").pack(padx=(30,30), pady=(160,160))

        #funciones que los ayudaran a obtener los datos de cada columna y puedan usarlos

        def ingreso_honorarios_brutos(self): #copiar esta idea para las otras 2 columnas

            self.bdd = coneccion_bdd.main()
            self.rut_sesion = self.rut.get()

            contador =2
            suma =0
            honorarios_brutos_mensual = []
            honorarios_brutos_mensual.append(self.rut_sesion)
            for x in lista_entries:
                if(contador%4==0):
                    value = x.get().strip()
                    if value != "":
                        #suma = suma + int(value)
                        honorarios_brutos_mensual.append(int(value))
                contador = contador+1

            self.ingreso_honorarios_brutos = self.bdd.ingreso_honorarios_brutos(honorarios_brutos_mensual)

            return honorarios_brutos_mensual

        def obtencion_porcentaje_honorario(self): #obtiene el 11,5
            self.bdd = coneccion_bdd.main()
            self.obtencion_porcentaje_honorario = self.bdd.obtencion_porcentaje_honorario()

            return self.obtencion_porcentaje_honorario

        def obtencion_honorario_bruto_anual(self):
            contador = 2
            suma = 0
            honorarios_brutos_mensual = []

            for x in lista_entries:
                if (contador % 4 == 0):
                    value = x.get().strip()
                    if value != "":
                        if(value.isnumeric()):
                            if(int(value) >=0):
                                suma = suma + int(value)
                contador = contador + 1
            return suma

        def obtencion_retenido_anual_estipulado(self, honorario_bruto_anual,decimal_honorario ):
            retenido_anual_estipulado = honorario_bruto_anual * (decimal_honorario/100)
            return retenido_anual_estipulado

        def obtencion_sueldo_anual(self):
            contador = 0
            suma = 0
            for x in lista_entries:
                if (contador % 4 == 0):
                    value = x.get().strip()
                    if value != "":
                        if (value.isnumeric()):
                            if (int(value) >= 0):
                                suma = suma + int(value)
                contador = contador + 1
            return suma

        def obtencion_gastos_presuntos(self, honorario_bruto_anual):

            self.bdd = coneccion_bdd.main()
            self.obtencion_limite_presuncion = self.bdd.obtencion_limite_presuncion()

            self.obtencion_porcentaje_honorario

            gastos_presuntos = honorario_bruto_anual * 0.3

            if(gastos_presuntos > self.obtencion_limite_presuncion):
                gastos_presuntos = self.obtencion_limite_presuncion

            return gastos_presuntos

        def obtencion_afecto_impuesto_global(self,honorario_bruto_anual,gastos_presuntos):
            afecto_impuesto_global = honorario_bruto_anual - gastos_presuntos

            return afecto_impuesto_global

        def obtencion_renta_imponible_anual(self,sueldo_anual, afecto_impuesto_global):

            renta_imponible_anual = sueldo_anual + afecto_impuesto_global

            return renta_imponible_anual

        def obtencion_impuesto_total(self,renta_imponible_anual):

            #obtener factor y cant a rebajar de la bdd:
            self.bdd = coneccion_bdd.main()
            self.obtencion_datos = self.bdd.obtencion_datos_factor(renta_imponible_anual)

            factor = self.obtencion_datos[0]
            cant_rebajar = self.obtencion_datos[1]
            print(f"factor: {factor}")
            print(f"cant_rebajar: {cant_rebajar}")
            impuesto_total = (float(renta_imponible_anual)*float(factor)) - float(cant_rebajar)
            return impuesto_total

        def obtencion_impuesto_final(self, impuesto_total,retenido_anual_estipulado):
            impuesto_final = float(impuesto_total) - float(retenido_anual_estipulado)
            return impuesto_final

        #Boton que deberia mostrar si debe o no impuestos

        boton_calcular = Button(w2,command= calcular, text = 'Registrar datos',relief="ridge", bg="#FAFAD2", borderwidth=4, width=20,pady=10, font=("Helvetica", 15)).grid(column=1)


    def __init__(self):

        self.rut_usuario = ""
        self.nombre_usuario = ""

        global root
        root = Tk()
        root.title("Tax Help")
        #root.iconbitmap('img/icon/ayaya-emote.ico')
        root.geometry("580x290")
        root.config(
            bg="#778899"
        )

        contenido = Frame(root, bg="#778899")
        contenido.pack()

        botones = Frame(root)
        botones.pack()

        boton_exit = Frame(root)
        boton_exit.pack(side=BOTTOM)
        label = Label(contenido, height=1, bg="#778899").pack()
        label = Label(contenido, text="Bienvenido a Tax Help", borderwidth=0,highlightthickness=2, highlightbackground="#D2691E", relief="solid")
        label.pack()
        Label(contenido, text="", bg="#778899").pack()

        label.config(
            font=("Times New Roman", 33),
            pady=15,
            padx=20,
            bg="#FFFFE0"
        )
        #boton_calcular = Button(w2, command=calcular, text='Registrar datos', relief="ridge", bg="#FAFAD2",
         #                       borderwidth=4, width=20, pady=10, font=("Helvetica", 15)).grid(column=1)

        self.button_sesion = Button(botones, text="Iniciar sesión",  bg="#F8F8FF", padx=20, pady=7, font=("italic", 15),command=self.inicioSesion)
        self.button_sesion.pack(side=tk.LEFT)
        self.button_sesion.config(
            width=10
        )

        button_registro = Button(botones, text="Registrar", bg="#F8F8FF", padx=20, pady=7, font=("italic", 15),command=self.registro)
        button_registro.pack(side=tk.LEFT)
        button_registro.config(
            width=10
        )

        self.button_proyeccion = Button(botones, state="disabled", padx=20, pady=7, font=("italic", 15), bg="#ADD8E6" ,text="Proyección", command=self.new_window)
        self.button_proyeccion.pack(side=tk.LEFT)
        self.button_proyeccion.config(
            width=10
        )

        button_quit = Button(boton_exit, text="Salir", bg="#F8F8FF", padx=13, pady=3, font=("italic", 15), command=root.quit)
        button_quit.pack()
        button_quit.config(
            width=10
        )

        root.mainloop()


aplicacion1 = Main()