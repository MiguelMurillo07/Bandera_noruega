from tkinter import *

principal = Tk()

principal.title("Bandera de Noruega")

principal.geometry("700x500")

principal.resizable(0,0)

principal.config(bg= "red")

#Frame entrada

frame_entrada = Frame(principal)
frame_entrada.config(bg= "red", width=100 , height=80)
frame_entrada.place(x=10 , y=10)

#Frame operaciones

frame_operaciones = Frame(principal)
frame_operaciones.config(bg= "white", width=680, height=100)
frame_operaciones.place(x=10, y=200)

frame_operaciones2 = Frame(principal)
frame_operaciones2.config(bg= "white", width=100, height=680)
frame_operaciones2.place(x=200 , y=10)

frame_operaciones3 = Frame(principal)
frame_operaciones3.config(bg= "blue", width=680, height=70)
frame_operaciones3.place(x=10, y=215)

frame_operaciones4 = Frame(principal)
frame_operaciones4.config(bg= "blue", width=70, height=680)
frame_operaciones4.place(x=215, y=10)


principal.mainloop()