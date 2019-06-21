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

table = dynamodb.Table('users')


# querying section
response = table.query(
     IndexName="localIndex",                                 
     KeyConditionExpression=Key('age').eq(38) & Key('id').eq(1)
)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))