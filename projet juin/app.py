# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# # Page d'inscription utilisateur
# @app.route('/')
# def registration_page():
#     return render_template('registration.html')

# # Page de gestion des utilisateurs pour l'administrateur
# @app.route('/admin/users')
# def admin_users_page():
#     # Ici, vous pouvez récupérer les données des utilisateurs depuis la base de données ou un autre moyen
#     # users = ...

#     # Passage des données à la page HTML
#     return render_template('gestion_u_admin', users=users)

# # Validation de l'inscription utilisateur
# @app.route('/validate_registration', methods=['POST'])
# def validate_registration():
#     # Ici, vous pouvez traiter les données envoyées par le formulaire et les enregistrer dans la base de données
#     # et générer un code QR unique pour l'utilisateur

#     return redirect('/admin/users')  # Redirige vers la page de gestion des utilisateurs

# if __name__ == '__main__':
#     app.run(debug=True)






from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         dateNaissance = request.form['dateNaissance']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         vehicule = request.form['vehicule']
#         disponibilite = request.form['disponibilite']
#         motivation = request.form['motivation']
        
#         # Stockez les données dans le fichier Jinja nommé 'mma'
#         with open('mma.jinja', 'w') as file:
#             file.write(f"Nom complet: {nom}\n")
#             file.write(f"Adresse: {adresse}\n")
#             file.write(f"Numéro de téléphone: {telephone}\n")
#             file.write(f"Adresse e-mail: {email}\n")
#             file.write(f"Date de naissance: {dateNaissance}\n")
#             file.write(f"Expérience en tant que chauffeur: {experience}\n")
#             file.write(f"Formations complémentaires: {formation}\n")
#             file.write(f"Type de véhicule utilisé: {vehicule}\n")
#             file.write(f"Disponibilité: {disponibilite}\n")
#             file.write(f"Motivation: {motivation}\n")
        
#         return 'Formulaire soumis avec succès!'
#     else:
#         return render_template('index.html')

# if __name__ == '__main__':
#     app.run()



#<-------------------------------code juste------------------------->


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         nom = request.form['nom']
#         adresse = request.form['adresse']
#         telephone = request.form['telephone']
#         email = request.form['email']
#         dateNaissance = request.form['dateNaissance']
#         experience = request.form['experience']
#         formation = request.form['formation']
#         vehicule = request.form['vehicule']
#         disponibilite = request.form['disponibilite']
#         motivation = request.form['motivation']
        
#         # Stockez les données dans le fichier Jinja nommé 'mma.jinja'
#         with open('templates/mma.jinja', 'w') as file:
#             file.write("{% extends 'base.jinja' %}\n")
#             file.write("{% block content %}\n")
#             file.write(f"<h1>Formulaire de recrutement</h1>\n")
#             file.write(f"<p>Nom complet: {nom}</p>\n")
#             file.write(f"<p>Adresse: {adresse}</p>\n")
#             file.write(f"<p>Numéro de téléphone: {telephone}</p>\n")
#             file.write(f"<p>Adresse e-mail: {email}</p>\n")
#             file.write(f"<p>Date de naissance: {dateNaissance}</p>\n")
#             file.write(f"<p>Expérience en tant que chauffeur: {experience}</p>\n")
#             file.write(f"<p>Formations complémentaires: {formation}</p>\n")
#             file.write(f"<p>Type de véhicule utilisé: {vehicule}</p>\n")
#             file.write(f"<p>Disponibilité: {disponibilite}</p>\n")
#             file.write(f"<p>Motivation: {motivation}</p>\n")
#             file.write("{% endblock %}\n")
        
#         return 'Formulaire soumis avec succès!'
#     else:
#         return render_template('index.html')


# if __name__ == '__main__':
#     app.run()










# from flask import Flask, render_template, request

# app = Flask(__name__)
# @app.route('/')
# def depot_dossier():
#     return render_template('depot_dossier.html')
# @app.route('/collect_elements', methods=['POST'])
# def collect_elements():
#     # Récupérer les données du formulaire
#     nom = request.form.get('nom')
#     adresse = request.form.get('adresse')
#     telephone = request.form.get('telephone')
#     email = request.form.get('email')
#     dateNaissance = request.form.get('dateNaissance')
#     categoriePermis=request.form.get('categoriePermis')
#     dateObtentionPermis=request.form.get('dateObtentionPermis')
#     paysEmissionPermis=request.form.get('paysEmissionPermis')
#     responsabilites=request.form.get('responsabilites')
#     motivation=request.form.get('motivation')
#     cv=request.form.get('cv')
#     photoIdentite=request.form.get('photoIdentite')
#     copiePermis=request.form.get('copiePermis')
#     # Ajouter d'autres champs du formulaire ici

#     # Afficher les éléments collectés
#     return render_template('depot_dossier.html', nom=nom, adresse=adresse, telephone=telephone, email=email, dateNaissance=dateNaissance, categoriePermis=categoriePermis, dateObtentionPermis=dateObtentionPermis, paysEmissionPermis=paysEmissionPermis,responsabilites=responsabilites, motivation= motivation, cv=cv, photoIdentite=photoIdentite,copiePermis=copiePermis)

# if __name__ == '__main__':
#     app.run()














# import sqlite3
# from flask import Flask, request

# app = Flask(__name__)

# # Route pour traiter les données du formulaire
# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     # Récupérer les données du formulaire
#     nom = request.form.get('nom')
#     adresse = request.form.get('adresse')
#     telephone = request.form.get('telephone')
#     email = request.form.get('email')
#     date_naissance = request.form.get('dateNaissance')
#     experience = request.form.get('experience')
#     formation = request.form.get('formation')
#     vehicule = request.form.get('vehicule')
#     disponibilite = request.form.get('disponibilite')
#     motivation = request.form.get('motivation')
    
#     # Connexion à la base de données SQLite
#     conn = sqlite3.connect('donnees.db')
#     cursor = conn.cursor()
    
#     # Création de la table si elle n'existe pas déjà
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS candidats (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nom TEXT,
#             adresse TEXT,
#             telephone TEXT,
#             email TEXT,
#             date_naissance TEXT,
#             experience TEXT,
#             formation TEXT,
#             vehicule TEXT,
#             disponibilite TEXT,
#             motivation TEXT
#         )
#     ''')
    
#     # Insertion des données du formulaire dans la table
#     cursor.execute('''
#         INSERT INTO candidats (
#             nom, adresse, telephone, email, date_naissance, experience,
#             formation, vehicule, disponibilite, motivation
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     ''', (nom, adresse, telephone, email, date_naissance, experience,
#           formation, vehicule, disponibilite, motivation))
    
#     # Fermeture de la connexion à la base de données
#     conn.commit()
#     conn.close()
    
#     return 'Formulaire soumis avec succès !'

# if __name__ == '__main__':
#     app.run()






# import sqlite3
# from flask import Flask, request, render_template

# app = Flask(__name__)

# # Route pour afficher le formulaire
# @app.route('/')
# def index():
#     return render_template('form1.html')

# # Route pour traiter les données du formulaire
# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     # Récupérer les données du formulaire
#     nom = request.form.get('nom')
#     adresse = request.form.get('adresse')
#     telephone = request.form.get('telephone')
#     email = request.form.get('email')
#     date_naissance = request.form.get('dateNaissance')
#     experience = request.form.get('experience')
#     formation = request.form.get('formation')
#     vehicule = request.form.get('vehicule')
#     disponibilite = request.form.get('disponibilite')
#     motivation = request.form.get('motivation')

#     # Connexion à la base de données SQLite
#     conn = sqlite3.connect('donnees.db')
#     cursor = conn.cursor()

#     # Création de la table si elle n'existe pas déjà
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS candidats (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nom TEXT,
#             adresse TEXT,
#             telephone TEXT,
#             email TEXT,
#             date_naissance TEXT,
#             experience TEXT,
#             formation TEXT,
#             vehicule TEXT,
#             disponibilite TEXT,
#             motivation TEXT
#         )
#     ''')

#     # Insertion des données du formulaire dans la table
#     cursor.execute('''
#         INSERT INTO candidats (
#             nom, adresse, telephone, email, date_naissance, experience,
#             formation, vehicule, disponibilite, motivation
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     ''', (nom, adresse, telephone, email, date_naissance, experience,
#           formation, vehicule, disponibilite, motivation))

#     # Fermeture de la connexion à la base de données
#     conn.commit()
#     conn.close()

#     return 'Formulaire soumis avec succès !'

# if __name__ == '__main__':
#     app.run()





import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Chemin du fichier de base de données SQLite
db_path = os.path.join(os.path.dirname(__file__), 'donnees.db')

# Route pour afficher le formulaire
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulaire de candidature</title>
    </head>
    <body>
        <form action="/submit_form" method="POST" enctype="multipart/form-data">
            <label for="nom">Nom complet :</label>
            <input type="text" id="nom" name="nom" required>
            
            <label for="adresse">Adresse :</label>
            <input type="text" id="adresse" name="adresse" required>
            
            <label for="telephone">Numéro de téléphone :</label>
            <input type="text" id="telephone" name="telephone" required>
            
            <label for="email">Adresse e-mail :</label>
            <input type="email" id="email" name="email" required>
            
            <label for="dateNaissance">Date de naissance :</label>
            <input type="date" id="dateNaissance" name="dateNaissance" required>
            
            <label for="experience">Expérience en tant que chauffeur :</label>
            <textarea id="experience" name="experience" required></textarea>
            
            <label for="formation">Formations complémentaires :</label>
            <textarea id="formation" name="formation" required></textarea>
            
            <label for="vehicule">Type de véhicule utilisé :</label>
            <input type="text" id="vehicule" name="vehicule" required>
            
            <label for="disponibilite">Disponibilité :</label>
            <input type="text" id="disponibilite" name="disponibilite" required>
            
            <label for="motivation">Motivation :</label>
            <textarea id="motivation" name="motivation" required></textarea>
            
            <label for="cv">CV :</label>
            <input class="recruitment-file" type="file" id="cv" name="cv" required>
            
            <label for="photoIdentite">Photo d'identité:</label>
            <input class="recruitment-file" type="file" id="photoIdentite" name="photoIdentite" required>
            
            <label for="permis">Copie du permis de conduire :</label>
            <input class="recruitment-file" type="file" id="permis" name="permis" required>
            
            <hr>
            <input type="submit" value="Envoyer">
        </form>
    </body>
    </html>
    '''

# 






import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Chemin du fichier de base de données SQLite
db_path = os.path.join(os.path.dirname(__file__), 'donnees.db')

# Route pour afficher le formulaire
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <title>Formulaire de candidature</title>
</head>
<body>
    <form action="/submit_form" method="POST" enctype="multipart/form-data">
        <label for="nom">Nom complet :</label>
        <input type="text" id="nom" name="nom" required>
        
        <label for="adresse">Adresse :</label>
        <input type="text" id="adresse" name="adresse" required>
        
        <label for="telephone">Numéro de téléphone :</label>
        <input type="text" id="telephone" name="telephone" required>
        
        <label for="email">Adresse e-mail :</label>
        <input type="email" id="email" name="email" required>
        
        <label for="dateNaissance">Date de naissance :</label>
        <input type="date" id="dateNaissance" name="dateNaissance" required>
        
        <label for="experience">Expérience en tant que chauffeur :</label>
        <textarea id="experience" name="experience" required></textarea>
        
        <label for="formation">Formations complémentaires :</label>
        <textarea id="formation" name="formation" required></textarea>
        
        <label for="vehicule">Type de véhicule utilisé :</label>
        <input type="text" id="vehicule" name="vehicule" required>
        
        <label for="disponibilite">Disponibilité :</label>
        <input type="text" id="disponibilite" name="disponibilite" required>
        
        <label for="motivation">Motivation :</label>
        <textarea id="motivation" name="motivation" required></textarea>
        
        <label for="cv">CV :</label>
        <input class="recruitment-file" type="file" id="cv" name="cv" required>
        
        <label for="photoIdentite">Photo d'identité:</label>
        <input class="recruitment-file" type="file" id="photoIdentite" name="photoIdentite" required>
        
        <label for="permis">Copie du permis de conduire :</label>
        <input class="recruitment-file" type="file" id="permis" name="permis" required>
        
        <hr>
        <input type="submit" value="Envoyer">
    </form>
</body>
</html>

    '''

# Route pour traiter les données du formulaire
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Récupérer les données du formulaire
    nom = request.form.get('nom')
    adresse = request.form.get('adresse')
    telephone = request.form.get('telephone')
    email = request.form.get('email')
    date_naissance = request.form.get('dateNaissance')
    experience = request.form.get('experience')
    formation = request.form.get('formation')
    vehicule = request.form.get('vehicule')
    disponibilite = request.form.get('disponibilite')
    motivation = request.form.get('motivation')

    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insérer les données du formulaire dans la table candidats
    cursor.execute('''
        INSERT INTO candidats (nom, adresse, telephone, email, date_naissance, experience, formation, vehicule, disponibilite, motivation)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nom, adresse, telephone, email, date_naissance, experience, formation, vehicule, disponibilite, motivation))

    # Fermeture de la connexion à la base de données
    conn.commit()
    conn.close()

    return 'Formulaire soumis avec succès !'

if __name__ == '__main__':
    # Vérifier si le fichier de base de données existe
    if not os.path.exists(db_path):
        # Créer la base de données et la table
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE candidats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                adresse TEXT,
                telephone TEXT,
                email TEXT,
                date_naissance TEXT,
                experience TEXT,
                formation TEXT,
                vehicule TEXT,
                disponibilite TEXT,
                motivation TEXT
            )
        ''')
        conn.commit()
        conn.close()

    # Lancer l'application Flask
    app.run()
