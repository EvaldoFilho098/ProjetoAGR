from tkinter import LabelFrame, Tk, StringVar,IntVar,DISABLED, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X,N,E,S,W, font
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import FALSE
from typing import Sized
import img
from var import *
from PIL import Image,ImageTk
import ToolTip as TP
from Classes import AutocompleteCombobox
import Banco
import Janela
from class_agr import AGR

class informacoes:
    def __init__(self,toplevel,id):
        agr = AGR(id)
        #CONFIGURACOES ----
        #Titulo
        toplevel.title(titulos)
        #Tamanho da toplevelela
        toplevel.geometry(str(largura+100)+"x"+str(altura+100))
        #Cor de Fundo
        toplevel.configure(background = cor_escura)
        #Nao redimensionar
        toplevel.resizable(width = False, height = False)
        #Transparencia
        toplevel.attributes("-alpha",0.96)
        #Icone
        toplevel.iconbitmap(default="Icons/icon.ico")
        #Logo
        self.logo = PhotoImage(file="icons/logo_.png")

        x_primeira = 35
        x_segunda = 435
        x_terceira = 735

        y_1 = 5
        y_2 = 40
        y_3 = 80
        y_4 = 120

        check = 25

        '''
        rsz_x = rsz_y = 25
        img_sim_o= (Image.open("Icons\\confirmacao.png"))
        img_sim= img.resizing(img_sim_o,rsz_x,rsz_y) #icone de confirmacao
        #img_nao= img.resizing(img_nao_o,rsz_x,rsz_y) #icone de negacao
        '''

        #TOPO
        self.TopFrame = Frame(toplevel, width = largura+100, height = 30, bg = cor_meta, relief = "raise" )
        self.TopFrame.pack(side=TOP)
        self.TopLabel = Label(self.TopFrame,text="Informações",font=fonte_Mediana,background=cor_escura,foreground=cor_contraste)
        self.TopLabel.place(x=50,y=0)
        #RODAPE
        self.BottomFrame = Frame(toplevel, width = largura+100, height = 30, bg = cor_meta, relief = "raise" )
        self.BottomFrame.pack(side=BOTTOM)
        self.BottomLabel = Label(self.BottomFrame,text="META",font=fonte_Mediana,background=cor_escura,foreground=cor_contraste)
        self.BottomLabel.place(x=1000,y=0)
        #NOME E STATUS
        self.NomeFrame = Frame(toplevel, width = largura, height = 100, bg = cor_escura, relief = "raise" )
        self.NomeFrame.pack(side=TOP)

        nome = agr.Nome.split(' ')
        if len(nome) > 1:
            nome = nome[0] + ' ' + nome[-1]
        self.NomeLabel = Label(self.NomeFrame,text= nome.upper(),font=fonte_Titulos,background=cor_escura,foreground=cor_contraste)
        self.NomeLabel.place(x=0,y=30)

        agr.Atualiza_Situacao()
        self.StatusLabel = Label(self.NomeFrame,text=agr.Status.upper(),font=fonte_Destaques,background=cor_escura,foreground=cor_contraste)
        self.StatusLabel.place(x=850,y=30)

        '''
        #IMAGEM STATUS
        self.Status_imgFrame = Frame(self.NomeFrame, width = 40, height = 40, bg = cor, relief = "raise" )
        self.Status_imgFrame.place(x=800,y=40)
        self.Status_imgLabel = Label(self.Status_imgFrame, image=img_sim,background=cor)
        self.Status_imgLabel.place(x=0,y=0)
        '''

        #INFO PESSOAIS
        
        self.InfosFrame = Frame(toplevel, width = largura, height = 150, bg = cor, relief = "raise" )
        self.InfosFrame.place(x=50,y=150)
        self.BotaoMudar = Button(self.InfosFrame,width=3,background=cor_escura)
        self.BotaoMudar.place(x=993,y=0)
        self.InfosLabel = Label(self.InfosFrame,text="Informações Pessoais",font=fonte_Mediana_2,background=cor_escura,foreground=cor_contraste)
        self.InfosLabel.place(x=0,y=0)
        self.NomeLabel = Label(self.InfosFrame,text="Nome Completo: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.NomeLabel.place(x=x_primeira,y=y_2)
        self.NomeLabel_ = Label(self.InfosFrame,text=agr.Nome.upper(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.NomeLabel_.place(x=x_primeira + 140 ,y=y_2)

        self.CPFLabel = Label(self.InfosFrame,text="CPF: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.CPFLabel.place(x=x_primeira,y=y_3)
        self.CPFLabel_ = Label(self.InfosFrame,text=agr.CPF,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.CPFLabel_.place(x=x_primeira + 40,y=y_3)

        self.CidadeLabel = Label(self.InfosFrame,text="Cidade: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.CidadeLabel.place(x=x_primeira,y=y_4)
        self.CidadeLabel_ = Label(self.InfosFrame,text=agr.Cidade.upper() + " - " + agr.UF.upper(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.CidadeLabel_.place(x=x_primeira + 70 ,y=y_4)

        self.PostoLabel = Label(self.InfosFrame,text="Posto: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.PostoLabel.place(x=x_segunda + 190,y=y_1)
        self.PostoLabel_ = Label(self.InfosFrame,text=agr.Posto,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.PostoLabel_.place(x=x_segunda + 190 + 55,y=y_1)

        self.TelefoneLabel = Label(self.InfosFrame,text="Telefone: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.TelefoneLabel.place(x=x_segunda + 190,y=y_2)
        self.TelefoneLabel_ = Label(self.InfosFrame,text=agr.Telefone,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.TelefoneLabel_.place(x=x_segunda + 190 + 75,y=y_2)

        self.EmailLabel = Label(self.InfosFrame,text="E-mail: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.EmailLabel.place(x=x_segunda + 190,y=y_3)
        self.EmailLabel_ = Label(self.InfosFrame,text=agr.Email,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.EmailLabel_.place(x=x_segunda + 190 + 55,y=y_3)

        self.ParceiraLabel = Label(self.InfosFrame,text="Parceira: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.ParceiraLabel.place(x=x_segunda + 190,y=y_4)
        self.ParceiraLabel_ = Label(self.InfosFrame,text=agr.Parceira.upper(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.ParceiraLabel_.place(x=x_segunda + 190 + 75,y=y_4)

        #DOCS
        #CER,CTPS,COPIA_CPF,COPIA_DOC,TITULO,CURRICULO,ESCOLARIDADE,DECL_END,ROTEIRO_ENT,CERT_CURSO
        self.DocsFrame = Frame(toplevel, width = largura, height = 150, bg = cor, relief = "raise" )
        self.DocsFrame.place(x=50,y=320)
        self.BotaoMudar_2 = Button(self.DocsFrame,width=3,background=cor_escura)
        self.BotaoMudar_2.place(x=993,y=0)
        self.DocsLabel = Label(self.DocsFrame,text="Documentos",font=fonte_Mediana_2,background=cor_escura,foreground=cor_contraste)
        self.DocsLabel.place(x=0,y=0)

        self.CERLabel = Label(self.DocsFrame,text=".CER ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.CERLabel.place(x=x_primeira + 25,y=y_2)
        self.chkCER = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.CER == "OK":
            self.chkCER.state(['selected','disabled'])
        else:
            self.chkCER.state(['!alternate','disabled'])
        #self.chkCER.state(['!alternate'])
        self.chkCER.place(x=x_primeira,y = y_2 + 2)

        self.CTPSLabel = Label(self.DocsFrame,text="CTPS ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.CTPSLabel.place(x=x_primeira + 25,y=y_3)
        self.chkCTPS = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.CTPS == "OK":
            self.chkCTPS.state(['selected','disabled'])
        else:
            self.chkCTPS.state(['!alternate','disabled'])
        #self.chkCTPS.state(['!alternate'])
        self.chkCTPS.place(x=x_primeira,y = y_3 + 2)

        self.Copia_CPFLabel = Label(self.DocsFrame,text="Cópia do CPF e Documentos ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.Copia_CPFLabel.place(x=x_primeira + 25,y=y_4)
        self.chkCopia_CPF = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Copia_CPF == "OK":
            self.chkCopia_CPF.state(['selected','disabled'])
        else:
            self.chkCopia_CPF.state(['!alternate','disabled'])
        #self.chkCopia_CPF.state(['!alternate'])
        self.chkCopia_CPF.place(x=x_primeira,y = y_4 + 2)

        '''
        self.Copia_DocLabel = Label(self.DocsFrame,text="Cópia de Documento ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.Copia_DocLabel.place(x=x_segunda,y=y_1)
        self.chkCopia_Docs = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        #self.chkCopia_Docs.state(['!alternate'])
        self.chkCopia_Docs.place(x=x_segunda - check,y = y_1 + 2)
        '''

        self.TituloLabel = Label(self.DocsFrame,text="Título de Eleitor ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.TituloLabel.place(x=x_segunda,y=y_1)

        self.chkTitulo = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Titulo == "OK":
            self.chkTitulo.state(['selected','disabled'])
        else:
            self.chkTitulo.state(['!alternate','disabled'])
        #self.chkTitulo.state(['!alternate'])
        self.chkTitulo.place(x=x_segunda - check,y = y_1 + 2)

        self.CurriculoLabel = Label(self.DocsFrame,text="Currículo ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.CurriculoLabel.place(x=x_segunda,y=y_2 + 20)
        self.chkCurriculo = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Curriculo == "OK":
            self.chkCurriculo.state(['selected','disabled'])
        else:
            self.chkCurriculo.state(['!alternate','disabled'])
        #self.chkCurriculo.state(['!alternate'])
        self.chkCurriculo.place(x=x_segunda - check,y = y_2 + 20 + 2)

        self.EscolaridadeLabel = Label(self.DocsFrame,text="Escolaridade ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.EscolaridadeLabel.place(x=x_segunda,y=y_4)
        self.chkEscolaridade = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Escolaridade == "OK":
            self.chkEscolaridade.state(['selected','disabled'])
        else:
            self.chkEscolaridade.state(['!alternate','disabled'])
        #self.chkEscolaridade.state(['!alternate'])
        self.chkEscolaridade.place(x=x_segunda - check,y = y_4 + 2)

        self.Dec_EndLabel = Label(self.DocsFrame,text="Declaração de Endereço ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.Dec_EndLabel.place(x=x_terceira,y=y_1)
        self.chkDec_End = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Decl_Endereco == "OK":
            self.chkDec_End.state(['selected','disabled'])
        else:
            self.chkDec_End.state(['!alternate','disabled'])
        #self.chkDec_End.state(['!alternate'])
        self.chkDec_End.place(x=x_terceira - check,y = y_1 + 2)

        self.Rot_EntLabel = Label(self.DocsFrame,text="Roteiro da Entrevista ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.Rot_EntLabel.place(x=x_terceira,y=y_2 + 20)
        self.chkRot_Ent = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Roteiro_Entrevista == "OK":
            self.chkRot_Ent.state(['selected','disabled'])
        else:
            self.chkRot_Ent.state(['!alternate','disabled'])
        #self.chkRot_Ent.state(['!alternate'])
        self.chkRot_Ent.place(x=x_terceira - check,y = y_2 + 20 + 2)

        self.Cert_CursoLabel = Label(self.DocsFrame,text="Certificado do Curso de AGR ",font=fonte_Textos,background=cor_escura
        ,foreground=cor_contraste)
        self.Cert_CursoLabel.place(x=x_terceira,y=y_4)
        self.chkCert_Curso = ttk.Checkbutton(self.DocsFrame,style="TCheckbutton")
        if agr.Cert_Curso == "OK":
            self.chkCert_Curso.state(['selected','disabled'])
        else:
            self.chkCert_Curso.state(['!alternate','disabled'])
        #self.chkCert_Curso.state(['!alternate'])
        self.chkCert_Curso.place(x=x_terceira - check,y = y_4 + 2)

        #Situacoes
        self.SituFrame = Frame(toplevel, width = largura, height = 150, bg = cor, relief = "raise" )
        self.SituFrame.place(x=50,y=490)
        self.BotaoMudar_3 = Button(self.SituFrame,width=3,background=cor_escura)
        self.BotaoMudar_3.place(x=993,y=0)
        self.SituLabel = Label(self.SituFrame,text="Situações ",font=fonte_Mediana_2,background=cor_escura,foreground=cor_contraste)
        self.SituLabel.place(x=0,y=0)

        
        self.VenCert = Label(self.SituFrame,text="Vencimento do Certificado: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.VenCert.place(x=x_primeira,y=y_2)
        self.VenCert_ = Label(self.SituFrame,text=agr.Vencimento_Cert,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.VenCert_.place(x=x_primeira + 140 ,y=y_2)

        self.DiasCert = Label(self.SituFrame,text="Dias Restantes Do Certificado ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.DiasCert.place(x=x_primeira,y=y_3)
        self.DiasCert_ = Label(self.SituFrame,text=agr.Expirar(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.DiasCert_.place(x=x_primeira + 40,y=y_3)

        self.VenCurso = Label(self.SituFrame,text="Vencimento do Curso: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.VenCurso.place(x=x_primeira,y=y_4)
        self.VenCurso_ = Label(self.SituFrame,text=agr.Data_Curso + " - " + agr.UF.upper(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.VenCurso_.place(x=x_primeira + 70 ,y=y_4)

        self.PostoLabel = Label(self.SituFrame,text="Posto: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.PostoLabel.place(x=x_segunda + 190,y=y_1)
        self.PostoLabel_ = Label(self.SituFrame,text=agr.Posto,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.PostoLabel_.place(x=x_segunda + 190 + 55,y=y_1)

        self.TelefoneLabel = Label(self.SituFrame,text="Telefone: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.TelefoneLabel.place(x=x_segunda + 190,y=y_2)
        self.TelefoneLabel_ = Label(self.SituFrame,text=agr.Telefone,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.TelefoneLabel_.place(x=x_segunda + 190 + 75,y=y_2)

        self.EmailLabel = Label(self.SituFrame,text="E-mail: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.EmailLabel.place(x=x_segunda + 190,y=y_3)
        self.EmailLabel_ = Label(self.SituFrame,text=agr.Email,font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.EmailLabel_.place(x=x_segunda + 190 + 55,y=y_3)

        self.ParceiraLabel = Label(self.SituFrame,text="Parceira: ",font=fonte_Textos,background=cor,foreground=cor_contraste)
        self.ParceiraLabel.place(x=x_segunda + 190,y=y_4)
        self.ParceiraLabel_ = Label(self.SituFrame,text=agr.Parceira.upper(),font=fonte_Textos,background=cor_escura,foreground=cor_contraste)
        self.ParceiraLabel_.place(x=x_segunda + 190 + 75,y=y_4)
        '''
        #Logo da Meta e Titulo do programa
        self.logo_meta = Label(self.TopFrame, image=self.logo,bg=cor)
        self.logo_meta.place(x=10,y=5)
        self.meta = Label(self.TopFrame,text = "Controle de AGR's",font=fonte_Titulos, fg= cor_contraste, bg=cor)
        self.meta.place(x=340,y=25)

        #AMBIENTE DE INFORMACOES 1
        self.infosFrame = Frame(toplevel, width = 960, height = 450, bg=cor,relief="raise")
        self.infosFrame.place(x = 30,y=125)
        '''
    
instancia = Tk()
informacoes(instancia,13)
instancia.mainloop()