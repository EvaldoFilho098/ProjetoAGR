from tkinter import Tk, StringVar, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X
from tkinter import messagebox
from tkinter import ttk
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


#AMBIENTE DE EXIBICAO DE AGRS
AGRs_Frame = Frame(Janela, width = 525, height = 325, bg=cor_escura,relief="raise")
AGRs_Frame.place(x = 50,y=230)

####################################################
dadosCols = ("ID","NOME", "MUNICIPIO", "UF", "STATUS", "PARCEIRA")
listagem = ttk.Treeview(AGRs_Frame,columns = dadosCols, show='headings', height = 15, selectmode='extended')

#print(dadosCols)
#listagem.bind('<Double-1>',Mostrar)

listagem.column("ID", width = 30)
listagem.heading("ID",text="ID")

listagem.column("NOME", width = 120)
listagem.heading("NOME",text="NOME")

listagem.column("MUNICIPIO", width = 120)
listagem.heading("MUNICIPIO",text="MUNICIPIO")

listagem.column("UF", width = 30)
listagem.heading("UF",text="UF")

listagem.column("STATUS", width = 100)
listagem.heading("STATUS",text="STATUS")

listagem.column("PARCEIRA", width = 100)
listagem.heading("PARCEIRA",text="PARCEIRA")

listagem.pack(side=LEFT)

#BARRAS DE ROLAGEM DA VISUALIZACAO
ysb = ttk.Scrollbar(AGRs_Frame, orient=VERTICAL, command=listagem.yview)
listagem['yscroll'] = ysb.set
 
ysb.pack(side = RIGHT, fill = Y)

# TEXTOS DOS CABEÇALHO
for c in dadosCols:
    listagem.heading(c, text=c.title())

# INSRINDO OS ITENS
for item in Banco.Select_Columns(colunas_select):
    listagem.insert('', 'end', values=item)

#AMBIENTE DE INFORMACOES DO AGR SELECIONADO
info_AGR_Sel_Frame = Frame(Janela, width = 370, height = 325, bg=cor_escura,relief="raise")
info_AGR_Sel_Frame.place(x = 600,y=230)

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

    #POSTO
    postoLabel = Label(cadastroFrame,text = "Posto: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    postoLabel.place(x = 10,y = y_inicio + y_cad )
    postoEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    postoEntry.place(x = x_entry, y = y_inicio + y_cad)

    #CIDADE
    cidadeLabel = Label(cadastroFrame,text = "Cidade: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    cidadeLabel.place(x = 10,y = y_inicio + y_cad*2 )
    lista_cidade = ["Ponta Pora"]
    cidadeEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor)
    cidadeEntry.set_completion_list(lista_cidade)
    #ufEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    #ufEntry.place(x = x_entry, y = y_inicio + y_cad*3)
    #cidadeEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    cidadeEntry.place(x = x_entry, y = y_inicio + y_cad*2 + 2 )

    #UF
    ufLabel = Label(cadastroFrame,text = "UF: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    ufLabel.place(x = 10,y = y_inicio + y_cad*3 )
    lista_uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    ufEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor)
    ufEntry.set_completion_list(lista_uf)
    #ufEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    ufEntry.place(x = x_entry, y = y_inicio + y_cad*3 + 2)

    #E-mail
    emailLabel = Label(cadastroFrame,text = "E-mail: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    emailLabel.place(x = 10,y = y_inicio + y_cad*4 )
    emailEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    emailEntry.place(x = x_entry, y = y_inicio + y_cad*4)

    #Telefone
    telLabel = Label(cadastroFrame,text = "Telefone: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    telLabel.place(x = 10,y = y_inicio + y_cad*5 )
    telEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    telEntry.place(x = x_entry, y = y_inicio + y_cad*5)

    #Parceira
    parcLabel = Label(cadastroFrame,text = "Parceira: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    parcLabel.place(x = 10,y = y_inicio + y_cad*6 )
    lista_parc = ["Soluti","Safeweb","Soluti/Safeweb"]
    parcEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p)
    parcEntry.set_completion_list(lista_parc)
    #parcEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    parcEntry.place(x = x_entry, y = y_inicio + y_cad*6 + 2)

    #Data
    dataLabel = Label(cadastroFrame,text = "Data: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    dataLabel.place(x = 10,y = y_inicio + y_cad*7 )
    dataEntry = Entry(cadastroFrame, width = width_entry,bg=cor,foreground=cor_contraste,font=fonte_Textos)
    dataEntry.place(x = x_entry, y = y_inicio + y_cad*7)
    dataEntry.insert(0, data)

    #Status
    chkValueStatus = BooleanVar() 
    chkValueStatus.set(False)
    chkStatus = Checkbutton(cadastroFrame, text='Ativo',font = fonte_Textos, var = chkValueStatus,bg=cor, activebackground = cor, fg=cor_contraste, selectcolor= cor)
    chkStatus.place(x= 10,y = y_inicio + y_cad*8)

    #Treinamento
    chkValueTrein = BooleanVar() 
    chkValueTrein.set(False)
    chkTrein = Checkbutton(cadastroFrame, text='Treinamento',font = fonte_Textos, var = chkValueTrein,bg=cor, activebackground = cor, fg=cor_contraste, selectcolor= cor)
    chkTrein.place(x= 10,y = y_inicio + y_cad*9 + 5)

    #Parametrização
    chkValuePar = BooleanVar() 
    chkValuePar.set(False)
    chkPar = Checkbutton(cadastroFrame, text='Parametrização',var = chkValuePar,font = fonte_Textos,bg=cor, activebackground = cor, fg=cor_contraste, selectcolor= cor)
    chkPar.place(x= 10,y = y_inicio + y_cad*10 + 10)

    #Termo
    chkValueTermo = BooleanVar() 
    chkValueTermo.set(False)
    chkTermo = Checkbutton(cadastroFrame, text='Termo',var = chkValueTermo,bg=cor,font = fonte_Textos, activebackground = cor, fg=cor_contraste, selectcolor= cor)
    chkTermo.place(x= 10,y = y_inicio + y_cad*11 + 15)

    def Salvar():
        #Nome, Posto, Cidade, UF, email, telefone, parceira, data, status, treinamento, parametrizacao, termo
        txt = ""
        #NOME
        nome = nomeEntry.get()
        if nome == "":
            txt += "Nome Inválido!\n"
            nomeEntry.delete(0,END) 
        
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
        if not chkValueStatus.get() :
            Status = "Inativo"

        #Treinamento
        Trein = "Sim"
        if not chkValueTrein.get():
            Trein = "Não"
        
        #Parametrizacao
        Par = "Sim"
        if not chkValuePar.get():
            Par = "Não"
        
        #Termo
        Termo = "Sim"
        if not chkValueTermo.get():
            Termo = "Não"

        #CASO TUDO ESTEJA CORRETO
        if txt == "":
            
            #CADASTRA NO BANCO DE DADOS
            conn,cursor = Banco.conectar()

            Banco.Inserir(nome,posto,cidade,uf,tel,email,Par,Status,Termo,'',parc,Trein,data)

            #MOSTRA MENSAGEM DE SUCESSO
            messagebox.showinfo(title="SUCESSO!", message="Atendimento Cadastrado com Sucesso!")

            #LIMPA AS SELEÇÕES E TEXTOS
            nomeEntry.delete(0,END)
            postoEntry.delete(0,END)
            cidadeEntry.delete(0,END)
            ufEntry.delete(0,END)
            telEntry.delete(0,END)
            emailEntry.delete(0,END)
            parcEntry.delete(0,END)
            dataEntry.delete(0,END)

            chkValuePar.set(False)
            chkValueStatus.set(False)
            chkValueTermo.set(False)
            chkValueTrein.set(False)

            #ALTERA A QUANTIDADE DE ATENDIMENTOS
            qtd_agr = Banco.Contagem()
            qtd_ativos = len(Banco.Select_Where("STATUS","Ativo"))

            qtd['text'] = str(qtd_agr)
            qtd_Atv['text'] = str(qtd_ativos)

            qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
            qtd.place(relx=0.5, rely=0.5,anchor=CENTER)
            
            new = Banco.Select_Where("NOME",nome)[0]
            listagem.insert('', 'end', values=new)
            listagem.pack(side=LEFT)
            #ALTERA A LISTAGEM
            # INSRINDO OS ITENS
            #for item in Banco.Select_Columns(["ID","NOME", "MUNICIPIO", "UF", "STATUS", "PARCEIRA"]):
                #listagem.insert('', 'end', values=item)


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

remocaoButton = Button(infosFrame,image= img_rem, bg=cor, fg=cor_contraste, width = w_button, height= h_button)
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



Funcoes.Infos_Agrs("Evaldo","MATRIZ","Caratinga","MG","6789","evaldo@meta","Sim","Nao","Inativo","Safeweb","","SIM",data)

#Botao de Editar AGR
#EdicaoButton = Button(infosFrame, text = "Editar AGR", bg=cor, fg=cor_contraste, width = 15)
#EdicaoButton.place(x = 170, y = 55)

