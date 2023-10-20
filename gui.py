from tkinter import *
 
window = Tk() 
window.geometry("500x500")
window.title("Första GUI")

icon = PhotoImage(file='SSK.png')
window.iconphoto(True,icon)
window.config(background="darkblue")

window.mainloop() #Själva fönstret

