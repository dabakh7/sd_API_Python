import sys
sys.path.append("..")
from dbconfig import mydb,mycursor

class Poste:
    def __init__(self,title,body,userId):
        self.title = title
        self.body = body
        self.userId = userId
    def ajouter_Post(self):
        tuple_poste = (self.title,self.body,self.userId)
        insert_Post = "INSERT INTO POSTS (postTitle,postBody,userId) VALUES (%s,%s,%s)"
        # mycursor.execute(insert_Post,tuple_poste)
        # mydb.commit()
