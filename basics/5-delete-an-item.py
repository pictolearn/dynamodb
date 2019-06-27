                                            # Deleting an item in a table
# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3  

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError     

import json                                        
import decimal

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
      
# resource request service and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')             
table = dynamodb.Table('MOVIES_DB')

title = "Pictolearn Movie"
year = 2019

print("Attempting a conditional delete...")

# try block
try:
    response = table.delete_item(
        Key={
            'year': year,
            'title': title                                                            
        },
        ConditionExpression="info.rating <= :val",
        ExpressionAttributeValues= {
            ":val": decimal.Decimal(6)
        }
    )
    print("DeleteItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))     

# exception handling
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":               
        print(e.response['Error']['Message'])
    else:
        raise