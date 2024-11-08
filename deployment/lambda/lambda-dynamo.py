import json
import boto3

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('http-crud-tutorial-items')

def lambda_handler(event, context):
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        if event['routeKey'] == "DELETE /items/{id}":
            # Suppression de l'élément
            table.delete_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = f"Deleted item {event['pathParameters']['id']}"
        
        elif event['routeKey'] == "GET /items/{id}":
            # Récupération d'un élément par ID
            response = table.get_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = response.get('Item', {})
        
        elif event['routeKey'] == "GET /items":
            # Récupération de tous les éléments
            response = table.scan()
            body = response.get('Items', [])
        
        elif event['routeKey'] == "PUT /items":
            # Mise à jour ou ajout d'un élément
            request_json = json.loads(event['body'])
            table.put_item(
                Item={
                    'id': request_json['id'],
                    'price': request_json['price'],
                    'name': request_json['name']
                }
            )
            body = f"Put item {request_json['id']}"
        
        else:
            raise Exception(f"Unsupported route: \"{event['routeKey']}\"")
    
    except Exception as err:
        status_code = 400
        body = str(err)
    
    finally:
        body = json.dumps(body)
    
    return {
        'statusCode': status_code,
        'body': body,
        'headers': headers
    }
