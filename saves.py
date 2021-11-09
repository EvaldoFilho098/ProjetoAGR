def __init__(self,nome,cpf,cidade,uf,posto,email,telefone,tabela_precos=None):
        self.Nome = nome
        self.CPF = cpf
        self.Cidade = cidade
        self.UF = uf
        self.Posto = posto
        self.Email = email
        self.Telefone = telefone
        self.CER = None
        self.CTPS = None
        self.Copia_CPF = None
        self.Copia_Doc = None
        self.Titulo = None
        self.Curriculo = None
        self.Escolaridade = None
        self.Decl_Endereco = None
        self.Curso = None
        self.Roteiro_Entrevista = None
        self.Parametrizacao = None
        self.Treinamento = None
        self.Status = None
        self.Parceira = None
        self.Vencimento_Cert = None
        self.Data_Curso = None
        self.Tabela_Precos = {}
        self.Termo = None
        self.Pendencias = []
        self.Aptidao = None
        if tabela_precos == None:
            self.Tabela_Precos = {
                "e-CPF A1" : "R$",
                "e-CPF A3" : "R$",
                "e-CPF A3 + Token" : "R$",
                "e-CPF A3 + Cartao": "R$",
                "e-CPF A3 + Cartao + Leitora": "R$",
                "e-CNPJ A1": "R$",
                "e-CNPJ A3": "R$",
                "e-CNPJ A3 + Token": "R$",
                "e-CNPJ A3 + Cartao": "R$",
                "e-CNPJ A3 + Cartao + Leitora": "R$",
                "OAB": "R$",
                "OAB Token": "R$",
                "Leitora De Cartao": "R$",
                "Cartao": "R$",
                "Token": "R$",
            }
        else: 
            self.Tabela_Precos = tabela_precos

