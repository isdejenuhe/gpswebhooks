import azure.functions as func
import json
import logging
mailgunRoutes = func.Blueprint()


@mailgunRoutes.route(route="mailgunRoutes/getRespuesta", methods=[func.HttpMethod.POST])
def getRespuesta(req: func.HttpRequest) -> func.HttpResponse:
    # Establecer la conexión
    try:
        content = req.get_body()
        logging.info('%s', content)
        content2 = json.loads(content)
        logging.info('%s',content2)
        s_resultado = {
            "gracias":"muchas gracias"
        }
        print(content)
        return func.HttpResponse(json.dumps(s_resultado), mimetype="application/json")
    except Exception as error:
        return func.HttpResponse(
            json.dumps({"error": f"{error}"}),
            status_code=200,
            mimetype="application/json")
