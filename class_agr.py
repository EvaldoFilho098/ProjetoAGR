import Banco
from datetime import date, timedelta

class AGR:

    def __init__(self,id):
        self.id = id

        infos = Banco.Select_Where(Slc="ID",Whr = str(id),tabela="AGR")
        """
            NOME,CPF,POSTO, MUNICIPIO, UF, PARCEIRA, TELEFONE, EMAIL 
        """
        self.Nome = infos[0][1]
        self.CPF = infos[0][2]
        self.Posto = infos[0][3]
        self.Cidade = infos[0][4]
        self.UF = infos[0][5]
        self.Parceira = infos[0][6]
        self.Telefone = infos[0][7]
        self.Email = infos[0][8]
        

        docs = Banco.Select_Where(Slc="ID",Whr = str(id),tabela="DOCUMENTOS")
        """
            CER,CTPS,COPIA_CPF,COPIA_DOC,TITULO,CURRICULO,ESCOLARIDADE,DECL_END,ROTEIRO_ENT,CERT_CURSO
        """
        self.CER = docs[0][1]
        self.CTPS = docs[0][2]
        self.Copia_CPF = docs[0][3]
        self.Copia_Doc = docs[0][4]
        self.Titulo = docs[0][5]
        self.Curriculo = docs[0][6]
        self.Escolaridade = docs[0][7]
        self.Decl_Endereco = docs[0][8]
        self.Roteiro_Entrevista = docs[0][9]
        self.Cert_Curso = docs[0][10]
        

        situ = Banco.Select_Where(Slc="ID",Whr = str(id),tabela="SITUACOES")
        """
            ID,STATUS,CURSO_AGR,PARAMETR,TREINAMENTO,TERMO,TABELA_PRECOS,
            DATA_VENC_CERT,DATA_SOL_CURSO,DATA_CONCL_CURSO,DATA_INICIO,DATA_DESLIG
        """
        self.Status = situ[0][1]
        self.Curso = situ[0][2]
        self.Parametrizacao = situ[0][3]
        self.Treinamento = situ[0][4]
        self.Termo = situ[0][5]
        self.Tabela_Precos = situ[0][6]
        self.Vencimento_Cert = situ[0][7]
        self.Data_Sol_Curso = situ[0][8]
        self.Data_Con_Curso = situ[0][9]
        self.Data_Inicio = situ[0][10]
        self.Data_Deslig = situ[0][11]

        self.Pendencias = []
        self.Aptidao = "0%"
        
    
    def set(self,atributo,novo):
        if atributo.lower() == "nome": self.Nome = novo
        elif atributo.lower() == "cpf": self.CPF = novo
        elif atributo.lower() == "cidade": self.Cidade = novo
        elif atributo.lower() == "uf": self.UF = novo
        elif atributo.lower() == "posto": self.Posto = novo
        elif atributo.lower() == "emai": self.Email = novo
        elif atributo.lower() == "telefone": self.Telefone = novo
        elif atributo.lower() == "status": self.Status = novo
        elif atributo.lower() == "cer": self.CER = novo
        elif atributo.lower() == "ctps": self.CTPS = novo
        elif atributo.lower() == "copia_cpf": self.Copia_CPF = novo
        elif atributo.lower() == "copia_doc": self.Copia_Doc = novo
        elif atributo.lower() == "titulo": self.Titulo = novo
        elif atributo.lower() == "curriculo": self.Curriculo = novo
        elif atributo.lower() == "escolaridade": self.Escolaridade = novo
        elif atributo.lower() == "decl_endereco": self.Decl_Endereco = novo
        elif atributo.lower() == "roteiro_entrevista": self.Roteiro_Entrevista = novo
        elif atributo.lower() == "parceira" : self.Parceira = novo
        elif atributo.lower() == "vencimento_cert": self.Vencimento_Cert = novo
        elif atributo.lower() == "termo": self.Termo = novo

    def Solicitar_Curso(self,data):
        Banco.Alterar("SITUACOES","CURSO_AGR","ANDAMENTO",self.id)
        Banco.Alterar("SITUACOES","DATA_SOL_CURSO",data,self.id)
        self.Curso = "Andamento"
        self.Data_Curso = data

    def Concluir_Curso(self,data):
        Banco.Alterar("SITUACOES","CURSO_AGR","OK",self.id)
        Banco.Alterar("SITUACOES","DATA_CONCL_CURSO",data,self.id)
        self.Curso = "OK"
        self.Data_Fim = data
    
    def Inativo(self):
        Banco.Alterar("SITUACOES","STATUS","INATIVO",self.id)
        self.Status = "Inativo"
    
    def Ativo(self):
        Banco.Alterar("SITUACOES","STATUS","ATIVO",self.id)
        self.Status = "Ativo"
    
    def Pendente(self):
        Banco.Alterar("SITUACOES","STATUS","PENDENTE",self.id)
        self.Status = "Pendente"
    
    def Parametrizar(self):
        Banco.Alterar("SITUACOES","PARAMETR","OK",self.id)
        self.Parametrizacao = "OK"
    
    def Treino(self):
        Banco.Alterar("SITUACOES","TREINAMENTO","OK",self.id)
        self.Treinamento = "OK"
    
    def Expirar(self):
        '''
        quantos dias faltam para o certificado vencer
        '''
        hoje = date.today().strftime("%d/%m/%Y")
        hoje = hoje.split('/')

        venc = self.Vencimento_Cert.split("/")

        data1 = date(day=int(hoje[0]), month=int(hoje[1]), year=int(hoje[2]))
        data2 = date(day=int(venc[0]), month=int(venc[1]), year=int(venc[2]))

        dias =  data2 - data1
        return dias.days
    
    def Tempo_Curso(self):
        '''
        Quantos dias faltam para expirar o curso e que dia ele ira expirar
        '''
        hoje = date.today().strftime("%d/%m/%Y")
        hoje = hoje.split('/')
        hj = date(day=int(hoje[0]), month=int(hoje[1]), year=int(hoje[2]))

        sol = self.Data_Sol_Curso.split('/')
        data_sol = date(day=int(sol[0]), month=int(sol[1]), year=int(sol[2]))

        data_exp = data_sol + timedelta(days=15)

        restante = data_exp - hj
        data_exp = data_exp.strftime("%d/%m/%Y")

        return data_exp,restante.days
    
    def Valor_Tabela_Precos(self,nome,preco):
        if "R$" in str(preco):
            self.Tabela_Precos[nome] = str(preco)
        else:
            self.Tabela_Precos[nome] = "R$" + str(preco)
    
    def Infos(self):
        return self.Nome,self.CPF,self.Cidade,self.UF,self.Posto,self.Email,self.Telefone
    
    def Docs(self):
        return self.CER,self.CTPS,self.Copia_CPF,self.Copia_Doc,self.Titulo,self.Curriculo,self.Escolaridade,self.Decl_Endereco,self.Roteiro_Entrevista,self.Cert_Curso
    
    def Situacoes(self):
        return self.Status,self.Curso,self.Parametrizacao,self.Treinamento,self.Termo,self.Tabela_Precos,self.Vencimento_Cert,self.Data_Sol_Curso,self.Data_Con_Curso,self.Data_Inicio, self.Data_Deslig,self.Pendencias,self.Aptidao
    
    def Situacao(self,x):
        if self.Status == True:
            return "Ativo"
        elif self.Status == False:
            return "Inativo"
        elif self.Status == None:
            return "Pendente"
    
    def Atualiza_Situacao(self):
        situacao = 0
        
        if self.CER == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Arquivo .CER")

        if self.CTPS == "OK":
            situacao += 1
        else:
            self.Pendencias.append("CTPS")

        if self.Copia_CPF == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Copia do CPF")

        if self.Copia_Doc == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Copia de Documento com Foto")

        if self.Curriculo == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Curriculo")

        if self.Escolaridade == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Escolaridade")

        if self.Decl_Endereco == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Declaracao de Endereco")

        if self.Cert_Curso == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Certificado de Conclusao Do Curso")

        if self.Curso == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Curso de AGR")

        if self.Roteiro_Entrevista == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Roteiro Entrevista")

        if self.Parametrizacao == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Parametrizacao")

        if self.Treinamento == "OK":
            situacao += 1
        else:
            self.Pendencias.append("Treinamento")
        
        y = int((100*situacao)/12)
        self.Aptidao = str(y) + "%"

        if situacao == 12:
            self.Ativo()
        else:
            self.Pendente()
    
    def Atualiza(self):
        
        self.Atualiza_Situacao()
        self.Tempo_Curso()
        self.Expirar()

"""x = AGR(14)
x.Atualiza_Situacao()
print(x.Pendencias)
print(x.Aptidao)
print(x.Status)
print(x.Expirar())
print(x.Tempo_Curso())
"""


#hoje = date.today().strftime("%d/%m/%Y")
#hoje = hoje.split('/')

#venc = "16/12/2021"
#venc = venc.split("/")

#data1 = date(day=int(hoje[0]), month=int(hoje[1]), year=int(hoje[2]))
#data2 = date(day=int(venc[0]), month=int(venc[1]), year=int(venc[2]))

#dias =  data2 + timedelta(days=2)

#print(dias.strftime("%d/%m/%Y"))