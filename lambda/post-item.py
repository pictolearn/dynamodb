# creating a new item in an existing table
# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package

# Test: curl -X POST -d "@post.json" <API-GATEWAY-URL>/<end-point> -k -v 

import boto3                                   
import json                                   
import decimal  

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError       

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    # service from AWS and region are set
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')          

    # Specify a table name
    table = dynamodb.Table('MOVIES_DB')  

    title = event["title"]
    year = event["year"]

    # try block
    try:
        
        # putting items into the table
        response = table.put_item(
        Item={
                'year': int(year),                                                     
                'title': title,
                'info': {
                    'plot':"A nice theme",
                    'rating': decimal.Decimal(0)
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response, indent=4, cls=DecimalEncoder)
        }
        # exception handling
    except ClientError as e:
        errorMsg = e.response['Error']['Message']
        print(errorMsg)
        return {
        'statusCode': 200,
        'body': json.dumps(errorMsg +" title >> " + title + " year >> " + year)
        }
