import Janela
from tkinter import Tk, StringVar, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X
from tkinter import messagebox
from tkinter import ttk
from var import *
import img

#def Inserir(Janela, Banco):
#    pass

#FUNÇÕES



def Mensagem_Aviso(txt):
    ''' Aviso para caso falte alguma informação válida'''
    messagebox.showerror(title="Impossível Cadastrar Atendimento", message= txt)

def Infos_Agrs(nome,posto, municipio, uf, tel, email, par, termo, status, parceira, obs, treinamento, data ):
    
    
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

    x_info = 10
    y_info = 27
    y_inicio = 50

    frame_Nome = Label(Janela.info_AGR_Sel_Frame, text= nome,bg=cor_escura, fg = cor_contraste, font= fonte_Destaques)
    frame_Nome.place(x=x_info,y=0)

    frame_Status = Label(Janela.info_AGR_Sel_Frame, text='Situação: ' + status ,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Status.place(x=x_info,y=y_inicio )
    frame_status_img = Label(Janela.info_AGR_Sel_Frame,image=img_status,bg=cor_escura)
    frame_status_img.place(x=90 + len(status)*9 ,y=y_inicio + 5) 

    frame_Posto = Label(Janela.info_AGR_Sel_Frame, text='Posto:  ',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Posto.place(x=x_info,y=y_inicio + y_info)

    frame_Municipio = Label(Janela.info_AGR_Sel_Frame, text='Local:  '+ municipio + ' - ' + uf,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Municipio.place(x=x_info,y=y_inicio + y_info*2)

    frame_Email = Label(Janela.info_AGR_Sel_Frame, text='E-Mail:  ' + email,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Email.place(x=x_info,y=y_inicio + y_info*3)

    frame_Tel = Label(Janela.info_AGR_Sel_Frame, text='Telefone:  ' + tel,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Tel.place(x=x_info,y=y_inicio + y_info*4)

    frame_Parceiro = Label(Janela.info_AGR_Sel_Frame, text='Parceria:  ' + parceira,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Parceiro.place(x=x_info,y=y_inicio + y_info*5)

    frame_data = Label(Janela.info_AGR_Sel_Frame, text='Data de Inicio:  ' + data,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_data.place(x=x_info,y=y_inicio + y_info*6)

    frame_Par = Label(Janela.info_AGR_Sel_Frame, text='Parametrização ',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Par.place(x=x_info,y=y_inicio + y_info*7)
    frame_Par_img = Label(Janela.info_AGR_Sel_Frame,image=img_par,bg=cor_escura)
    frame_Par_img.place(x=140,y=y_inicio + y_info*7 + 5)

    frame_Treino = Label(Janela.info_AGR_Sel_Frame, text='Treinamento ',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Treino.place(x=x_info,y=y_inicio + y_info*8)
    frame_Treino_img = Label(Janela.info_AGR_Sel_Frame,image=img_treino,bg=cor_escura)
    frame_Treino_img.place(x=117,y=y_inicio + y_info*8 + 5)

    frame_Termo = Label(Janela.info_AGR_Sel_Frame, text='Termo ',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    frame_Termo.place(x=x_info,y=y_inicio + y_info*9)
    frame_Termo_img = Label(Janela.info_AGR_Sel_Frame,image=img_termo,bg=cor_escura)
    frame_Termo_img.place(x=65,y=y_inicio + y_info*9 + 5)


    #if obs != '' :
    #    frame_Obs = Label(Janela.info_AGR_Sel_Frame, text='Observacoes: ' + obs,bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
    #    frame_Obs.place(x=10,y=235)
