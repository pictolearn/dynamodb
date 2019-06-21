# querying of items in the table
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

#resource request and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')    

table = dynamodb.Table('MOVIES_DB')

print("Movies from 1985")

response = table.query(
  
  # condition expression
    KeyConditionExpression=Key('year').eq(1985)                      
)

for i in response['Items']:
    print(i['year'], ":", i['title'])