BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "AGR" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"NOME"	TEXT NOT NULL,
	"POSTO"	TEXT NOT NULL,
	"MUNICIPIO"	TEXT NOT NULL,
	"UF"	TEXT NOT NULL,
	"STATUS"	TEXT NOT NULL,
	"PARCEIRA"	TEXT NOT NULL,
	"DATA"	TEXT NOT NULL,
	"PARAMET"	TEXT NOT NULL,
	"TREIN"	TEXT NOT NULL,
	"TERMO" TEXT NOT NULL,
	"TELEFONE" TEXT NOT NULL,
	"EMAIL" TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
COMMIT;

"ID","NOME","POSTO","CIDADE","UF","STATUS","PARCEIRA",
"DATA INICIO", "PARAMETRIZACAO", "TREINAMENTO","TERMO",
"TELEFONE","EMAIL"