from datetime import date
import Banco

data = date.today().strftime("%d/%m/%Y")

#VARIAVEIS DE COR, TAMANHO E FONTE
largura = 1024
altura = 600

xLabels = 40
xEntrys = 165

yInicialCadastro = 50

entrysWidth = 30

cor_escura = 'grey8'
cor = "grey13" 
cor_contraste = "white"
cor_meta = "orange red"
fonte_Titulos= ("Century Gothic",32)
fonte_Textos= ("Century Gothic",12)
fonte_Mediana_2= ("Century Gothic",14)
fonte_Mediana= ("Century Gothic",18)
fonte_Destaques= ("Century Gothic",24)
titulos = "META CERTIFICADO DIGITAL "

qtd_agr = Banco.Contagem()
qtd_ativos = Banco.Contagem("STATUS","Ativo")

x_info = 10
x_plus = 6
x_img = 80
y_info = 27
y_inicio = 50

#NOME,POSTO, MUNICIPIO, UF, TELEFONE, EMAIL, PARAMET, STATUS, TERMO, OBS, PARCEIRA, TREINAMENTO, DATA

colunas_select = ["ID","NOME","POSTO","MUNICIPIO","UF","STATUS","PARCEIRA",
            "DATA", "PARAMET", "TREINAMENTO","TERMO",
            "TELEFONE","EMAIL"]