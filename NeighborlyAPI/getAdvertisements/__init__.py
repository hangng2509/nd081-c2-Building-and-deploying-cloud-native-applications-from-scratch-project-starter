import azure.functions as func
import config_handler as config_handler;
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        uow = config_handler.MongoConfigHandler()
        collection = uow.get_all("advertisements")
        result = dumps(collection)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

