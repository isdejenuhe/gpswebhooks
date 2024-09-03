import os
import pymongo
def connectDB(s_apuntar_cliente):
    try:
        mong_conect = pymongo.MongoClient(os.getenv("mongoConn"))
        mydb = mong_conect[f"""gmtgps{s_apuntar_cliente.replace("-", "")}"""]
        return mydb
    except Exception as ex:
        # En este punto, connection no ha sido definido
        raise ex  # Re-lanzar la excepción para que el llamador la maneje
