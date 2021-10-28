BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "AGR" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"NOME"	TEXT NOT NULL,
	"MUNICIPIO"	TEXT NOT NULL,
	"UF"	TEXT NOT NULL,
	"TELEFONE"	TEXT NOT NULL,
	"EMAIL"	TEXT NOT NULL,
	"PARAMET"	TEXT NOT NULL,
	"STATUS"	TEXT NOT NULL,
	"TERMO"	TEXT NOT NULL,
	"OBS"	TEXT,
	"TREINAMENTO" TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
COMMIT;
