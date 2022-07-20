import mysql.connector

db = mysql.connector.connect(host="localhost", port="3306", user="root", password="Rikelme10@", database="results")
mycursor = db.cursor()
#mycursor.execute("CREATE TABLE livescore(time VARCHAR(50))") > nessa linha foi criado a tabela LIVESCORE, com o atributo TIMES

print(db)