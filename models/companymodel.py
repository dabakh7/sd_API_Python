import sys
sys.path.append("..")
from dbconfig import mydb,mycursor

class Company:
    def __init__(self,name,catchPhrase,bs,userId):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs
        self.userId = userId
    def ajouter_Company(self):
        tuple_company = (self.name,self.catchPhrase,self.bs,self.userId)
        insert_company = "INSERT INTO COMPANY (companyName,companyCatchPhrase,companyBs,userId) VALUES (%s,%s,%s,%s)"
        # itmycursor.execute(insert_company,tuple_company)
        # mydb.comm()
        # print(tuple_company)


