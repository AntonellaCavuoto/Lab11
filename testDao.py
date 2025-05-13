from database.DAO import DAO

print(DAO.getProdottiColore("Green"))

k = (DAO.getProdAnno("2018", "White"))

for i in k:
    print(i[0][0])
