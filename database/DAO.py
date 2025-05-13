from database.DB_connect import DBConnect
from model.prodotto import Prodotto
from model.vendite import Vendite


class DAO():
    # def __init__(self):
    #     pass

    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select gp.Product_color 
                    from go_products gp 
                    group by gp.Product_color """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getProdotti():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getProdottiColore(colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                    from go_products gp 
                    where gp.Product_color = %s"""

        cursor.execute(query, (colore,))

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getProdAnno(anno, colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select distinct gds.Product_number as pn1, gds1.Product_number as pn2, gds.`Date` as date, 
                    gds.Retailer_code as retailer
                    from go_daily_sales gds,  go_daily_sales gds1, go_products gp1, go_products gp 
                    where gds.`Date` = gds1.`Date` and 
                    YEAR(gds.`Date`) = %s and 
                    YEAR(gds1.`Date`) = YEAR(gds.`Date`) and 
                    gds.Product_number < gds1.Product_number and
                    gds.Retailer_code = gds1.Retailer_code and 
                    gds.Product_number = gp.Product_number  and gds1.Product_number = gp1.Product_number and 
                    gp.Product_color = %s and
                    gp.Product_color = gp1.Product_color"""

        cursor.execute(query, (anno, colore))

        for row in cursor:
            result.append(Vendite(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getPeso(anno, colore, u, v):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select distinct t.pn1, t.pn2, t.date, count(*)
                    from(select distinct gds.Product_number as pn1, gds1.Product_number as pn2, gds.`Date` as date, 
                    gds.Retailer_code as retailer
                    from go_daily_sales gds,  go_daily_sales gds1, go_products gp1, go_products gp 
                    where gds.`Date` = gds1.`Date` and 
                    YEAR(gds.`Date`) = %s and 
                    YEAR(gds1.`Date`) = YEAR(gds.`Date`) and 
                    gds.Product_number < gds1.Product_number and
                    gds.Retailer_code = gds1.Retailer_code and 
                    gds.Product_number = gp.Product_number  and gds1.Product_number = gp1.Product_number and 
                    gp.Product_color = %s and
                    gp.Product_color = gp1.Product_color) t
                    where t.pn1 = %s and t.pn2 = %s
                    group by t.pn1, t.pn2, t.date"""

        cursor.execute(query, (anno, colore, u, v))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()

        return result







