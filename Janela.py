from tkinter import LabelFrame, Tk, StringVar,IntVar,DISABLED, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X,N,E,S,W
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import FALSE
from typing import Sized
import img
from var import *
from PIL import Image,ImageTk
#import 
import ToolTip as TP
from Classes import AutocompleteCombobox
import Banco
#from Cadastro import Cadastrar

#Criar Janela


class Janela:
    def __init__(self,toplevel):
        #CONFIGURACOES ----
        #Titulo
        toplevel.title(titulos)
        #Tamanho da toplevelela
        toplevel.geometry(str(largura)+"x"+str(altura))
        #Cor de Fundo
        toplevel.configure(background = cor_meta)
        #Nao redimensionar
        toplevel.resizable(width = False, height = False)
        #Transparencia
        toplevel.attributes("-alpha",0.95)
        #Icone
        toplevel.iconbitmap(default="Icons/icon.ico")
        #Logo
        self.logo = PhotoImage(file="icons/logo_.png")

        #TITULO
        self.TopFrame = Frame(toplevel, width = largura, height = 100, bg = cor, relief = "raise" )
        self.TopFrame.pack(side=TOP)

        #Logo da Meta e Titulo do programa
        self.logo_meta = Label(self.TopFrame, image=self.logo,bg=cor)
        self.logo_meta.place(x=10,y=5)
        self.meta = Label(self.TopFrame,text = "Controle de AGR's",font=fonte_Titulos, fg= cor_contraste, bg=cor)
        self.meta.place(x=340,y=25)

        #AMBIENTE DE INFORMACOES 1
        self.infosFrame = Frame(toplevel, width = 960, height = 450, bg=cor,relief="raise")
        self.infosFrame.place(x = 30,y=125)

        #Data 
        self.date = Label(self.TopFrame,text=data,fg=cor_contraste,bg=cor,font=fonte_Mediana)
        self.date.place(x=865,y=35)

        #Quantidade de AGRs
        self.n_Agrs = Label(self.infosFrame, text="AGR's Cadastrados", fg = cor_contraste, bg=cor, font=fonte_Textos)
        self.n_Agrs.place(x=575,y=5)
        self.frame_aux = Frame(self.infosFrame, width = 170, height = 50, bg = cor_escura, relief="raise")
        self.frame_aux.place(x=570, y=30)
        self.qtd = Label(self.frame_aux,text=qtd_agr, bg = cor_escura, fg="red", font=fonte_Destaques)
        self.qtd.place(relx=0.5, rely=0.5,anchor=CENTER)

        #Quantidade de Agrs Ativos
        self.n_Ativos = Label(self.infosFrame, text="AGR's Ativos", fg = cor_contraste, bg=cor, font=fonte_Textos)
        self.n_Ativos.place(x=800,y=5)
        self.frame_auxAtv = Frame(self.infosFrame, width = 170, height = 50, bg = cor_escura, relief="raise")
        self.frame_auxAtv.place(x=770, y=30)
        self.qtd_Atv = Label(self.frame_auxAtv,text=qtd_ativos, bg = cor_escura , fg="red", font=fonte_Destaques)
        self.qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)

        #, width = 525, height = 325, bg=cor_meta,relief="raise"
        #AMBIENTE DE EXIBICAO DE AGRS
        self.AGRs_Frame = LabelFrame(toplevel,width = 525, height = 325)
        self.AGRs_Frame.place(x = 50,y=230)
        #self.AGRs_Frame.pack(padx=325,pady=130)

        ####################################################
        self.dadosCols = ("ID","NOME","CPF","POSTO","CIDADE","UF",
                    "PARCEIRA","TELEFONE","EMAIL","STATUS")
        self.listagem = ttk.Treeview(self.AGRs_Frame,columns = self.dadosCols,show='headings', height = 100, selectmode='browse')

        #print(self.dadosCols)
        self.listagem.bind('<Double-1>',self.Mostrar)
        #self.listagem.bind('<Button-1>',Mostrar)

        minw = 100
        #1
        self.listagem.column("ID", width = 30,minwidth=30)
        self.listagem.heading("ID",text="ID")
        #2
        self.listagem.column("NOME", width = 30,minwidth=minw)
        self.listagem.heading("NOME",text="NOME")
        #3
        self.listagem.column("CPF", width = 50,minwidth=minw)
        self.listagem.heading("CPF",text="CPF")
        #4
        self.listagem.column("POSTO", width = 50,minwidth=minw)
        self.listagem.heading("POSTO",text="POSTO")
        #5
        self.listagem.column("CIDADE", width = 50,minwidth=minw)
        self.listagem.heading("CIDADE",text="CIDADE")
        #6
        self.listagem.column("UF", width = 30,minwidth=30)
        self.listagem.heading("UF",text="UF")
        #7
        self.listagem.column("STATUS", width = 30,minwidth=50)
        self.listagem.heading("STATUS",text="STATUS")
        #8
        self.listagem.column("PARCEIRA", width = 30,minwidth=minw)
        self.listagem.heading("PARCEIRA",text="PARCEIRA")
        #9
        #self.listagem.column("DATA INICIO", width = 50,minwidth=70)
        #self.listagem.heading("DATA INICIO",text="DATA INICIO")
        #10
        #self.listagem.column("PARAMETRIZACAO", width = 30,minwidth=50)
        #self.listagem.heading("PARAMETRIZACAO",text="PARAMETRIZACAO")
        #11
        #self.listagem.column("TREINAMENTO", width = 30,minwidth=60)
        #self.listagem.heading("TREINAMENTO",text="TREINAMENTO")
        #12
        #self.listagem.column("TERMO", width = 30,minwidth=50)
        #self.listagem.heading("TERMO",text="TERMO")
        #13
        self.listagem.column("TELEFONE", width = 50,minwidth=minw)
        self.listagem.heading("TELEFONE",text="TELEFONE")
        #14
        self.listagem.column("EMAIL", width = 50,minwidth=minw)
        self.listagem.heading("EMAIL",text="EMAIL")

        self.listagem.place(x = 0, y = 0, width = 525, height = 305)

        #BARRAS DE ROLAGEM DA VISUALIZACAO
        self.ysb = ttk.Scrollbar(self.AGRs_Frame, orient=VERTICAL,command=self.listagem.yview)
        self.ysb.place(x=506,y=0,height=305)

        self.xsb = ttk.Scrollbar(self.AGRs_Frame, orient=HORIZONTAL,command=self.listagem.xview)
        self.xsb.place(x = 2, y = 305, width=510)

        self.listagem.configure(yscroll = self.ysb.set)
        self.listagem.configure(xscroll = self.xsb.set)

        # TEXTOS DOS CABEÇALHO
        for c in self.dadosCols:
            self.listagem.heading(c, text=c.title())

        # INSRINDO OS ITENS
        for item in Banco.Select_Columns(colunas_select):
            try:
                stts = Banco.Select_Where('STATUS','ID',item[0],'SITUACOES')
                item = list(item)
                item.append(stts[0][0])
            except:
                pass
            item = tuple(item)
            self.listagem.insert('', 'end', values=item)

        #AMBIENTE DE INFORMACOES DO AGR SELECIONADO
        self.info_AGR_Sel_Frame = Frame(toplevel, width = 370, height = 325, bg=cor_escura,relief="raise")
        self.info_AGR_Sel_Frame.place(x = 600,y=230)

        rsz_x = 25
        rsz_y = 25
        w_button = 30
        h_button = 30
        y_buttons = 35

        self.img_add= img.resizing(img.img_add_o,rsz_x,rsz_y) #icone de adicionar
        self.img_edi= img.resizing(img.img_edi_o,rsz_x,rsz_y) #icone de editar
        self.img_rem= img.resizing(img.img_rem_o,rsz_x,rsz_y) #icone de remover
        self.img_sim= img.resizing(img.img_sim_o,rsz_x,rsz_y) #icone de confirmacao
        self.img_nao= img.resizing(img.img_nao_o,rsz_x,rsz_y) #icone de negacao
        self.img_sim_men= img.resizing(img.img_sim_o,15,15) #icone de confirmacao
        self.img_nao_men= img.resizing(img.img_nao_o,15,15) #icone de negacao
        self.img_sav= img.resizing(img.img_sav_o,rsz_x,rsz_y) #icone de save
        self.img_inf= img.resizing(img.img_inf_o,rsz_x,rsz_y) #icone de informacoes

        #Botao de Adicionar AGRq
        self.cadastroButton = Button(self.infosFrame,image= self.img_add, bg=cor, fg=cor_contraste, width = w_button, height= h_button,command = self.Cadastrar)
        self.cadastroButton.place(x = 20 , y = y_buttons)
        TP.CreateToolTip(self.cadastroButton, text = 'Cadastrar')

        self.edicaoButton = Button(self.infosFrame,image= self.img_edi, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
        self.edicaoButton.place(x = 70 , y = y_buttons)
        TP.CreateToolTip(self.edicaoButton, text = 'Editar')

        self.remocaoButton = Button(self.infosFrame,image= self.img_rem, bg=cor, fg=cor_contraste, width = w_button, height= h_button, command=self.Excluir)
        self.remocaoButton.place(x = 120 , y = y_buttons)
        TP.CreateToolTip(self.remocaoButton, text = 'Remover')

        self.confirmacaoButton = Button(self.infosFrame,image= self.img_sim, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
        self.confirmacaoButton.place(x = 270 , y = y_buttons)
        TP.CreateToolTip(self.confirmacaoButton, text = 'Mostrar AGRs Ativos')

        self.negacaoButton = Button(self.infosFrame,image= self.img_nao, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
        self.negacaoButton.place(x = 320 , y = y_buttons)
        TP.CreateToolTip(self.negacaoButton, text = 'Mostrar AGRs Inativos')

        self.informacaoButton = Button(self.infosFrame,image= self.img_inf, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
        self.informacaoButton.place(x = 370 , y = y_buttons)
        TP.CreateToolTip(self.informacaoButton, text = 'Mostrar Todos Os AGRs')

        self.saveButton = Button(self.infosFrame,image= self.img_sav, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
        self.saveButton.place(x = 510 , y = y_buttons)
        TP.CreateToolTip(self.saveButton, text = 'Salvar')

        self.frame_Nome = Label(self.info_AGR_Sel_Frame, text= '',bg=cor_escura, fg = cor_contraste, font= fonte_Destaques)
        self.frame_Nome.place(x=x_info,y=0)

        self.frame_cpf = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_cpf.place(x=x_info,y=y_inicio + y_info)

        self.frame_Status = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_Status.place(x=x_info,y=y_inicio)
        self.frame_status_img = Label(self.info_AGR_Sel_Frame,image=None,bg=cor_escura)
        self.frame_status_img.place(x=130 ,y=y_inicio + 5) 

        self.frame_Posto = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_Posto.place(x=x_info,y=y_inicio + y_info*2)

        self.frame_Municipio = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_Municipio.place(x=x_info,y=y_inicio + y_info*3)

        #self.frame_Email = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        #self.frame_Email.place(x=x_info,y=y_inicio + y_info*3)

        self.frame_Tel = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_Tel.place(x=x_info,y=y_inicio + y_info*4)

        self.frame_Parceiro = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        self.frame_Parceiro.place(x=x_info,y=y_inicio + y_info*5)

        #self.frame_data = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        #self.frame_data.place(x=x_info,y=y_inicio + y_info*6)

        #self.frame_Par = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        #self.frame_Par.place(x=x_info,y=y_inicio + y_info*7)
        #self.frame_Par_img = Label(self.info_AGR_Sel_Frame,image=None,bg=cor_escura)
        #self.frame_Par_img.place(x=50,y=y_inicio + y_info*7 + 5)

        #self.frame_Treino = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        #self.frame_Treino.place(x=x_info,y=y_inicio + y_info*8)
        #self.frame_Treino_img = Label(self.info_AGR_Sel_Frame,image=None,bg=cor_escura)
        #self.frame_Treino_img.place(x=50,y=y_inicio + y_info*8 + 5)

        #self.frame_Termo = Label(self.info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
        #self.frame_Termo.place(x=x_info,y=y_inicio + y_info*9)
        #self.frame_Termo_img = Label(self.info_AGR_Sel_Frame,image=None,bg=cor_escura)
        #self.frame_Termo_img.place(x=50,y=y_inicio + y_info*9 + 5)

        #Botao de Editar AGR
        #self.EdicaoButton = Button(self.infosFrame, text = "Editar AGR", bg=cor, fg=cor_contraste, width = 15)
        #self.EdicaoButton.place(x = 170, y = 55)

    def Mostrar(self,event):
        
        #global self.listagem
        #, lista_atendimentos,lista_certificados,lista_locais,lista_solicitantes
        #Pega o item selecionado
        """
        "ID","NOME","CPF","POSTO","CIDADE","UF","STATUS","PARCEIRA",
            "DATA INICIO", "PARAMETRIZACAO", "TREINAMENTO","TERMO",
            "TELEFONE","EMAIL" """

        nodeId_1 = self.listagem.focus()
        
        #Pega as informacoes do item
        id_ = self.listagem.item(nodeId_1)['values'][0]
        nome_ = self.listagem.item(nodeId_1)['values'][1]
        cpf_ = self.listagem.item(nodeId_1)['values'][2]
        posto_ = self.listagem.item(nodeId_1)['values'][3]
        municipio_ = self.listagem.item(nodeId_1)['values'][4]
        uf_ = self.listagem.item(nodeId_1)['values'][5]
        
        parceira_ = self.listagem.item(nodeId_1)['values'][6]
        #data_ = self.listagem.item(nodeId_1)['values'][8]
        #par_ = self.listagem.item(nodeId_1)['values'][9]
        #trein_ = self.listagem.item(nodeId_1)['values'][10]
        #termo_ = self.listagem.item(nodeId_1)['values'][11]
        telefone_ = self.listagem.item(nodeId_1)['values'][7]
        email_ = self.listagem.item(nodeId_1)['values'][8]
        status_ = self.listagem.item(nodeId_1)['values'][9]

        self.Infos_Agrs(nome_,cpf_,posto_, municipio_, uf_, telefone_, email_,status_, parceira_)
        
    def Excluir(self):

        x = messagebox.showwarning(message="Tem Certeza Que Deseja Excluir o AGR Selecionado?")
        if x == 'ok':
        
            #global self.listagem 

            nodeId_1 = self.listagem.focus()
                
            #Pega as informacoes do item
            id_ = self.listagem.item(nodeId_1)['values'][0]

            Banco.Deletar(id_)

            #ALTERA A QUANTIDADE DE ATENDIMENTOS
            qtd_agr = Banco.Contagem()
            qtd_ativos = len(Banco.Select_Where("STATUS","Ativo"))

            self.qtd['text'] = str(qtd_agr)
            self.qtd_Atv['text'] = str(qtd_ativos)

            self.qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
            self.qtd.place(relx=0.5, rely=0.5,anchor=CENTER)

            self.listagem.delete(nodeId_1)
            self.listagem.place(x = 0, y = 0, width = 525, height = 305)

            self.frame_Nome.configure(text='')
            self.frame_Nome.place(x=x_info,y=0)

            self.frame_cpf.configure(text='')
            self.frame_cpf.place(x=x_info + 190,y=y_inicio )

            self.frame_Status.configure(text='')
            self.frame_Status.place(x=x_info,y=y_inicio )
            self.frame_status_img.destroy() 

            self.frame_Posto.configure(text='')
            self.frame_Posto.place(x=x_info,y=y_inicio + y_info)

            self.frame_Municipio.configure(text='')
            self.frame_Municipio.place(x=x_info,y=y_inicio + y_info*2)

            #self.frame_Email.configure(text='')
            #self.frame_Email.place(x=x_info,y=y_inicio + y_info*3)

            self.frame_Tel.configure(text='')
            self.frame_Tel.place(x=x_info,y=y_inicio + y_info*4)

            self.frame_Parceiro.configure(text='')
            self.frame_Parceiro.place(x=x_info,y=y_inicio + y_info*5)

            #self.frame_data.configure(text='')
            #self.frame_data.place(x=x_info,y=y_inicio + y_info*6)

            #self.frame_Par.configure(text='')
            #self.frame_Par.place(x=x_info,y=y_inicio + y_info*7)
            #self.frame_Par_img.destroy()

            #self.frame_Treino.configure(text='')
            #self.frame_Treino.place(x=x_info,y=y_inicio + y_info*8)
            #self.frame_Treino_img.destroy()

            #self.frame_Termo.configure(text='')
            #self.frame_Termo.place(x=x_info,y=y_inicio + y_info*9)
            #self.frame_Termo_img.destroy()

            messagebox.showinfo(title="Sucesso!", message="Cadastro Removido com Sucesso!")
        else:
            pass

    def Alterar(self):
        #Criar Janela
        #global self.listagem 

        nodeId_1 = self.listagem.focus()
        id_ = self.listagem.item(nodeId_1)['values'][0]
        nome_ = self.listagem.item(nodeId_1)['values'][1]
        cpf_ = self.listagem.item(nodeId_1)['values'][2]
        posto_ = self.listagem.item(nodeId_1)['values'][3]
        municipio_ = self.listagem.item(nodeId_1)['values'][4]
        uf_ = self.listagem.item(nodeId_1)['values'][5]
        status_ = self.listagem.item(nodeId_1)['values'][6]
        parceira_ = self.listagem.item(nodeId_1)['values'][7]
        #data_ = self.listagem.item(nodeId_1)['values'][8]
        #par_ = self.listagem.item(nodeId_1)['values'][9]
        #trein_ = self.listagem.item(nodeId_1)['values'][10]
        #termo_ = self.listagem.item(nodeId_1)['values'][11]
        telefone_ = self.listagem.item(nodeId_1)['values'][12]
        email_ = self.listagem.item(nodeId_1)['values'][13]

        """ 
        "ID","NOME","CPF","POSTO","MUNICIPIO","UF","STATUS",
        "PARCEIRA","DATA", "PARAMET", "TREINAMENTO","TERMO",
        "TELEFONE","EMAIL" 
        """

        Banco.Alterar("NOME","",id_)
        Banco.Alterar("CPF","",id_)
        Banco.Alterar("POSTO","",id_)
        Banco.Alterar("MUNICIPIO","",id_)
        Banco.Alterar("UF","",id_)
        #Banco.Alterar("STATUS","",id_)
        Banco.Alterar("PARCEIRA","",id_)
        #Banco.Alterar("DATA","",id_)
        #Banco.Alterar("PARAMET","",id_)
        #Banco.Alterar("TREINAMENTO","",id_)
        #Banco.Alterar("TERMO","",id_)

        #self.cidadeEntry.current(0)
    
    def Infos_Agrs(self,nome,cpf,posto, municipio, uf, tel, email, status, parceira, ):
    
        '''
        if par.upper() == "SIM":
            img_par = self.img_sim_men
        else:
            img_par = self.img_nao_men

        if termo.upper() == "SIM":
            img_termo = self.img_sim_men
        else:
            img_termo = self.img_nao_men  
        '''

        if status.upper() == "ATIVO":
            self.img_status = self.img_sim_men
        else:
            self.img_status = self.img_nao_men  
        
        '''
        if treinamento.upper() == "SIM":
            img_treino = self.img_sim_men
        else:
            img_treino = self.img_nao_men 
        '''

        nome = nome.split(' ')
        if len(nome) > 1:
            nome = nome[0] + ' ' + nome[-1]
        self.frame_Nome.configure(text=nome)
        cpf = "CPF: " + cpf
        self.frame_cpf.configure(text=cpf)
        status = "Status: " + status
        self.frame_Status.configure(text= status)
        try:
            self.frame_status_img.configure(image=self.img_status)
        except:
            self.frame_status_img = Label(self.info_AGR_Sel_Frame,image=self.img_status,bg=cor_escura)

        if ": INATIVO" in status: 
            self.frame_status_img.place(x=145 ,y=y_inicio + 5)
        elif ": ATIVO" in status:
            self.frame_status_img.place(x=130 ,y=y_inicio + 5)

        self.frame_Posto.configure(text= "Posto: " + posto)

        self.frame_Municipio.configure(text="Cidade: "+ municipio + " - " + uf)

        #self.frame_Email.configure(text="E-mail: " + email)

        self.frame_Tel.configure(text="Telefone: " + tel)

        self.frame_Parceiro.configure(text="Parceira: "+ parceira)

        #self.frame_data.configure(text="Data de Inicio: " + data)

        '''
        par = "Parametrização: " + par 
        self.frame_Par.configure(text=par)
        try:
            self.frame_Par_img.configure(image=img_par)
        except:
            self.frame_Par_img = Label(self.info_AGR_Sel_Frame,image=img_par,bg=cor_escura)
            
        self.frame_Par_img.place(x=185,y=y_inicio + y_info*7 + 5)
        
        treinamento = "Treinamento: " + treinamento 
        self.frame_Treino.configure(text=treinamento)
        try:
            self.frame_Treino_img.configure(image=img_treino)
        except:
            self.frame_Treino_img = Label(self.info_AGR_Sel_Frame,image=img_treino,bg=cor_escura)
        self.frame_Treino_img.place(x=160,y=y_inicio + y_info*8 + 5)

        termo = "Termo: " + termo 
        self.frame_Termo.configure(text=termo)
        try:
            self.frame_Termo_img.configure(image=img_termo)
        except:
            self.frame_Termo_img = Label(self.info_AGR_Sel_Frame,image=img_termo,bg=cor_escura)

        self.frame_Termo_img.place(x=120,y=y_inicio + y_info*9 + 5)
        '''
    def format_cpf(self,event = None):
        
            text = self.cpfEntry.get().replace(".", "").replace("-", "")[:11]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue
                if index in [2, 5]: new_text += text[index] + "."
                elif index == 8: new_text += text[index] + "-"
                else: new_text += text[index]

            self.cpfEntry.delete(0, "end")
            self.cpfEntry.insert(0, new_text)

    def format_tel(self,event = None):
        
            text = self.telEntry.get().replace("(", "").replace(")","").replace("-", "")[:11]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue

                if index == 0: new_text += "(" + text[index] 
                elif index == 1: new_text += text[index] + ")"
                elif index == 6: new_text += text[index] + "-"
                else: new_text += text[index]

            self.telEntry.delete(0, "end")
            self.telEntry.insert(0, new_text)
    
    def format_data(self,event = None):
        
            text = self.dataEntry.get().replace("/", "")[:8]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue

                if index == 1: new_text +=  text[index] + "/" 
                elif index == 3: new_text += text[index] + "/"
                else: new_text += text[index]

            self.dataEntry.delete(0, "end")
            self.dataEntry.insert(0, new_text)

    def Cadastrar__(self):
        #Criar Janela
        self.jan = Tk()

        #CONFIGURACOES ----
        #Titulo
        self.jan.title("CADASTRO")
        #Tamanho da Janela
        self.jan.geometry(str(400)+"x"+str(650))
        #Cor de Fundo
        self.jan.configure(background = cor)
        #Nao redimensionar
        self.jan.resizable(width = False, height = False)
        #Transparencia
        self.jan.attributes("-alpha",0.99)

        x_entry = 95
        y_inicio = 30
        y_cad = 55
        width_entry = 28
        width_entry_p = 39
        y_cad2 = 50
        x_check = 10
        x_label_check = 40

        ############################################################################

        #AMBIENTE DE DADOS
        self.cadastroFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.cadastroFrame.place(x = 20,y=50)
        self.cadastroLabel = Label(self.jan,text = "DADOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.cadastroLabel.place(x = 20, y = 15)

        #NOME
        self.nomeLabel = Label(self.cadastroFrame,text = "Nome: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.nomeLabel.place(x = 10,y = y_inicio)
        self.nomeEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.nomeEntry.place(x = x_entry, y = y_inicio)

        #CPF
        

        self.cpfLabel = Label(self.cadastroFrame,text = "CPF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.cpfLabel.place(x = 10,y = y_inicio + y_cad )
        self.cpfEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.cpfEntry.bind("<KeyRelease>", self.format_cpf)
        self.cpfEntry.place(x = x_entry, y = y_inicio + y_cad)

        #POSTO
        self.postoLabel = Label(self.cadastroFrame,text = "Posto: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.postoLabel.place(x = 10,y = y_inicio + y_cad*2 )
        self.postoEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor,height=15)
        self.postoEntry.set_completion_list(lista_posto)
        self.postoEntry.place(x = x_entry, y = y_inicio + y_cad * 2)

        #CIDADE
        self.cidadeLabel = Label(self.cadastroFrame,text = "Cidade: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.cidadeLabel.place(x = 10,y = y_inicio + y_cad*3 )
        #lista_cidade = ["Ponta Pora","Campo Grande","Dourados"]
        self.cidadeEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor,height=15)
        self.cidadeEntry.set_completion_list(lista_cidade)
        self.cidadeEntry.place(x = x_entry, y = y_inicio + y_cad*3 + 2 )

        #UF
        self.ufLabel = Label(self.cadastroFrame,text = "UF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.ufLabel.place(x = 10,y = y_inicio + y_cad*4 )
        self.lista_uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
        self.ufEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor)
        self.ufEntry.set_completion_list(self.lista_uf)
        self.ufEntry.place(x = x_entry, y = y_inicio + y_cad*4 + 2)

        #E-mail
        self.emailLabel = Label(self.cadastroFrame,text = "E-mail: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.emailLabel.place(x = 10,y = y_inicio + y_cad*5 )
        self.emailEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.emailEntry.place(x = x_entry, y = y_inicio + y_cad*5)

        #Telefone
        
        self.telLabel = Label(self.cadastroFrame,text = "Telefone: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.telLabel.place(x = 10,y = y_inicio + y_cad*6 )
        self.telEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.telEntry.bind("<KeyRelease>", self.format_tel)
        self.telEntry.place(x = x_entry, y = y_inicio + y_cad*6)

        #Parceira
        self.parcLabel = Label(self.cadastroFrame,text = "Parceira: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.parcLabel.place(x = 10,y = y_inicio + y_cad*7 )
        self.lista_parc = ["Soluti","Meta","Soluti/Meta"]
        self.parcEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p)
        self.parcEntry.set_completion_list(self.lista_parc)
        self.parcEntry.place(x = x_entry, y = y_inicio + y_cad*7 + 2)

        '''
        #Termo
        self.TermoLabel = Label(self.cadastroFrame,text = "Termo ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TermoLabel.place(x= 10,y = y_inicio + y_cad*8 )
        self.chkTermo = ttk.Checkbutton(self.cadastroFrame,style="TCheckbutton")
        self.chkTermo.state(['!alternate'])
        self.chkTermo.place(x= x_entry,y = y_inicio + y_cad*8 + 3)

        ####################################################################################
        
        #AMBIENTE DE DOCUMENTOS
        self.docsFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.docsFrame.place(x = 420,y=50)
        self.docsLabel = Label(self.jan,text = "DOCUMENTOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.docsLabel.place(x = 420, y = 15)

        #.CER
        self.CERLabel = Label(self.docsFrame,text = "Arquivo .CER ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CERLabel.place(x=x_label_check,y = y_inicio )
        self.chkCER = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCER.state(['!alternate'])
        self.chkCER.place(x=x_check ,y = y_inicio + 3)

        #CTPS
        self.CTPSLabel = Label(self.docsFrame,text = "CTPS ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CTPSLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
        self.chkCTPS = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCTPS.state(['!alternate'])
        self.chkCTPS.place(x=x_check ,y = y_inicio + y_cad2)

        #Copia CPF
        self.CPFLabel = Label(self.docsFrame,text = "Cópia do CPF ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CPFLabel.place(x=x_label_check,y = y_inicio + y_cad2*2 )
        self.chkCCPF = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCCPF.state(['!alternate'])
        self.chkCCPF.place(x=x_check ,y = y_inicio + y_cad2*2 + 3)

        #Copia docs
        self.CDocLabel = Label(self.docsFrame,text = "Cópia de Documento Com Foto ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CDocLabel.place(x=x_label_check,y = y_inicio + y_cad2*3 )
        self.chkCDoc = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCDoc.state(['!alternate'])
        self.chkCDoc.place(x=x_check ,y = y_inicio + y_cad2*3 + 3)

        #Titulo
        self.TituloLabel = Label(self.docsFrame,text = "Copia do Título de Eleitor ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TituloLabel.place(x=x_label_check,y = y_inicio + y_cad2*4 )
        self.chkTitulo = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkTitulo.state(['!alternate'])
        self.chkTitulo.place(x=x_check ,y = y_inicio + y_cad2*4 + 3)

        #Curriculo
        self.CurrLabel = Label(self.docsFrame,text = "Curriculo  ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CurrLabel.place(x=x_label_check,y = y_inicio + y_cad2*5 )
        self.chkCurr = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCurr.state(['!alternate'])
        self.chkCurr.place(x=x_check ,y = y_inicio + y_cad2*5 + 3)

        #escolar
        self.escolarLabel = Label(self.docsFrame,text = "Escolaridade ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.escolarLabel.place(x=x_label_check,y = y_inicio + y_cad2*6 )
        self.chkescolar = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkescolar.state(['!alternate'])
        self.chkescolar.place(x=x_check ,y = y_inicio + y_cad2*6 + 3)

        #declaracao de endereco
        self.DEndLabel = Label(self.docsFrame,text = "Declaração de Endereço ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.DEndLabel.place(x=x_label_check,y = y_inicio + y_cad2*7 )
        self.chkDEnd = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkDEnd.state(['!alternate'])
        self.chkDEnd.place(x=x_check ,y = y_inicio + y_cad2*7 + 3)

        #roteiro entrevista
        self.REntrLabel = Label(self.docsFrame,text = "Roteiro Entrevista ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.REntrLabel.place(x=x_label_check,y = y_inicio + y_cad2*8 )
        self.chkREntr = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkREntr.state(['!alternate'])
        self.chkREntr.place(x=x_check ,y = y_inicio + y_cad2*8 + 3)

        #Certificado do Curso de Agr
        self.CursoLabel = Label(self.docsFrame,text = "Certificado do Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CursoLabel.place(x=x_label_check,y = y_inicio + y_cad2*9 )
        self.chkCurso = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCurso.state(['!alternate'])
        self.chkCurso.place(x=x_check ,y = y_inicio + y_cad2*9 + 3)

        ######################################################################

        #AMBIENTE DE PROGRESSO
        self.progFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.progFrame.place(x = 820,y=50)
        self.progLabel = Label(self.jan,text = "PROGRESSO",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.progLabel.place(x = 820, y = 15)

        #Curso de Agr
        self.CursoLabel = Label(self.progFrame,text = "Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CursoLabel.place(x=10,y = y_inicio )
        self.lista_situacoes = ['Concluído','Em Andamento','Não Solicitado']
        self.CursoEntry = AutocompleteCombobox(self.progFrame, width = 30,background=cor)
        self.CursoEntry.set_completion_list(self.lista_situacoes)
        self.CursoEntry.place(x=140 ,y = y_inicio+ 3)

        #Parametrizacao
        self.ParametLabel = Label(self.progFrame,text = "Parametrização ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.ParametLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
        self.chkParamet = ttk.Checkbutton(self.progFrame,style="TCheckbutton")
        self.chkParamet.state(['!alternate'])
        self.chkParamet.place(x=x_check ,y = y_inicio + y_cad2 + 3)
        
        #Treinamento
        self.TreinLabel = Label(self.progFrame,text = "Treinamento ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TreinLabel.place(x=x_label_check + 200,y = y_inicio + y_cad2 )
        self.chkTrein = ttk.Checkbutton(self.progFrame,style="TCheckbutton")
        self.chkTrein.state(['!alternate'])
        self.chkTrein.place(x=x_check+200,y = y_inicio + y_cad2 + 3)


        style = ttk.Style()
        style.configure("TCheckbutton", foreground="white", background="black",font=('Helvetica', 22))
        '''

        '''
        #Data

        self.dataLabel = Label(self.cadastroFrame,text = "Data: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.dataLabel.place(x = 10,y = y_inicio + y_cad*8 )
        self.dataEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.dataEntry.bind("<KeyRelease>", format_data)
        self.dataEntry.place(x = x_entry, y = y_inicio + y_cad*8)
        self.dataEntry.insert(0, data)

        #Status
        self.chkStatus = ttk.Checkbutton(self.cadastroFrame, text='Ativo')
        self.chkStatus.state(['!alternate'])
        self.chkStatus.place(x= 10,y = y_inicio + y_cad*9)

        #Treinamento
        self.chkTrein = ttk.Checkbutton(self.cadastroFrame,text='Treinamento')
        self.chkTrein.state(['!alternate'])
        self.chkTrein.place(x= 10,y = y_inicio + y_cad*10 - 10)

        #Parametrização
        self.chkPar = ttk.Checkbutton(self.cadastroFrame,text='Parametrização')
        self.chkPar.state(['!alternate'])
        self.chkPar.place(x= 10,y = y_inicio + y_cad*11 - 20)
        '''
    
    def Cadastrar(self):
        #Criar Janela
        self.jan = Tk()

        #CONFIGURACOES ----
        #Titulo
        self.jan.title("CADASTRO")
        #Tamanho da Janela
        self.jan.geometry(str(800)+"x"+str(650))
        #Cor de Fundo
        self.jan.configure(background = cor)
        #Nao redimensionar
        self.jan.resizable(width = False, height = False)
        #Transparencia
        self.jan.attributes("-alpha",0.99)

        x_entry = 95
        y_inicio = 30
        y_cad = 55
        width_entry = 28
        width_entry_p = 39
        y_cad2 = 50
        x_check = 10
        x_label_check = 40

        ############################################################################

        #AMBIENTE DE DADOS
        self.cadastroFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.cadastroFrame.place(x = 20,y=50)
        self.cadastroLabel = Label(self.jan,text = "DADOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.cadastroLabel.place(x = 20, y = 15)

        #NOME
        self.nomeLabel = Label(self.cadastroFrame,text = "Nome: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.nomeLabel.place(x = 10,y = y_inicio)
        self.nomeEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.nomeEntry.place(x = x_entry, y = y_inicio)

        #CPF
        

        self.cpfLabel = Label(self.cadastroFrame,text = "CPF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.cpfLabel.place(x = 10,y = y_inicio + y_cad )
        self.cpfEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.cpfEntry.bind("<KeyRelease>", self.format_cpf)
        self.cpfEntry.place(x = x_entry, y = y_inicio + y_cad)

        #POSTO
        self.postoLabel = Label(self.cadastroFrame,text = "Posto: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.postoLabel.place(x = 10,y = y_inicio + y_cad*2 )
        self.postoEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor,height=15)
        self.postoEntry.set_completion_list(lista_posto)
        self.postoEntry.place(x = x_entry, y = y_inicio + y_cad * 2)

        #CIDADE
        self.cidadeLabel = Label(self.cadastroFrame,text = "Cidade: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.cidadeLabel.place(x = 10,y = y_inicio + y_cad*3 )
        #lista_cidade = ["Ponta Pora","Campo Grande","Dourados"]
        self.cidadeEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor,height=15)
        self.cidadeEntry.set_completion_list(lista_cidade)
        self.cidadeEntry.place(x = x_entry, y = y_inicio + y_cad*3 + 2 )

        #UF
        self.ufLabel = Label(self.cadastroFrame,text = "UF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.ufLabel.place(x = 10,y = y_inicio + y_cad*4 )
        self.lista_uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
        self.ufEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p,background=cor)
        self.ufEntry.set_completion_list(self.lista_uf)
        self.ufEntry.place(x = x_entry, y = y_inicio + y_cad*4 + 2)

        #E-mail
        self.emailLabel = Label(self.cadastroFrame,text = "E-mail: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.emailLabel.place(x = 10,y = y_inicio + y_cad*5 )
        self.emailEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.emailEntry.place(x = x_entry, y = y_inicio + y_cad*5)

        #Telefone
        
        self.telLabel = Label(self.cadastroFrame,text = "Telefone: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.telLabel.place(x = 10,y = y_inicio + y_cad*6 )
        self.telEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.telEntry.bind("<KeyRelease>", self.format_tel)
        self.telEntry.place(x = x_entry, y = y_inicio + y_cad*6)

        #Parceira
        self.parcLabel = Label(self.cadastroFrame,text = "Parceira: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.parcLabel.place(x = 10,y = y_inicio + y_cad*7 )
        self.lista_parc = ["Soluti","Meta","Soluti/Meta"]
        self.parcEntry = AutocompleteCombobox(self.cadastroFrame, width = width_entry_p)
        self.parcEntry.set_completion_list(self.lista_parc)
        self.parcEntry.place(x = x_entry, y = y_inicio + y_cad*7 + 2)

        '''
        #Termo
        self.TermoLabel = Label(self.cadastroFrame,text = "Termo ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TermoLabel.place(x= 10,y = y_inicio + y_cad*8 )
        self.chkTermo = ttk.Checkbutton(self.cadastroFrame,style="TCheckbutton")
        self.chkTermo.state(['!alternate'])
        self.chkTermo.place(x= x_entry,y = y_inicio + y_cad*8 + 3)

        '''
        ####################################################################################
        
        #AMBIENTE DE DOCUMENTOS
        self.docsFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.docsFrame.place(x = 420,y=50)
        self.docsLabel = Label(self.jan,text = "DOCUMENTOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.docsLabel.place(x = 420, y = 15)

        #.CER
        self.CERLabel = Label(self.docsFrame,text = "Arquivo .CER ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CERLabel.place(x=x_label_check,y = y_inicio )
        self.chkCER = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCER.state(['!alternate'])
        self.chkCER.place(x=x_check ,y = y_inicio + 3)

        #CTPS
        self.CTPSLabel = Label(self.docsFrame,text = "CTPS ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CTPSLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
        self.chkCTPS = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCTPS.state(['!alternate'])
        self.chkCTPS.place(x=x_check ,y = y_inicio + y_cad2)

        #Copia CPF
        self.CPFLabel = Label(self.docsFrame,text = "Cópia do CPF ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CPFLabel.place(x=x_label_check,y = y_inicio + y_cad2*2 )
        self.chkCCPF = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCCPF.state(['!alternate'])
        self.chkCCPF.place(x=x_check ,y = y_inicio + y_cad2*2 + 3)

        #Copia docs
        self.CDocLabel = Label(self.docsFrame,text = "Cópia de Documento Com Foto ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CDocLabel.place(x=x_label_check,y = y_inicio + y_cad2*3 )
        self.chkCDoc = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCDoc.state(['!alternate'])
        self.chkCDoc.place(x=x_check ,y = y_inicio + y_cad2*3 + 3)

        #Titulo
        self.TituloLabel = Label(self.docsFrame,text = "Copia do Título de Eleitor ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TituloLabel.place(x=x_label_check,y = y_inicio + y_cad2*4 )
        self.chkTitulo = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkTitulo.state(['!alternate'])
        self.chkTitulo.place(x=x_check ,y = y_inicio + y_cad2*4 + 3)

        #Curriculo
        self.CurrLabel = Label(self.docsFrame,text = "Curriculo  ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CurrLabel.place(x=x_label_check,y = y_inicio + y_cad2*5 )
        self.chkCurr = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCurr.state(['!alternate'])
        self.chkCurr.place(x=x_check ,y = y_inicio + y_cad2*5 + 3)

        #escolar
        self.escolarLabel = Label(self.docsFrame,text = "Escolaridade ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.escolarLabel.place(x=x_label_check,y = y_inicio + y_cad2*6 )
        self.chkescolar = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkescolar.state(['!alternate'])
        self.chkescolar.place(x=x_check ,y = y_inicio + y_cad2*6 + 3)

        #declaracao de endereco
        self.DEndLabel = Label(self.docsFrame,text = "Declaração de Endereço ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.DEndLabel.place(x=x_label_check,y = y_inicio + y_cad2*7 )
        self.chkDEnd = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkDEnd.state(['!alternate'])
        self.chkDEnd.place(x=x_check ,y = y_inicio + y_cad2*7 + 3)

        #roteiro entrevista
        self.REntrLabel = Label(self.docsFrame,text = "Roteiro Entrevista ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.REntrLabel.place(x=x_label_check,y = y_inicio + y_cad2*8 )
        self.chkREntr = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkREntr.state(['!alternate'])
        self.chkREntr.place(x=x_check ,y = y_inicio + y_cad2*8 + 3)

        #Certificado do Curso de Agr
        self.CursoLabel = Label(self.docsFrame,text = "Certificado do Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CursoLabel.place(x=x_label_check,y = y_inicio + y_cad2*9 )
        self.chkCurso = ttk.Checkbutton(self.docsFrame,style="TCheckbutton")
        self.chkCurso.state(['!alternate'])
        self.chkCurso.place(x=x_check ,y = y_inicio + y_cad2*9 + 3)

        ######################################################################

        #AMBIENTE DE PROGRESSO
        self.progFrame = Frame(self.jan, width = 360, height = 530, bg=cor_escura,relief="raise")
        self.progFrame.place(x = 820,y=50)
        self.progLabel = Label(self.jan,text = "PROGRESSO",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
        self.progLabel.place(x = 820, y = 15)

        #Curso de Agr
        self.CursoLabel = Label(self.progFrame,text = "Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.CursoLabel.place(x=10,y = y_inicio )
        self.lista_situacoes = ['Concluído','Em Andamento','Não Solicitado']
        self.CursoEntry = AutocompleteCombobox(self.progFrame, width = 30,background=cor)
        self.CursoEntry.set_completion_list(self.lista_situacoes)
        self.CursoEntry.place(x=140 ,y = y_inicio+ 3)

        #Parametrizacao
        self.ParametLabel = Label(self.progFrame,text = "Parametrização ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.ParametLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
        self.chkParamet = ttk.Checkbutton(self.progFrame,style="TCheckbutton")
        self.chkParamet.state(['!alternate'])
        self.chkParamet.place(x=x_check ,y = y_inicio + y_cad2 + 3)
        
        #Treinamento
        self.TreinLabel = Label(self.progFrame,text = "Treinamento ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.TreinLabel.place(x=x_label_check + 200,y = y_inicio + y_cad2 )
        self.chkTrein = ttk.Checkbutton(self.progFrame,style="TCheckbutton")
        self.chkTrein.state(['!alternate'])
        self.chkTrein.place(x=x_check+200,y = y_inicio + y_cad2 + 3)


        style = ttk.Style()
        style.configure("TCheckbutton", foreground="white", background="black",font=('Helvetica', 22))
        

        '''
        #Data

        self.dataLabel = Label(self.cadastroFrame,text = "Data: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
        self.dataLabel.place(x = 10,y = y_inicio + y_cad*8 )
        self.dataEntry = Entry(self.cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
        self.dataEntry.bind("<KeyRelease>", format_data)
        self.dataEntry.place(x = x_entry, y = y_inicio + y_cad*8)
        self.dataEntry.insert(0, data)

        #Status
        self.chkStatus = ttk.Checkbutton(self.cadastroFrame, text='Ativo')
        self.chkStatus.state(['!alternate'])
        self.chkStatus.place(x= 10,y = y_inicio + y_cad*9)

        #Treinamento
        self.chkTrein = ttk.Checkbutton(self.cadastroFrame,text='Treinamento')
        self.chkTrein.state(['!alternate'])
        self.chkTrein.place(x= 10,y = y_inicio + y_cad*10 - 10)

        #Parametrização
        self.chkPar = ttk.Checkbutton(self.cadastroFrame,text='Parametrização')
        self.chkPar.state(['!alternate'])
        self.chkPar.place(x= 10,y = y_inicio + y_cad*11 - 20)
        '''


    def Salvar(self):
        #Nome,CPF, Posto, Cidade, UF, email, telefone, parceira, data, status, treinamento, parametrizacao, termo
        txt = ""
        #NOME
        nome = self.nomeEntry.get()
        if nome == "":
            txt += "Nome Inválido!\n"
            self.nomeEntry.delete(0,END) 
        
        #CPF
        cpf = self.cpfEntry.get()
        if cpf == "":
            txt += "CPF Inválido!\n"
            self.cpfEntry.delete(0,END)

        #POSTO
        posto = self.postoEntry.get()
        if posto == "":
            txt = txt + "Posto Inválido!\n"

        #CIDADE
        cidade = self.cidadeEntry.get()
        if cidade == "":
            txt = txt + "Cidade Inválida!\n"

        #UF
        uf = self.ufEntry.get()
        if uf == "" or uf not in self.lista_uf:
            txt = txt + "UF Inválido!\n"

        #EMAIL
        email = self.emailEntry.get()
        if email == "":
            txt = txt + "E-mail Inválido!\n"

        #TELEFONE
        tel =  self.telEntry.get()
        if tel == "":
            txt = txt + "Telefone Inválido!\n"

        #Parceira
        parc =  self.parcEntry.get()
        if parc == "" or parc not in self.lista_parc:
            txt = txt + "Parceira Inválida!\n"
        
        '''
        #DATA
        data = dataEntry.get()
        if data == "":
            txt = txt + "Data Inválida!\n"
        
        #Status
        Status = "Ativo"
        if 'selected' not in self.chkStatus.state():
            Status = "Inativo"

        #Treinamento
        Trein = "Sim"
        if 'selected' not in self.chkTrein.state():
            Trein = "Não"
        
        #Parametrizacao
        Par = "Sim"
        if 'selected' not in  self.chkPar.state():
            Par = "Não"
        
        #Termo
        Termo = "Sim"
        if 'selected' not in self.chkTermo.state():
            Termo = "Não"
        '''

        #CASO TUDO ESTEJA CORRETO
        if txt == "":
            
            #CADASTRA NO BANCO DE DADOS
            conn,cursor = Banco.conectar()

            #Banco.Inserir(nome,cpf,posto,cidade,uf,tel,email,Par,Status,Termo,parc,Trein,data)
            Banco.Inserir(nome,cpf,posto,cidade,uf,tel,email,'Status',parc)

            #MOSTRA MENSAGEM DE SUCESSO
            messagebox.showinfo(title="SUCESSO!", message="Atendimento Cadastrado com Sucesso!")

            #LIMPA AS SELEÇÕES E TEXTOS
            self.nomeEntry.delete(0,END)
            self.cpfEntry.delete(0,END)
            self.postoEntry.delete(0,END)
            self.cidadeEntry.delete(0,END)
            self.ufEntry.delete(0,END)
            self.telEntry.delete(0,END)
            self.emailEntry.delete(0,END)
            self.parcEntry.delete(0,END)
            #dataEntry.delete(0,END)

            #self.chkStatus.state(['!alternate'])
            #self.chkPar.state(['!alternate'])
            #self.chkTermo.state(['!alternate'])
            #self.chkTrein.state(['!alternate'])

            #ALTERA A QUANTIDADE DE ATENDIMENTOS
            qtd_agr = Banco.Contagem()
            qtd_ativos = len(Banco.Select_Where("STATUS","Ativo"))

            self.qtd['text'] = str(qtd_agr)
            self.qtd_Atv['text'] = str(qtd_ativos)

            self.qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
            self.qtd.place(relx=0.5, rely=0.5,anchor=CENTER)
            
            uID = Banco.Ultima_ID()
            new = Banco.Select_Where("ID",uID)[0]
            self.listagem.insert('', 'end', values=new)
            self.listagem.place(x = 0, y = 0, width = 525, height = 305)

            self.jan.destroy()
        else:
            #CASO DE ERRADO
            self.Mensagem_Aviso(txt)


        #BOTAO DE Salvar
        #Cadastrar funçaõ salvar
        self.cadastroButton = Button(self.jan, text = "Salvar", bg=cor, fg=cor_contraste, width = 40, command=self.Salvar)
        self.cadastroButton.place(x = 50, y = 600 )

