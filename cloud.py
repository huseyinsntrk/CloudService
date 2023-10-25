Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... 
... def hello_cloud(event, context):
...     # Gelen veriyi işliyoruz
...     request_body = json.loads(event['body'])
... 
...     # Yanıt oluşturuyoruz
...     response = {
...         "statusCode": 200,
...         "headers": {
...             "Content-Type": "application/json"
...         },
...         "body": json.dumps({
...             "message": "Cloud!",
...             "received_data": request_body
...         })
...     }
... 
