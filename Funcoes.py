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

def Infos_Agrs(nome,cpf,posto, municipio, uf, tel, email, status, parceira, ):
    
    '''
    if par.upper() == "SIM":
        img_par = Janela.img_sim_men
    else:
        img_par = Janela.img_nao_men

    if termo.upper() == "SIM":
        img_termo = Janela.img_sim_men
    else:
        img_termo = Janela.img_nao_men  
    '''

    if status.upper() == "ATIVO":
        img_status = Janela.img_sim_men
    else:
        img_status = Janela.img_nao_men  
    
    '''
    if treinamento.upper() == "SIM":
        img_treino = Janela.img_sim_men
    else:
        img_treino = Janela.img_nao_men 
    '''

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

    if ": INATIVO" in status: 
        Janela.frame_status_img.place(x=145 ,y=y_inicio + 5)
    elif ": ATIVO" in status:
        Janela.frame_status_img.place(x=130 ,y=y_inicio + 5)

    Janela.frame_Posto.configure(text= "Posto: " + posto)

    Janela.frame_Municipio.configure(text="Cidade: "+ municipio + " - " + uf)

    #Janela.frame_Email.configure(text="E-mail: " + email)

    Janela.frame_Tel.configure(text="Telefone: " + tel)

    Janela.frame_Parceiro.configure(text="Parceira: "+ parceira)

    #Janela.frame_data.configure(text="Data de Inicio: " + data)

    '''
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
    '''


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
    jan.attributes("-alpha",0.99)

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
    cadastroFrame = Frame(jan, width = 360, height = 530, bg=cor_escura,relief="raise")
    cadastroFrame.place(x = 20,y=50)
    cadastroLabel = Label(jan,text = "DADOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
    cadastroLabel.place(x = 20, y = 15)

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
    lista_parc = ["Soluti","Meta","Soluti/Meta"]
    parcEntry = AutocompleteCombobox(cadastroFrame, width = width_entry_p)
    parcEntry.set_completion_list(lista_parc)
    parcEntry.place(x = x_entry, y = y_inicio + y_cad*7 + 2)

    '''
    #Termo
    TermoLabel = Label(cadastroFrame,text = "Termo ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    TermoLabel.place(x= 10,y = y_inicio + y_cad*8 )
    chkTermo = ttk.Checkbutton(cadastroFrame,style="TCheckbutton")
    chkTermo.state(['!alternate'])
    chkTermo.place(x= x_entry,y = y_inicio + y_cad*8 + 3)

    ####################################################################################
    
    #AMBIENTE DE DOCUMENTOS
    docsFrame = Frame(jan, width = 360, height = 530, bg=cor_escura,relief="raise")
    docsFrame.place(x = 420,y=50)
    docsLabel = Label(jan,text = "DOCUMENTOS",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
    docsLabel.place(x = 420, y = 15)

    #.CER
    CERLabel = Label(docsFrame,text = "Arquivo .CER ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CERLabel.place(x=x_label_check,y = y_inicio )
    chkCER = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCER.state(['!alternate'])
    chkCER.place(x=x_check ,y = y_inicio + 3)

    #CTPS
    CTPSLabel = Label(docsFrame,text = "CTPS ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CTPSLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
    chkCTPS = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCTPS.state(['!alternate'])
    chkCTPS.place(x=x_check ,y = y_inicio + y_cad2)

    #Copia CPF
    CCPFLabel = Label(docsFrame,text = "Cópia do CPF ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CCPFLabel.place(x=x_label_check,y = y_inicio + y_cad2*2 )
    chkCCPF = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCCPF.state(['!alternate'])
    chkCCPF.place(x=x_check ,y = y_inicio + y_cad2*2 + 3)

    #Copia docs
    CDocLabel = Label(docsFrame,text = "Cópia de Documento Com Foto ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CDocLabel.place(x=x_label_check,y = y_inicio + y_cad2*3 )
    chkCDoc = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCDoc.state(['!alternate'])
    chkCDoc.place(x=x_check ,y = y_inicio + y_cad2*3 + 3)

    #Titulo
    TituloLabel = Label(docsFrame,text = "Copia do Título de Eleitor ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    TituloLabel.place(x=x_label_check,y = y_inicio + y_cad2*4 )
    chkTitulo = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkTitulo.state(['!alternate'])
    chkTitulo.place(x=x_check ,y = y_inicio + y_cad2*4 + 3)

    #Curriculo
    CurrLabel = Label(docsFrame,text = "Curriculo  ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CurrLabel.place(x=x_label_check,y = y_inicio + y_cad2*5 )
    chkCurr = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCurr.state(['!alternate'])
    chkCurr.place(x=x_check ,y = y_inicio + y_cad2*5 + 3)

    #escolar
    escolarLabel = Label(docsFrame,text = "Escolaridade ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    escolarLabel.place(x=x_label_check,y = y_inicio + y_cad2*6 )
    chkescolar = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkescolar.state(['!alternate'])
    chkescolar.place(x=x_check ,y = y_inicio + y_cad2*6 + 3)

    #declaracao de endereco
    DEndLabel = Label(docsFrame,text = "Declaração de Endereço ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    DEndLabel.place(x=x_label_check,y = y_inicio + y_cad2*7 )
    chkDEnd = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkDEnd.state(['!alternate'])
    chkDEnd.place(x=x_check ,y = y_inicio + y_cad2*7 + 3)

    #roteiro entrevista
    REntrLabel = Label(docsFrame,text = "Roteiro Entrevista ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    REntrLabel.place(x=x_label_check,y = y_inicio + y_cad2*8 )
    chkREntr = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkREntr.state(['!alternate'])
    chkREntr.place(x=x_check ,y = y_inicio + y_cad2*8 + 3)

    #Certificado do Curso de Agr
    CursoLabel = Label(docsFrame,text = "Certificado do Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CursoLabel.place(x=x_label_check,y = y_inicio + y_cad2*9 )
    chkCurso = ttk.Checkbutton(docsFrame,style="TCheckbutton")
    chkCurso.state(['!alternate'])
    chkCurso.place(x=x_check ,y = y_inicio + y_cad2*9 + 3)

    ######################################################################

    #AMBIENTE DE PROGRESSO
    progFrame = Frame(jan, width = 360, height = 530, bg=cor_escura,relief="raise")
    progFrame.place(x = 820,y=50)
    progLabel = Label(jan,text = "PROGRESSO",font=fonte_Mediana, anchor="w", fg=cor_contraste, bg=cor_escura)
    progLabel.place(x = 820, y = 15)

    #Curso de Agr
    CursoLabel = Label(progFrame,text = "Curso de AGR ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    CursoLabel.place(x=10,y = y_inicio )
    lista_situacoes = ['Concluído','Em Andamento','Não Solicitado']
    CursoEntry = AutocompleteCombobox(progFrame, width = 30,background=cor)
    CursoEntry.set_completion_list(lista_situacoes)
    CursoEntry.place(x=140 ,y = y_inicio+ 3)

    #Parametrizacao
    ParametLabel = Label(progFrame,text = "Parametrização ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    ParametLabel.place(x=x_label_check,y = y_inicio + y_cad2 )
    chkParamet = ttk.Checkbutton(progFrame,style="TCheckbutton")
    chkParamet.state(['!alternate'])
    chkParamet.place(x=x_check ,y = y_inicio + y_cad2 + 3)
    
    #Treinamento
    TreinLabel = Label(progFrame,text = "Treinamento ",font=fonte_Textos, anchor="w", fg=cor_contraste, bg=cor)
    TreinLabel.place(x=x_label_check + 200,y = y_inicio + y_cad2 )
    chkTrein = ttk.Checkbutton(progFrame,style="TCheckbutton")
    chkTrein.state(['!alternate'])
    chkTrein.place(x=x_check+200,y = y_inicio + y_cad2 + 3)


    style = ttk.Style()
    style.configure("TCheckbutton", foreground="white", background="black",font=('Helvetica', 22))
    '''

    '''
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
    '''
    


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
        
        '''
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
            nomeEntry.delete(0,END)
            cpfEntry.delete(0,END)
            postoEntry.delete(0,END)
            cidadeEntry.delete(0,END)
            ufEntry.delete(0,END)
            telEntry.delete(0,END)
            emailEntry.delete(0,END)
            parcEntry.delete(0,END)
            #dataEntry.delete(0,END)

            #chkStatus.state(['!alternate'])
            #chkPar.state(['!alternate'])
            #chkTermo.state(['!alternate'])
            #chkTrein.state(['!alternate'])

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


    #BOTAO DE Salvar
    #Cadastrar funçaõ salvar
    cadastroButton = Button(jan, text = "Salvar", bg=cor, fg=cor_contraste, width = 40, command=Salvar)
    cadastroButton.place(x = 50, y = 600 )

    jan.mainloop()