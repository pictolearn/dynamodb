                                        # query using title

# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
import json                                   
import decimal  

# This queries for all of the users whose particular key equals the value
from boto3.dynamodb.conditions import Key, Attr                     

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

# resource request service and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')   

table = dynamodb.Table('MOVIES_DB')

print("Movies from 1992 - titles A-L, with genres and lead actor")

# querying section
response = table.query(                                                                   
    ProjectionExpression="#yr, title, info.genres, info.actors[0]",

  # Expression Attribute Names for Projection Expression only.
    ExpressionAttributeNames={ "#yr": "year" }, 
    KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
)

print(response)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))