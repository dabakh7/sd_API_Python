from controleur import Utilisateur

api_users = Utilisateur("users")
# print(api_users.lien_valide()) ###partie Vue

# api_photo = Utilisateur("photos")
# print(api_photo.lien_valide())
# api_album = Utilisateur("albums")
# api_comments = Utilisateur("comments")
# api_todos = Utilisateur("todos")
api_posts = Utilisateur("posts")
donnees_Posts = api_posts.lien_valide()





