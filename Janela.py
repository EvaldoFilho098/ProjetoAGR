from tkinter import LabelFrame, Tk, StringVar,IntVar,DISABLED, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X,N,E,S,W
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import FALSE
from typing import Sized
import img
from var import *
from PIL import Image,ImageTk
import Funcoes
import ToolTip as TP
from Classes import AutocompleteCombobox
import Banco
#from Cadastro import Cadastrar

#Criar Janela
Janela = Tk()

#CONFIGURACOES ----
#Titulo
Janela.title(titulos)
#Tamanho da Janelaela
Janela.geometry(str(largura)+"x"+str(altura))
#Cor de Fundo
Janela.configure(background = cor_meta)
#Nao redimensionar
Janela.resizable(width = False, height = False)
#Transparencia
Janela.attributes("-alpha",0.95)
#Icone
Janela.iconbitmap(default="Icons/icon.ico")
#Logo
logo = PhotoImage(file="icons/logo_.png")

#TITULO
TopFrame = Frame(Janela, width = largura, height = 100, bg = cor, relief = "raise" )
TopFrame.pack(side=TOP)

#Logo da Meta e Titulo do programa
logo_meta = Label(TopFrame, image=logo,bg=cor)
logo_meta.place(x=10,y=5)
meta = Label(TopFrame,text = "Controle de AGR's",font=fonte_Titulos, fg= cor_contraste, bg=cor)
meta.place(x=340,y=25)

#AMBIENTE DE INFORMACOES 1
infosFrame = Frame(Janela, width = 960, height = 450, bg=cor,relief="raise")
infosFrame.place(x = 30,y=125)

#Data 
date = Label(TopFrame,text=data,fg=cor_contraste,bg=cor,font=fonte_Mediana)
date.place(x=865,y=35)

#Quantidade de AGRs
n_Agrs = Label(infosFrame, text="AGR's Cadastrados", fg = cor_contraste, bg=cor, font=fonte_Textos)
n_Agrs.place(x=575,y=5)
frame_aux = Frame(infosFrame, width = 170, height = 50, bg = cor_escura, relief="raise")
frame_aux.place(x=570, y=30)
qtd = Label(frame_aux,text=qtd_agr, bg = cor_escura, fg="red", font=fonte_Destaques)
qtd.place(relx=0.5, rely=0.5,anchor=CENTER)

#Quantidade de Agrs Ativos
n_Ativos = Label(infosFrame, text="AGR's Ativos", fg = cor_contraste, bg=cor, font=fonte_Textos)
n_Ativos.place(x=800,y=5)
frame_auxAtv = Frame(infosFrame, width = 170, height = 50, bg = cor_escura, relief="raise")
frame_auxAtv.place(x=770, y=30)
qtd_Atv = Label(frame_auxAtv,text=qtd_ativos, bg = cor_escura , fg="red", font=fonte_Destaques)
qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)

#, width = 525, height = 325, bg=cor_meta,relief="raise"
#AMBIENTE DE EXIBICAO DE AGRS
AGRs_Frame = LabelFrame(Janela,width = 525, height = 325)
AGRs_Frame.place(x = 50,y=230)
#AGRs_Frame.pack(padx=325,pady=130)

####################################################
dadosCols = ("ID","NOME","CPF","POSTO","CIDADE","UF","STATUS","PARCEIRA",
            "DATA INICIO", "PARAMETRIZACAO", "TREINAMENTO","TERMO",
            "TELEFONE","EMAIL")
listagem = ttk.Treeview(AGRs_Frame,columns = dadosCols,show='headings', height = 100, selectmode='browse')

def Mostrar(event):
    
    
        global listagem
        #, lista_atendimentos,lista_certificados,lista_locais,lista_solicitantes
        #Pega o item selecionado
        """
        "ID","NOME","CPF","POSTO","CIDADE","UF","STATUS","PARCEIRA",
            "DATA INICIO", "PARAMETRIZACAO", "TREINAMENTO","TERMO",
            "TELEFONE","EMAIL" """

        nodeId_1 = listagem.focus()
        
        #Pega as informacoes do item
        id_ = listagem.item(nodeId_1)['values'][0]
        nome_ = listagem.item(nodeId_1)['values'][1]
        cpf_ = listagem.item(nodeId_1)['values'][2]
        posto_ = listagem.item(nodeId_1)['values'][3]
        municipio_ = listagem.item(nodeId_1)['values'][4]
        uf_ = listagem.item(nodeId_1)['values'][5]
        status_ = listagem.item(nodeId_1)['values'][6]
        parceira_ = listagem.item(nodeId_1)['values'][7]
        data_ = listagem.item(nodeId_1)['values'][8]
        par_ = listagem.item(nodeId_1)['values'][9]
        trein_ = listagem.item(nodeId_1)['values'][10]
        termo_ = listagem.item(nodeId_1)['values'][11]
        telefone_ = listagem.item(nodeId_1)['values'][12]
        email_ = listagem.item(nodeId_1)['values'][13]

        Funcoes.Infos_Agrs(nome_,cpf_,posto_, municipio_, uf_, telefone_, email_, par_, termo_, status_, parceira_, trein_,data_ )
    

#print(dadosCols)
listagem.bind('<Double-1>',Mostrar)
minw = 100
#1
listagem.column("ID", width = 30,minwidth=30)
listagem.heading("ID",text="ID")
#2
listagem.column("NOME", width = 30,minwidth=minw)
listagem.heading("NOME",text="NOME")
#3
listagem.column("CPF", width = 50,minwidth=minw)
listagem.heading("CPF",text="CPF")
#4
listagem.column("POSTO", width = 50,minwidth=minw)
listagem.heading("POSTO",text="POSTO")
#5
listagem.column("CIDADE", width = 50,minwidth=minw)
listagem.heading("CIDADE",text="CIDADE")
#6
listagem.column("UF", width = 30,minwidth=30)
listagem.heading("UF",text="UF")
#7
listagem.column("STATUS", width = 30,minwidth=50)
listagem.heading("STATUS",text="STATUS")
#8
listagem.column("PARCEIRA", width = 30,minwidth=minw)
listagem.heading("PARCEIRA",text="PARCEIRA")
#9
listagem.column("DATA INICIO", width = 50,minwidth=70)
listagem.heading("DATA INICIO",text="DATA INICIO")
#10
listagem.column("PARAMETRIZACAO", width = 30,minwidth=50)
listagem.heading("PARAMETRIZACAO",text="PARAMETRIZACAO")
#11
listagem.column("TREINAMENTO", width = 30,minwidth=60)
listagem.heading("TREINAMENTO",text="TREINAMENTO")
#12
listagem.column("TERMO", width = 30,minwidth=50)
listagem.heading("TERMO",text="TERMO")
#13
listagem.column("TELEFONE", width = 50,minwidth=minw)
listagem.heading("TELEFONE",text="TELEFONE")
#14
listagem.column("EMAIL", width = 50,minwidth=minw)
listagem.heading("EMAIL",text="EMAIL")

listagem.place(x = 0, y = 0, width = 525, height = 305)

#BARRAS DE ROLAGEM DA VISUALIZACAO
ysb = ttk.Scrollbar(AGRs_Frame, orient=VERTICAL,command=listagem.yview)
ysb.place(x=506,y=0,height=305)

xsb = ttk.Scrollbar(AGRs_Frame, orient=HORIZONTAL,command=listagem.xview)
xsb.place(x = 2, y = 305, width=510)

listagem.configure(yscroll = ysb.set)
listagem.configure(xscroll = xsb.set)

# TEXTOS DOS CABEÇALHO
for c in dadosCols:
    listagem.heading(c, text=c.title())

# INSRINDO OS ITENS
for item in Banco.Select_Columns(colunas_select):
    listagem.insert('', 'end', values=item,)

#AMBIENTE DE INFORMACOES DO AGR SELECIONADO
info_AGR_Sel_Frame = Frame(Janela, width = 370, height = 325, bg=cor_escura,relief="raise")
info_AGR_Sel_Frame.place(x = 600,y=230)

def Excluir():

    x = messagebox.showwarning(message="Tem Certeza Que Deseja Excluir o AGR Selecionado?")
    if x == 'ok':
    
        global listagem 

        nodeId_1 = listagem.focus()
            
        #Pega as informacoes do item
        id_ = listagem.item(nodeId_1)['values'][0]

        Banco.Deletar(id_)

        #ALTERA A QUANTIDADE DE ATENDIMENTOS
        qtd_agr = Banco.Contagem()
        qtd_ativos = len(Banco.Select_Where("STATUS","Ativo"))

        qtd['text'] = str(qtd_agr)
        qtd_Atv['text'] = str(qtd_ativos)

        qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
        qtd.place(relx=0.5, rely=0.5,anchor=CENTER)

        listagem.delete(nodeId_1)
        listagem.place(x = 0, y = 0, width = 525, height = 305)

        frame_Nome.configure(text='')
        frame_Nome.place(x=x_info,y=0)

        frame_cpf.configure(text='')
        frame_cpf.place(x=x_info + 190,y=y_inicio )

        frame_Status.configure(text='')
        frame_Status.place(x=x_info,y=y_inicio )
        frame_status_img.destroy() 

        frame_Posto.configure(text='')
        frame_Posto.place(x=x_info,y=y_inicio + y_info)

        frame_Municipio.configure(text='')
        frame_Municipio.place(x=x_info,y=y_inicio + y_info*2)

        frame_Email.configure(text='')
        frame_Email.place(x=x_info,y=y_inicio + y_info*3)

        frame_Tel.configure(text='')
        frame_Tel.place(x=x_info,y=y_inicio + y_info*4)

        frame_Parceiro.configure(text='')
        frame_Parceiro.place(x=x_info,y=y_inicio + y_info*5)

        frame_data.configure(text='')
        frame_data.place(x=x_info,y=y_inicio + y_info*6)

        frame_Par.configure(text='')
        frame_Par.place(x=x_info,y=y_inicio + y_info*7)
        frame_Par_img.destroy()

        frame_Treino.configure(text='')
        frame_Treino.place(x=x_info,y=y_inicio + y_info*8)
        frame_Treino_img.destroy()

        frame_Termo.configure(text='')
        frame_Termo.place(x=x_info,y=y_inicio + y_info*9)
        frame_Termo_img.destroy()

        messagebox.showinfo(title="Sucesso!", message="Cadastro Removido com Sucesso!")
    else:
        pass

def Alterar():
    pass

def Cadastrar():
    #Criar Janela
    jan = Tk()

    #CONFIGURACOES ----
    #Titulo
    jan.title("CADASTRO")
    #Tamanho da Janela
    jan.geometry(str(400)+"x"+str(650))
    #Cor de Fundo
    jan.configure(background = cor)
    #Nao redimensionar
    jan.resizable(width = False, height = False)
    #Transparencia
    jan.attributes("-alpha",0.95)

    x_entry = 95
    y_inicio = 30
    y_cad = 40
    width_entry = 28
    width_entry_p = 39

    #AMBIENTE DE CADASTRO
    cadastroFrame = Frame(jan, width = 360, height = 530, bg=cor_escura,relief="raise")
    cadastroFrame.place(x = 20,y=50)
    cadastroLabel = Label(jan,text = "CADASTRO",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
    cadastroLabel.place(x = 135, y = 15)

    #NOME
    nomeLabel = Label(cadastroFrame,text = "Nome: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    nomeLabel.place(x = 10,y = y_inicio)
    nomeEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    nomeEntry.place(x = x_entry, y = y_inicio)

    #CPF
    def format_cpf(event = None):
    
        text = cpfEntry.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]

        cpfEntry.delete(0, "end")
        cpfEntry.insert(0, new_text)

    cpfLabel = Label(cadastroFrame,text = "CPF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    cpfLabel.place(x = 10,y = y_inicio + y_cad )
    cpfEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    cpfEntry.bind("<KeyRelease>", format_cpf)
    cpfEntry.place(x = x_entry, y = y_inicio + y_cad)

    #POSTO
    postoLabel = Label(cadastroFrame,text = "Posto: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    postoLabel.place(x = 10,y = y_inicio + y_cad*2 )
    postoEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    postoEntry.place(x = x_entry, y = y_inicio + y_cad * 2)

    #CIDADE
    cidadeLabel = Label(cadastroFrame,text = "Cidade: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    cidadeLabel.place(x = 10,y = y_inicio + y_cad*3 )
    lista_cidade = ["Ponta Pora"]
    cidadeEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor)
    cidadeEntry.set_completion_list(lista_cidade)
    cidadeEntry.place(x = x_entry, y = y_inicio + y_cad*3 + 2 )

    #UF
    ufLabel = Label(cadastroFrame,text = "UF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    ufLabel.place(x = 10,y = y_inicio + y_cad*4 )
    lista_uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    ufEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor)
    ufEntry.set_completion_list(lista_uf)
    ufEntry.place(x = x_entry, y = y_inicio + y_cad*4 + 2)

    #E-mail
    emailLabel = Label(cadastroFrame,text = "E-mail: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    emailLabel.place(x = 10,y = y_inicio + y_cad*5 )
    emailEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    emailEntry.place(x = x_entry, y = y_inicio + y_cad*5)

    #Telefone
    def format_tel(event = None):
    
        text = telEntry.get().replace("(", "").replace(")","").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue

            if index == 0: new_text += "(" + text[index] 
            elif index == 1: new_text += text[index] + ")"
            elif index == 6: new_text += text[index] + "-"
            else: new_text += text[index]

        telEntry.delete(0, "end")
        telEntry.insert(0, new_text)

    telLabel = Label(cadastroFrame,text = "Telefone: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    telLabel.place(x = 10,y = y_inicio + y_cad*6 )
    telEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    telEntry.bind("<KeyRelease>", format_tel)
    telEntry.place(x = x_entry, y = y_inicio + y_cad*6)

    #Parceira
    parcLabel = Label(cadastroFrame,text = "Parceira: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    parcLabel.place(x = 10,y = y_inicio + y_cad*7 )
    lista_parc = ["Soluti","Safeweb","Soluti/Safeweb"]
    parcEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p)
    parcEntry.set_completion_list(lista_parc)
    parcEntry.place(x = x_entry, y = y_inicio + y_cad*7 + 2)

    
    #Data
    def format_data(event = None):
    
        text = dataEntry.get().replace("/", "")[:8]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue

            if index == 1: new_text +=  text[index] + "/" 
            elif index == 3: new_text += text[index] + "/"
            else: new_text += text[index]

        dataEntry.delete(0, "end")
        dataEntry.insert(0, new_text)

    dataLabel = Label(cadastroFrame,text = "Data: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    dataLabel.place(x = 10,y = y_inicio + y_cad*8 )
    dataEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    dataEntry.bind("<KeyRelease>", format_data)
    dataEntry.place(x = x_entry, y = y_inicio + y_cad*8)
    dataEntry.insert(0, data)

    #Status
    chkStatus = ttk.Checkbutton(cadastroFrame, text='Ativo')
    chkStatus.state(['!alternate'])
    chkStatus.place(x= 10,y = y_inicio + y_cad*9)

    #Treinamento
    chkTrein = ttk.Checkbutton(cadastroFrame,text='Treinamento')
    chkTrein.state(['!alternate'])
    chkTrein.place(x= 10,y = y_inicio + y_cad*10 - 10)

    #Parametrização
    chkPar = ttk.Checkbutton(cadastroFrame,text='Parametrização')
    chkPar.state(['!alternate'])
    chkPar.place(x= 10,y = y_inicio + y_cad*11 - 20)

    #Termo
    chkTermo = ttk.Checkbutton(cadastroFrame, text='Termo')
    chkTermo.state(['!alternate'])
    chkTermo.place(x= 10,y = y_inicio + y_cad*12 - 30)

    
    def Salvar():
        #Nome,CPF, Posto, Cidade, UF, email, telefone, parceira, data, status, treinamento, parametrizacao, termo
        txt = ""
        #NOME
        nome = nomeEntry.get()
        if nome == "":
            txt += "Nome Inválido!\n"
            nomeEntry.delete(0,END) 
        
        #CPF
        cpf = cpfEntry.get()
        if cpf == "":
            txt += "CPF Inválido!\n"
            cpfEntry.delete(0,END)

        #POSTO
        posto = postoEntry.get()
        if posto == "":
            txt = txt + "Posto Inválido!\n"

        #CIDADE
        cidade = cidadeEntry.get()
        if cidade == "":
            txt = txt + "Cidade Inválida!\n"

        #UF
        uf = ufEntry.get()
        if uf == "" or uf not in lista_uf:
            txt = txt + "UF Inválido!\n"

        #EMAIL
        email = emailEntry.get()
        if email == "":
            txt = txt + "E-mail Inválido!\n"

        #TELEFONE
        tel =  telEntry.get()
        if tel == "":
            txt = txt + "Telefone Inválido!\n"

        #Parceira
        parc =  parcEntry.get()
        if parc == "" or parc not in lista_parc:
            txt = txt + "Parceira Inválida!\n"
        
        #DATA
        data = dataEntry.get()
        if data == "":
            txt = txt + "Data Inválida!\n"
        
        #Status
        Status = "Ativo"
        if 'selected' not in chkStatus.state():
            Status = "Inativo"

        #Treinamento
        Trein = "Sim"
        if 'selected' not in chkTrein.state():
            Trein = "Não"
        
        #Parametrizacao
        Par = "Sim"
        if 'selected' not in  chkPar.state():
            Par = "Não"
        
        #Termo
        Termo = "Sim"
        if 'selected' not in chkTermo.state():
            Termo = "Não"

        #CASO TUDO ESTEJA CORRETO
        if txt == "":
            
            #CADASTRA NO BANCO DE DADOS
            conn,cursor = Banco.conectar()

            Banco.Inserir(nome,cpf,posto,cidade,uf,tel,email,Par,Status,Termo,parc,Trein,data)

            #MOSTRA MENSAGEM DE SUCESSO
            messagebox.showinfo(title="SUCESSO!", message="Atendimento Cadastrado com Sucesso!")

            #LIMPA AS SELEÇÕES E TEXTOS
            nomeEntry.delete(0,END)
            cpfEntry.delete(0,END)
            postoEntry.delete(0,END)
            cidadeEntry.delete(0,END)
            ufEntry.delete(0,END)
            telEntry.delete(0,END)
            emailEntry.delete(0,END)
            parcEntry.delete(0,END)
            dataEntry.delete(0,END)

            chkStatus.state(['!alternate'])
            chkPar.state(['!alternate'])
            chkTermo.state(['!alternate'])
            chkTrein.state(['!alternate'])

            #ALTERA A QUANTIDADE DE ATENDIMENTOS
            qtd_agr = Banco.Contagem()
            qtd_ativos = len(Banco.Select_Where("STATUS","Ativo"))

            qtd['text'] = str(qtd_agr)
            qtd_Atv['text'] = str(qtd_ativos)

            qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
            qtd.place(relx=0.5, rely=0.5,anchor=CENTER)
            
            uID = Banco.Ultima_ID()
            new = Banco.Select_Where("ID",uID)[0]
            listagem.insert('', 'end', values=new)
            listagem.place(x = 0, y = 0, width = 525, height = 305)

            jan.destroy()
        else:
            #CASO DE ERRADO
            Funcoes.Mensagem_Aviso(txt)


    #BOTAO DE INSERIR
    #Cadastrar funçaõ inserir
    cadastroButton = Button(jan, text = "Salvar", bg=cor, fg=cor_contraste, width = 30, command=Salvar)
    cadastroButton.place(x = 90, y = 600 )

    jan.mainloop()


rsz_x = 25
rsz_y = 25
w_button = 30
h_button = 30
y_buttons = 35

img_add= img.resizing(img.img_add_o,rsz_x,rsz_y) #icone de adicionar
img_edi= img.resizing(img.img_edi_o,rsz_x,rsz_y) #icone de editar
img_rem= img.resizing(img.img_rem_o,rsz_x,rsz_y) #icone de remover
img_sim= img.resizing(img.img_sim_o,rsz_x,rsz_y) #icone de confirmacao
img_nao= img.resizing(img.img_nao_o,rsz_x,rsz_y) #icone de negacao
img_sim_men= img.resizing(img.img_sim_o,15,15) #icone de confirmacao
img_nao_men= img.resizing(img.img_nao_o,15,15) #icone de negacao
img_sav= img.resizing(img.img_sav_o,rsz_x,rsz_y) #icone de save
img_inf= img.resizing(img.img_inf_o,rsz_x,rsz_y) #icone de informacoes

#Botao de Adicionar AGRq
cadastroButton = Button(infosFrame,image= img_add, bg=cor, fg=cor_contraste, width = w_button, height= h_button,command = Cadastrar)
cadastroButton.place(x = 20 , y = y_buttons)
TP.CreateToolTip(cadastroButton, text = 'Cadastrar')

edicaoButton = Button(infosFrame,image= img_edi, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
edicaoButton.place(x = 70 , y = y_buttons)
TP.CreateToolTip(edicaoButton, text = 'Editar')

remocaoButton = Button(infosFrame,image= img_rem, bg=cor, fg=cor_contraste, width = w_button, height= h_button, command=Excluir)
remocaoButton.place(x = 120 , y = y_buttons)
TP.CreateToolTip(remocaoButton, text = 'Remover')

confirmacaoButton = Button(infosFrame,image= img_sim, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
confirmacaoButton.place(x = 270 , y = y_buttons)
TP.CreateToolTip(confirmacaoButton, text = 'Mostrar AGRs Ativos')

negacaoButton = Button(infosFrame,image= img_nao, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
negacaoButton.place(x = 320 , y = y_buttons)
TP.CreateToolTip(negacaoButton, text = 'Mostrar AGRs Inativos')

informacaoButton = Button(infosFrame,image= img_inf, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
informacaoButton.place(x = 370 , y = y_buttons)
TP.CreateToolTip(informacaoButton, text = 'Mostrar Todos Os AGRs')

saveButton = Button(infosFrame,image= img_sav, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
saveButton.place(x = 510 , y = y_buttons)
TP.CreateToolTip(saveButton, text = 'Salvar')

frame_Nome = Label(info_AGR_Sel_Frame, text= '',bg=cor_escura, fg = cor_contraste, font= fonte_Destaques)
frame_Nome.place(x=x_info,y=0)

frame_cpf = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_cpf.place(x=x_info + 190,y=y_inicio )

frame_Status = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Status.place(x=x_info,y=y_inicio )
frame_status_img = Label(info_AGR_Sel_Frame,image=None,bg=cor_escura)
frame_status_img.place(x=75 ,y=y_inicio + 5) 

frame_Posto = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Posto.place(x=x_info,y=y_inicio + y_info)

frame_Municipio = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Municipio.place(x=x_info,y=y_inicio + y_info*2)

frame_Email = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Email.place(x=x_info,y=y_inicio + y_info*3)

frame_Tel = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Tel.place(x=x_info,y=y_inicio + y_info*4)

frame_Parceiro = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Parceiro.place(x=x_info,y=y_inicio + y_info*5)

frame_data = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_data.place(x=x_info,y=y_inicio + y_info*6)

frame_Par = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Par.place(x=x_info,y=y_inicio + y_info*7)
frame_Par_img = Label(info_AGR_Sel_Frame,image=None,bg=cor_escura)
frame_Par_img.place(x=50,y=y_inicio + y_info*7 + 5)

frame_Treino = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Treino.place(x=x_info,y=y_inicio + y_info*8)
frame_Treino_img = Label(info_AGR_Sel_Frame,image=None,bg=cor_escura)
frame_Treino_img.place(x=50,y=y_inicio + y_info*8 + 5)

frame_Termo = Label(info_AGR_Sel_Frame, text='',bg=cor_escura, fg = cor_contraste, font= fonte_Textos)
frame_Termo.place(x=x_info,y=y_inicio + y_info*9)
frame_Termo_img = Label(info_AGR_Sel_Frame,image=None,bg=cor_escura)
frame_Termo_img.place(x=50,y=y_inicio + y_info*9 + 5)


#Botao de Editar AGR
#EdicaoButton = Button(infosFrame, text = "Editar AGR", bg=cor, fg=cor_contraste, width = 15)
#EdicaoButton.place(x = 170, y = 55)

