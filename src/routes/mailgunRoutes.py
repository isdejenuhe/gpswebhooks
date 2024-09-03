import azure.functions as func
import json
from src.db.connectDBMongo import connectDB
from datetime import datetime
mailgunRoutes = func.Blueprint()

@mailgunRoutes.route(route="mailgunRoutes/getRespuesta", methods=[func.HttpMethod.POST])
def getRespuesta(req: func.HttpRequest) -> func.HttpResponse:
    # Establecer la conexión
    try:
        content = req.get_body()
        content2 = json.loads(content)
        s_correo = content2["event-data"]["recipient"]
        
        sistema = ""
        proceso = ""
        rfc     = ""

        if len(content2["event-data"]["tags"]) > 0:
            sistema = content2["event-data"]["tags"][0]
        if len(content2["event-data"]["tags"]) > 1:
            proceso = content2["event-data"]["tags"][1]
        if len(content2["event-data"]["tags"]) > 2:
            rfc     = content2["event-data"]["tags"][2]

        my_conection = connectDB("") #connectamos a la bd principal
        notificaciones = my_conection["listaNegraCorreosElectronicos"] #connectamos a la bd principal
        notificaciones.insert_one({
            'correoElectronico': s_correo,
            'sistema': str(sistema),
            'proceso': str(proceso),
            'rfc': str(rfc),
            'creadoEl': datetime.utcnow()
        })
        return func.HttpResponse(json.dumps({"ok": True}), mimetype="application/json")
    except Exception as error:
        return func.HttpResponse(
            json.dumps({"error": f"{error}"}),
            status_code=200,
            mimetype="application/json")
