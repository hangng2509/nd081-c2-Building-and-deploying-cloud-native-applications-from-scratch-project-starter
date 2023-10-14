import azure.functions as func
from bson.json_util import dumps
import config_handler as config_handler;

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            uow = config_handler.MongoConfigHandler()
            collection_name = "advertisements"
            result = uow.get_one(collection_name, id)
           
            print("----------result--------")
            result = dumps(result)
            print(result)

            return func.HttpResponse(
                result, mimetype="application/json", charset="utf-8", status_code=200
            )
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)