import sys
sys.path.append("..")
from controleur import Utilisateur
from models.addressmodel import Adresse
from models.usermodel import Users
from models.companymodel import Company
api_users = Utilisateur("users")
donnee_users = api_users.lien_valide()
tab_Addresse = Adresse.recuperer_Adresse()
tab_Users = Users.recuperer_IdUsers()
for user in donnee_users:            ###ces deux lignes nous permet de correspondre chaque utilisateur
    addresse = user.get('address')   ###avec son id_adresse
    company = user.get('company')
    contenu = (adresses['street'],adresses['suite'],adresses['city'],adresses['zipcode'],adresses['geo']['lat'],adresses['geo']['lng'])
    pers = Adresse(adresses['street'],adresses['suite'],adresses['city'],adresses['zipcode'],adresses['geo']['lat'],adresses['geo']['lng'])
    pers.ajouter_Adresse()
    for addr in tab_Addresse:
        if addr[1] == addresse['street']:
            user_adresse_id = addr[0]
        
    utilisateur = Users(user['name'],user['username'],user['email'],user['phone'],user['website'],user_adresse_id)
    utilisateur.ajouter_Users()
    for post in tab_Users:
        if post[1] == user.get('name'):
            id_user = post[0]
    compagny = Company(company['name'],company['catchPhrase'],company['bs'],id_user)
    compagny.ajouter_Company()


        
    