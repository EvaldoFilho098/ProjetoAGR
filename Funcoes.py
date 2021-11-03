import Janela
from tkinter import Tk, StringVar, Frame,Entry,Label,Button,Menu,BooleanVar,Checkbutton,PhotoImage,END,RIGHT,LEFT,TOP,BOTTOM,CENTER,VERTICAL,Y,HORIZONTAL,X
from tkinter import messagebox
from tkinter import ttk
from var import *
from Classes import AutocompleteCombobox
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
    postoEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor,height=15)
    postoEntry.set_completion_list(lista_posto)
    postoEntry.place(x = x_entry, y = y_inicio + y_cad * 2)

    #CIDADE
    cidadeLabel = Label(cadastroFrame,text = "Cidade: ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    cidadeLabel.place(x = 10,y = y_inicio + y_cad*3 )
    #lista_cidade = ["Ponta Pora","Campo Grande","Dourados"]
    cidadeEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p,background=cor,height=15)
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

            Janela.qtd['text'] = str(qtd_agr)
            Janela.qtd_Atv['text'] = str(qtd_ativos)

            Janela.qtd_Atv.place(relx=0.5, rely=0.5,anchor=CENTER)
            Janela.qtd.place(relx=0.5, rely=0.5,anchor=CENTER)
            
            uID = Banco.Ultima_ID()
            new = Banco.Select_Where("ID",uID)[0]
            Janela.listagem.insert('', 'end', values=new)
            Janela.listagem.place(x = 0, y = 0, width = 525, height = 305)

            jan.destroy()
        else:
            #CASO DE ERRADO
            Mensagem_Aviso(txt)


    #BOTAO DE INSERIR
    #Cadastrar funçaõ inserir
    cadastroButton = Button(jan, text = "Salvar", bg=cor, fg=cor_contraste, width = 30, command=Salvar)
    cadastroButton.place(x = 90, y = 600 )

    jan.mainloop()