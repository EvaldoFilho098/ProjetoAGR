import sqlite3

def conectar():
    conn = sqlite3.connect('AGR.db')
    cursor = conn.cursor()
    return conn,cursor

# inserindo dados na tabela
def Inserir(Nome,cpf,Posto,Municipio,UF,Telefone,Email,Paramet,Status,Termo,Parceira,Treinamento,data):
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO AGR (NOME,CPF,POSTO, MUNICIPIO, UF, TELEFONE, EMAIL, PARAMET, STATUS, TERMO, PARCEIRA, TREINAMENTO, DATA)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (Nome,cpf,Posto, Municipio, UF, Telefone, Email, Paramet, Status, Termo,Parceira,Treinamento,data))
    conn.commit()
    conn.close()

#######################################################################

# lendo os dados
def Select_Where(Slc = '',Whr = ''):
    conn,cursor = conectar()

    #cursor.execute(""" 
    #SELECT '%s' FROM AGR;
    #""" % Slc)
    if Whr != '':
        comando = "SELECT * FROM AGR WHERE " + Slc + "='" + Whr + "'"
    else: 
        #cursor.execute("SELECT * FROM AGR ")
        comando = "SELECT * FROM AGR "
        
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista

def Select_Columns(lista):
    conn,cursor = conectar()
    comando = "SELECT "
    for coluna in lista:
        comando += coluna + ","
    
    comando = comando[:len(comando)-1] + " FROM AGR"
    #print(comando)

    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista
    
###################################################################


# alterando os dados da tabela
def Alterar(up, new, id):
    conn,cursor = conectar()

    comando = "UPDATE AGR SET " + up + "='" + new + "' WHERE ID=" + id
    print(comando)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

###################################################################

def Deletar(id):
    conn,cursor = conectar()
    comando = "DELETE FROM AGR WHERE ID=" + str(id)
    cursor.execute(comando)

    conn.commit()
    conn.close()

################################################################

def Contagem(Cnt='',Whr=''):
    conn,cursor = conectar()

    if Cnt == '' and Whr == '':
        comando = "SELECT COUNT(*) FROM AGR"
    else:
        comando = "SELECT COUNT(*) FROM AGR WHERE " + Cnt + "='" + Whr + "'"

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