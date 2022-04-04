import sys
sys.path.append("..")
from dbconfig import mydb,mycursor
class Users:
    def __init__(self,name,userName,userEmail,userPhone,userWebsite,addressId):
        self.name = name
        self.userName = userName
        self.userEmail = userEmail
        self.userPhone = userPhone
        self.userWebsite =  userWebsite
        self.addressId = addressId
    def ajouter_Users(self):
        tuple_users = (self.name,self.userName,self.userEmail,self.userPhone,self.userWebsite,self.addressId)
        insert_users = "INSERT INTO USERS (name,userName,userEmail,userPhone,userWebsite,addressId) VALUES (%s,%s,%s,%s,%s,%s)"
        # mycursor.execute(insert_users,tuple_users)
        # mydb.commit()
    def recuperer_IdUsers():
        recup_Iduser="SELECT userId,name FROM USERS"
        mycursor.execute(recup_Iduser)
        resultats_user = mycursor.fetchall()
        return resultats_user