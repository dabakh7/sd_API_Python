import sys
sys.path.append("..")
from dbconfig import mydb,mycursor
class Adresse:
    def __init__(self,street,suite,city,zipcode,geo_lat,geo_long):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo_lat = geo_lat
        self.geo_long = geo_long
    def ajouter_Adresse(self):
        tuple_add = (self.street,self.suite,self.city,self.zipcode,self.geo_lat,self.geo_long)
        insert_add = "INSERT INTO ADDRESS (street,suite,city,zipcode,geo_lat,geo_lng) VALUES (%s,%s,%s,%s,%s,%s)"
        # mycursor.execute(insert_add,tuple_add)
        # mydb.commit()
    def recuperer_Adresse():
        recupere_Add = "SELECT  addressId,street FROM ADDRESS"
        mycursor.execute(recupere_Add)
        resultats = mycursor.fetchall()
        return resultats
    



