import sys
sys.path.append("..")
from controleur import Utilisateur
from models.usermodel import Users
from usercontroleurs import user
from models.postsmodel import Poste

api_users = Utilisateur("users")
donnee_users = api_users.lien_valide()
api_posts = Utilisateur("posts")
donnees_Posts = api_posts.lien_valide()
tab_Post = Users.recuperer_IdUsers()
for publier in donnees_Posts:
    for poster in tab_Post:
        if poster[1] == user.get('name'):
            id_userPost = poster[0]
    contenu = Poste(publier['title'],publier['body'],id_userPost)
    contenu.ajouter_Post()
    
            
        

    