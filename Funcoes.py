import Janela
from tkinter import Tk, StringVar, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X
from tkinter import messagebox
from tkinter import ttk
from var import *
import img


#FUNÇÕES

def Mensagem_Aviso(txt):
    ''' Aviso para caso falte alguma informação válida'''
    messagebox.showerror(title="Impossível Cadastrar Atendimento", message= txt)

def Infos_Agrs(nome,cpf,posto, municipio, uf, tel, email, par, termo, status, parceira, treinamento, data ):
    

    if par.upper() == "SIM":
        img_par = Janela.img_sim_men
    else:
        img_par = Janela.img_nao_men

    if termo.upper() == "SIM":
        img_termo = Janela.img_sim_men
    else:
        img_termo = Janela.img_nao_men  

    if status.upper() == "ATIVO":
        img_status = Janela.img_sim_men
    else:
        img_status = Janela.img_nao_men  
    
    if treinamento.upper() == "SIM":
        img_treino = Janela.img_sim_men
    else:
        img_treino = Janela.img_nao_men 

    nome = nome.split(' ')
    if len(nome) > 1:
        nome = nome[0] + ' ' + nome[-1]
    Janela.frame_Nome.configure(text=nome)
    cpf = "CPF: " + cpf
    Janela.frame_cpf.configure(text=cpf)
    status = "Status: " + status
    Janela.frame_Status.configure(text= status)
    try:
        Janela.frame_status_img.configure(image=img_status)
    except:
        Janela.frame_status_img = Label(Janela.info_AGR_Sel_Frame,image=img_status,bg=cor_escura)

    Janela.frame_status_img.place(x=130 ,y=y_inicio + 5)

    Janela.frame_Posto.configure(text= "Posto: " + posto)

    Janela.frame_Municipio.configure(text="Cidade: "+ municipio + " - " + uf)

    Janela.frame_Email.configure(text="E-mail: " + email)

    Janela.frame_Tel.configure(text="Telefone: " + tel)

    Janela.frame_Parceiro.configure(text="Parceira: "+ parceira)

    Janela.frame_data.configure(text="Data de Inicio: " + data)

    par = "Parametrização: " + par 
    Janela.frame_Par.configure(text=par)
    try:
        Janela.frame_Par_img.configure(image=img_par)
    except:
        Janela.frame_Par_img = Label(Janela.info_AGR_Sel_Frame,image=img_par,bg=cor_escura)
        
    Janela.frame_Par_img.place(x=185,y=y_inicio + y_info*7 + 5)
    
    treinamento = "Treinamento: " + treinamento 
    Janela.frame_Treino.configure(text=treinamento)
    try:
        Janela.frame_Treino_img.configure(image=img_treino)
    except:
        Janela.frame_Treino_img = Label(Janela.info_AGR_Sel_Frame,image=img_treino,bg=cor_escura)
    Janela.frame_Treino_img.place(x=160,y=y_inicio + y_info*8 + 5)

    termo = "Termo: " + termo 
    Janela.frame_Termo.configure(text=termo)
    try:
        Janela.frame_Termo_img.configure(image=img_termo)
    except:
        Janela.frame_Termo_img = Label(Janela.info_AGR_Sel_Frame,image=img_termo,bg=cor_escura)

    Janela.frame_Termo_img.place(x=120,y=y_inicio + y_info*9 + 5)


