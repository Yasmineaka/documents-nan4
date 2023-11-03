import sqlite3
from flask import Flask, render_template, request, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_clé_secrète'

# SQLite3
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# ma création de la table Utilisateur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateur (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        email TEXT UNIQUE,
        contact TEXT UNIQUE,
        mot_de_passe TEXT,
        solde REAL DEFAULT 3000
    )
''')
conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS compte_epargne (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        utilisateur_id INTEGER,
        montant_epargne REAL,
        FOREIGN KEY (utilisateur_id) REFERENCES utilisateur (id)
    )
''')
conn.commit()


login_manager = LoginManager(app)
login_manager.login_view = 'connexion'

class Utilisateur(UserMixin):
    def __init__(self, id, nom, email, contact, mot_de_passe, solde=0.0):
        self.id = id
        self.nom = nom
        self.email = email
        self.contact = contact
        self.mot_de_passe = mot_de_passe
        self.solde = solde

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    cursor.execute('SELECT * FROM utilisateur WHERE id = ?', (user_id,))
    utilisateur_data = cursor.fetchone()
    if utilisateur_data:
        return Utilisateur(*utilisateur_data)
    return None

    

@app.route('/')
def accueil():
    return render_template("index.html")

@app.route('/accueil_u')
def accueil_u():
    return render_template('accueil_u.html', nom=current_user.nom)

@app.route('/tache', methods=['POST', 'GET'])
@login_required
def tache():
    if request.method == 'POST':
        montant_epargne = float(request.form.get('montant_epargne'))
        if montant_epargne <= 0:
            flash('Le montant doit être positif.', 'danger')
        elif current_user.solde < montant_epargne:
            flash('Solde insuffisant.', 'danger')
        else:
            current_user.solde -= montant_epargne
            cursor.execute('INSERT INTO compte_epargne (utilisateur_id, montant_epargne) VALUES (?, ?)', (current_user.id, montant_epargne))
            conn.commit()
            cursor.execute('UPDATE utilisateur SET solde = ? WHERE id = ?', (current_user.solde, current_user.id))
            conn.commit()
            flash('Compte épargne créé avec succès !', 'success')
    cursor.execute('SELECT montant_epargne FROM compte_epargne WHERE utilisateur_id = ?', (current_user.id,))
    comptes_epargne = cursor.fetchall()

    return render_template('tache.html', solde=current_user.solde, comptes_epargne=comptes_epargne)


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        contact = request.form.get('contact')
        mot_de_passe = request.form.get('mot_de_passe')

        cursor.execute('SELECT * FROM utilisateur WHERE email = ? OR contact = ?', (email, contact))
        existe_utilisateur = cursor.fetchone()

        if existe_utilisateur:
            flash('Cet e-mail ou contact est déjà enregistré.', 'danger')
            return redirect('/inscription')

        mot_de_passe_hash = generate_password_hash(mot_de_passe, method='sha256')

        cursor.execute('INSERT INTO utilisateur (nom, email, contact, mot_de_passe) VALUES (?, ?, ?, ?)', (nom, email, contact, mot_de_passe_hash))
        conn.commit()

        flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
        return redirect('/connexion')

    return render_template('inscription.html')

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form.get('email')
        mot_de_passe = request.form.get('mot_de_passe')

        cursor.execute('SELECT * FROM utilisateur WHERE email = ?', (email,))
        utilisateur_data = cursor.fetchone()

        if utilisateur_data and check_password_hash(utilisateur_data[4], mot_de_passe):
            utilisateur = Utilisateur(*utilisateur_data)
            login_user(utilisateur)
            flash('Connexion réussie !', 'success')
            return redirect('/accueil_u')
        else:
            flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

    return render_template('connexion.html')


@app.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    flash('Déconnexion réussie.', 'success')
    return redirect('/')



@app.route('/apropos')
def apropos():
    return render_template('apropos.html')


if __name__ == '__main__':
    app.run(debug=True)
