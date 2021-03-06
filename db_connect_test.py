# -*- coding:utf-8 -*-
# author: Edilson Alzemand, at SIGEDO
# data base connect
# apt-get install python-mysqldb

import MySQLdb

# Conectar ao banco de dados

# SQLITE

conn = sqlite3.connect('clientes.db')

# MY SQL
con = MySQLdb.connect ( host = "localhost",
                        user = "root",
                        passwd = "*****",
                        db = "sigedo")
                        
# Ler dados do banco de dados
cursor = con.cursor ()
cursor.execute ("SELECT VERSION()")
res = cursor.fetchone ()
print "server version:", res[0]

# Gravar\alterar dados no bando de dados

cursor.execute ("INSERT INTO sigedo.aluno (al_matricula, al_nome, al_login, al_email) VALUES ('1401130027', 'Edilson Alzemand', 1401130027, 'edilson.alzemand@gmail.com')")

con.commit()

cursor.close ()
con.close ()
