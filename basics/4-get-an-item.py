                                                 # read an item in the table

# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
import json                                   
import decimal

# This queries for all of the users whose particular key equals the value
from boto3.dynamodb.conditions import Key, Attr               

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError                     

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

# service resource request and region are set
dynamodb = boto3.resource("dynamodb", region_name='us-east-1')        
table = dynamodb.Table('MOVIES_DB')

title = "Pictolearn Movie"
year = 2019

# try block
try:
    response = table.get_item(                                       
        Key={
            'year': year,
            'title': title
        }
    )
    
# exception handling
except ClientError as e:                                             
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))