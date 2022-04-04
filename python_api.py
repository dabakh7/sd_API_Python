import requests

class Utilisateur:
    def __init__(self,nom):
        self.nom = nom

    def lien_valide(self):
        liste = ["users","photos","albums","comments","todos","posts"]
        # info = input("lien :")
        if self.nom in liste:
            url = f"https://jsonplaceholder.typicode.com/{self.nom}"
            contenu = requests.get(url).json()
            return contenu

        else:
            return "donnée non valide" ####partie constructeur



# personne = Utilisateur("users")
# print(personne.lien_valide()) ###partie Vue

