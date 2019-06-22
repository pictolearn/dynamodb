                                                         #scan
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
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
      
# resource request service and region are set

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')          


table = dynamodb.Table('MOVIES_DB')

fe = Key('year').between(1950, 1959)
pe = "#yr, title, info.rating"
# Expression Attribute Names for Projection Expression only.
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html
ean = { "#yr": "year", }

 # table scan
response = table.scan(
    FilterExpression=fe,                                                 
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

print("---------------------------")

while 'LastEvaluatedKey' in response:
    response = table.scan(
        ProjectionExpression=pe,
        FilterExpression=fe,
        ExpressionAttributeNames= ean,
        ExclusiveStartKey=response['LastEvaluatedKey']
        )

    for i in response['Items']:
        print(json.dumps(i, cls=DecimalEncoder))