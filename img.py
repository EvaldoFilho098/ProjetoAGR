#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
#win = Tk()

#Set the geometry of tkinter frame
#win.geometry("100x100")

def resizing(img,x,y):
    resized_image= img.resize((x,y), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    return new_image

#Load an image in the script
img_add_o= (Image.open("Icons\\botao-adicionar.png"))
#Load an image in the script
img_edi_o= (Image.open("Icons\\editar.png"))
#Load an image in the script
img_rem_o= (Image.open("Icons\\lixeira-de-reciclagem.png"))
#Load an image in the script
img_sim_o= (Image.open("Icons\\confirmacao.png"))
#Load an image in the script
img_nao_o= (Image.open("Icons\\fechar.png"))
#Load an image in the script
img_sav_o= (Image.open("Icons\\salve-.png"))
#Load an image in the script
img_inf_o= (Image.open("Icons\\contato.png"))


#Resize the Image using resize method
#new_image = resizing(img)

#def my_command():
   #text.config(text= "You have clicked Me...")

#Let us create a label for button event
#img_label= Label(image=new_image)
#img_label.place(x=30, y=30)

#Let us create a dummy button and pass the image
#button= Button(win, image=new_image,borderwidth=0, text='Adicionar', compound=LEFT)
#button.pack(pady=30)

#win.mainloop()