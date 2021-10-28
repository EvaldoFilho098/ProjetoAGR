import sqlite3

def conectar():
    conn = sqlite3.connect('AGR.db')
    cursor = conn.cursor()
    return conn,cursor

# inserindo dados na tabela
def Inserir(Nome,Municipio,UF,Telefone,Email,Paramet,Status,Termo,OBS,Parceira):
    conn,cursor = conectar()
    cursor.execute("""
        INSERT INTO AGR (NOME, MUNICIPIO, UF, TELEFONE, EMAIL, PARAMET, STATUS, TERMO, OBS, PARCEIRA)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (Nome, Municipio, UF, Telefone, Email, Paramet, Status, Termo, OBS, Parceira))
    conn.commit()
    conn.close()
####################################
'''
# criando uma lista de dados
lista = [(
    'Fabio', 23, '44444444444', 'fabio@email.com', '1234-5678', 'Belo Horizonte', 'MG', '2014-06-09'),
    ('Joao', 21, '55555555555', 'joao@email.com',
     '11-1234-5600', 'Sao Paulo', 'SP', '2014-06-09'),
    ('Xavier', 24, '66666666666', 'xavier@email.com', '12-1234-5601', 'Campinas', 'SP', '2014-06-10')]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)
'''
##################################
'''
# solicitando os dados ao usuário
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('Email: ')
p_fone = input('Fone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em (yyyy-mm-dd): ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))
'''
#######################################################################
#Slc = "Ativo"
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
###################################################################

'''
id_cliente = 1
novo_fone = '11-1000-2014'
novo_criado_em = '2014-06-11'

'''

# alterando os dados da tabela
def Alterar(up, new, id):
    conn,cursor = conectar()

    comando = "UPDATE AGR SET " + up + "='" + new + "' WHERE ID=" + id
    print(comando)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

###################################################################
'''
id_cliente = 8

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))


# gravando no bd
conn.commit()
'''
def Deletar(id):
    conn,cursor = conectar()
    comando = "DELETE FROM AGR WHERE ID=" + id
    cursor.execute(comando)

    conn.commit()
    conn.close()
#lista = Select_Where()
#print(lista)

#Alterar('STATUS','Inativo','2')

#Inserir("Luiz","Ponta Pora","MS","33212304","luiz@meta","Sim","Ativo","Nao","","Soluti")

#Deletar('3')

#lista = Select_Where("STATUS","Inativo")
#for i in lista:
#    print(i)

#lista = Select_Where("UF","MS")
#print(lista)

