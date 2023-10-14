import azure.functions as func
import config_handler as config_handler;


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            uow = config_handler.MongoConfigHandler()
            collection_name = "advertisements"
            result = uow.delete_by_id(collection_name, id)
            return func.HttpResponse("Advertisement deleted successfully.")
        
        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
