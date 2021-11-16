import sqlite3

def conectar():
    conn = sqlite3.connect('AGR.db')
    cursor = conn.cursor()
    return conn,cursor

# inserindo dados na tabela
def Inserir(Nome,cpf,Posto,Municipio,UF,Telefone,Email,Parceira):
    """
    NOME,CPF,POSTO, MUNICIPIO, UF, TELEFONE, EMAIL, PARCEIRA
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO AGR (NOME,CPF,POSTO, MUNICIPIO, UF, TELEFONE, EMAIL, PARCEIRA)
        VALUES (?,?,?,?,?,?,?,?)
    """, (Nome,cpf,Posto, Municipio, UF, Telefone, Email,Parceira))
    id = cursor.lastrowid
    conn.commit()
    conn.close()

    return id

def Inserir_Docs(id,cer,ctps,copia_cpf,copia_doc,titulo,curriculo,escolaridade,decl_end,roteiro_ent,cert_curso):
    """
    CER,CTPS,COPIA_CPF,COPIA_DOC,TITULO,CURRICULO,ESCOLARIDADE,DECL_END,ROTEIRO_ENT,CERT_CURSO
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO DOCUMENTOS (ID,CER,CTPS,COPIA_CPF,COPIA_DOC,TITULO,CURRICULO,ESCOLARIDADE,DECL_END,ROTEIRO_ENT,CERT_CURSO)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (id,cer,ctps,copia_cpf,copia_doc,titulo,curriculo,escolaridade,decl_end,roteiro_ent,cert_curso))
    conn.commit()
    conn.close()

def Inserir_Situ(id,status,curso_agr,paramet,treinamento,termo,tabela_precos,
    data_venc_cer,data_sol_curso,data_concl_curso,data_inicio,data_desl):
    """
    ID,STATUS,CURSO_AGR,PARAMETR,TREINAMENTO,TERMO,TABELA_PRECOS,
    DATA_VENC_CERT,DATA_SOL_CURSO,DATA_CONCL_CURSO,DATA_INICIO,DATA_DESLIG
    """
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO SITUACOES (ID,STATUS,CURSO_AGR,PARAMETR,TREINAMENTO,TERMO,TABELA_PRECOS,
        DATA_VENC_CERT,DATA_SOL_CURSO,DATA_CONCL_CURSO,DATA_INICIO,DATA_DESLIG)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, (id,status,curso_agr,paramet,treinamento,termo,tabela_precos,
    data_venc_cer,data_sol_curso,data_concl_curso,data_inicio,data_desl))
    conn.commit()
    conn.close()

#######################################################################

# lendo os dados
def Select_Where(item = '*',Slc = '',Whr = '',tabela='AGR'):
    conn,cursor = conectar()

    #cursor.execute(""" 
    #SELECT '%s' FROM AGR;
    #""" % Slc)
    if str(Whr) != '':
        comando = "SELECT " + item + " FROM " + tabela + " WHERE " + Slc + "='" + str(Whr) + "'"
    else: 
        #cursor.execute("SELECT * FROM AGR ")
        comando = "SELECT * FROM " + tabela
        
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista

def Select_Columns(lista,tabela='AGR'):
    conn,cursor = conectar()
    comando = "SELECT "
    for coluna in lista:
        comando += coluna + ","
    
    comando = comando[:len(comando)-1] + " FROM " + tabela
    #print(comando)

    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista
    
###################################################################
def Select_Distinct(nome,tabela='AGR'):
    conn,cursor = conectar()
    comando = "SELECT DISTINCT " + nome + " FROM " + tabela
    
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha[0])

    conn.close()
    return lista

# alterando os dados da tabela
def Alterar(tabela,up, new, id):
    conn,cursor = conectar()

    comando = "UPDATE " + tabela + " SET " + up + "='" + new + "' WHERE ID=" + str(id)
    #print(comando)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

###################################################################

def Deletar(id):
    conn,cursor = conectar()
    comando = "DELETE FROM AGR WHERE ID=" + str(id)
    cursor.execute(comando)
    comando = "DELETE FROM DOCUMENTOS WHERE ID=" + str(id)
    cursor.execute(comando)
    comando = "DELETE FROM SITUACOES WHERE ID=" + str(id)
    cursor.execute(comando)

    conn.commit()
    conn.close()

################################################################

def Contagem(Cnt='',Whr='',tabela='AGR'):
    conn,cursor = conectar()

    if Cnt == '' and Whr == '':
        comando = "SELECT COUNT(*) FROM " + tabela
    else:
        comando = "SELECT COUNT(*) FROM " + tabela + " WHERE " + Cnt + "='" + Whr + "'"

    cursor.execute(comando)

    x = int(cursor.fetchall()[0][0])

    conn.close()

    return x

def Ultima_ID():
    conn,cursor = conectar()
    comando = "SELECT * FROM AGR WHERE ID=(SELECT max(ID) FROM AGR)"
    cursor.execute(comando)
    x = str(cursor.fetchall()[0][0])
    conn.close()

    return x
    
###########################  TESTES  ##############################

#Alterar('STATUS','Inativo','2')

#Inserir("Luiz","Ponta Pora","MS","33212304","luiz@meta","Sim","Ativo","Nao","","Soluti")

#Deletar('3')

#lista = Select_Where()
#print(lista)

#lista = Select_Where("STATUS","Inativo")
#for i in lista:
#    print(i)

#lista = Select_Where("UF","MS")
#print(lista)

#print(Contagem())
#print(Contagem("STATUS","Inativo"))

#lista = Select_Columns(["ID","NOME"])
#print(lista)