from tkinter import Tk, StringVar, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X
from tkinter import messagebox
from tkinter import ttk
import img
from var import *
from PIL import Image,ImageTk
import ToolTip as TP
from Classes import AutocompleteCombobox
import Banco
import Funcoes


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
        print(lista_parc)
        print(parc)
        print(parc in lista_parc)
        if parc == "" or parc not in lista_parc:
            txt = txt + "Parceira Inválida!\n"
        
        #DATA
        data = dataEntry.get()
        if data == "":
            txt = txt + "Data Inválida!\n"
        
        #Status
        Status = "Ativo"
        if not chkValueStatus.get():
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

            """
            
            #ALTERA A QUANTIDADE DE ATENDIMENTOS
            qtd_atendimentos = Banco.Contagem() 
            qtd['text'] = qtd_atendimentos
            qtd.place(relx=0.5, rely=0.5,anchor=CENTER)

            qtd_h = banco.dados.loc[banco.dados["Data"] == data].count()
            qtd_hj['text'] = qtd_h[0]
            qtd_hj.place(relx=0.5, rely=0.5,anchor=CENTER)
            """

            #ALTERA A LISTAGEM
            # INSRINDO OS ITENS
            for item in Banco.Select_Columns(["ID","NOME", "MUNICIPIO", "UF", "STATUS", "PARCEIRA"]):
                listagem.insert('', 'end', values=item)


            jan.destroy()
        else:
            #CASO DE ERRADO
            Funcoes.Mensagem_Aviso(txt)


    #BOTAO DE INSERIR
    #Cadastrar funçaõ inserir
    cadastroButton = Button(jan, text = "Salvar", bg=cor, fg=cor_contraste, width = 30, command=Salvar)
    cadastroButton.place(x = 90, y = 600 )

    jan.mainloop()
