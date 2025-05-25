import sqlite3

# créer une connexion à la base de donnée pw_manager
con = sqlite3.connect("pw_manager.db")

# traiter les datas ligne/ligne et récupérer les resultats
cur = con.cursor()

# table de DB
cur.execute("""
            CREATE TABLE IF NOT EXISTS pw_stock (
            website,
             id,
             password)""")

con.commit()

# sauvagarde dans le tab
cur.execute("""
    INSERT INTO pw_stock VALUES
        ("kurosaki.com", "kurosaki", "bankai123"),
        ("esap.fr", "esap", "esapeuh123")
""")

con.commit()

# vérif
cur.execute("SELECT * FROM pw_stock")
print(cur.fetchall())

con.commit()

con.close()