import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser
from functools import partial


class Main:

    def inicioSesion(self):
        self.gui_sesion = Toplevel(root)
        self.gui_sesion.title("Inicio sesion")
        self.gui_sesion.geometry("300x250")

        self.email = StringVar()
        self.password = StringVar()

        Label(self.gui_sesion, text="Ingresar datos: ").pack()

        Label(self.gui_sesion, text="Correo * ").pack()
        Entry(self.gui_sesion, textvariable=self.email).pack()

        Label(self.gui_sesion, text="Password * ").pack()
        Entry(self.gui_sesion, textvariable=self.password).pack()

        Label(self.gui_sesion, text="").pack()

        Button(self.gui_sesion, text="Iniciar sesión", width=10, height=1, command=self.iniciar_sesion).pack()

    def iniciar_sesion(self):
        #self.sesion1 = sesion_bdd.Session_bdd() #Crear archivo que inicie sesion en la bdd
        self.datos_sesion = (self.email.get(), self.password.get())
        self.verificador = self.sesion1.consulta(self.datos_sesion)

        if (self.verificador == None):
            mb.showinfo("Información", "Inicio incorrecto  ")

        else:
            self.email_sesion = self.verificador[0]
            self.password_sesion = self.verificador[1]
            mb.showinfo("Información", "Inicio correcto")
            #print("mail: " + self.email_sesion + " contra: " + self.password_sesion)
            self.email_usuario = self.verificador[0]
            self.password_usuario = self.verificador[1]

            self.button_productos.config(
                state="normal"
            )
            self.button_productos_favoritos.config(
                state="normal"
            )
            self.button_sesion.config(
                state="disabled"
            )
            self.button_productos_favoritos.config(
                state="normal"
            )
            self.gui_sesion.destroy()

    def registro(self):
        self.gui_registro = Toplevel(root)
        self.gui_registro.title("Registro")
        self.gui_registro.geometry("300x250")

        self.email = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        Label(self.gui_registro, text="Ingresar datos: ").pack()

        Label(self.gui_registro, text="Correo * ").pack()
        Entry(self.gui_registro, textvariable=self.email).pack()

        Label(self.gui_registro, text="Username * ").pack()
        Entry(self.gui_registro, textvariable=self.username).pack()

        Label(self.gui_registro, text="Password * ").pack()
        Entry(self.gui_registro, textvariable=self.password).pack()

        Label(self.gui_registro, text="").pack()

        Button(self.gui_registro, text="Registro", width=10, height=1, command=self.registrar_usuario).pack()

    def registrar_usuario(self):
        #self.registro1 = registro_bdd.Registro_bdd()
        self.tupla = (self.username.get(), self.email.get(), self.password.get())
        self.registro1.alta(self.tupla)
        mb.showinfo("Información", "Usuario registrado  ")
        self.email.set("")
        self.username.set("")
        self.password.set("")

    def new_window(self):

        w2 = Tk()
        matrix = [[0 for x in range(4)] for y in range(12)]
        rows = []
        cols = []

        l = Label(w2, text="Sueldo Imponible")
        l.grid(row=0, column=0)
        cols.append(l)

        l = Label(w2, text="Impuestos Retenidos")
        l.grid(row=0, column=1)
        cols.append(l)

        l = Label(w2, text="Honorarios Brutos")
        l.grid(row=0, column=2)
        cols.append(l)

        l = Label(w2, text="Impuestos Retenidos")
        l.grid(row=0, column=3)
        cols.append(l)

        lista_entries = []
        value = ''
        for i in range(12):
            for j in range(4):

                e = Entry(w2)
                e.grid(row=i+1, column=j, sticky=NSEW)

                cols.append(e.get())
                matrix[i][j] = e.get()
                lista_entries.append(e)

    #Función que agarre los datos (idea: crear lista que tenga las entries, luego usamos el get para obtener su valor)
        def calcular():
            for x in lista_entries:
                print(x.get())
        boton_calcular = Button(w2,command= calcular, text = 'Registrar datos').grid()

    def __init__(self):

        self.email_usuario = ""
        self.password_usuario = ""

        global root
        root = Tk()
        root.title("Tax Help")
        #root.iconbitmap('img/icon/ayaya-emote.ico')
        root.geometry("400x200")
        root.config(
            bg="#E0FFFF"
        )

        contenido = Frame(root, bg="#E0FFFF")
        contenido.pack()

        botones = Frame(root)
        botones.pack()

        boton_exit = Frame(root)
        boton_exit.pack(side=BOTTOM)

        label = Label(contenido, text="Bienvenido a Tax Help", borderwidth=2, relief="groove")
        label.pack()
        Label(contenido, text="", bg="#E0FFFF").pack()

        label.config(
            font=("Times New Roman", 24),
            pady=10,
            padx=10
        )

        self.button_sesion = Button(botones, text="Iniciar sesión", command=self.inicioSesion)
        self.button_sesion.pack(side=tk.LEFT)
        self.button_sesion.config(
            width=10
        )

        button_registro = Button(botones, text="Registrar", command=self.registro)
        button_registro.pack(side=tk.LEFT)
        button_registro.config(
            width=10
        )

        self.button_proyeccion = Button(botones,  text="Proyección", command=self.new_window)
        self.button_proyeccion.pack(side=tk.LEFT)
        self.button_proyeccion.config(
            width=10
        )


        button_quit = Button(boton_exit, text="Salir", command=root.quit)
        button_quit.pack()
        button_quit.config(
            width=10
        )

        root.mainloop()


aplicacion1 = Main()