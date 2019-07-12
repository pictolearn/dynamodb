import boto3                                   
import json                                   
import decimal


# This queries for all of the users whose particular key equals the value
from boto3.dynamodb.conditions import Key, Attr               

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError                     

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):

    # service resource request and region are set
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1')        
    table = dynamodb.Table('MOVIES_DB')
    
    title = event["title"]
    year = event["year"]
    
    
    
    # try block
    try:
        response = table.get_item(                                       
            Key={
                'year': int(year),
                'title': title
            }
        )
        item = response['Item']
        print("GetItem succeeded:")
        #print(json.dumps(item, indent=4, cls=DecimalEncoder))    
     
        return {
        'statusCode': 200,
        'body': json.dumps(item, indent=4, cls=DecimalEncoder)
        }
        
    # exception handling
    except ClientError as e:
        errorMsg = e.response['Error']['Message']
        print(errorMsg)
        return {
        'statusCode': 200,
        'body': json.dumps(errorMsg +" title >> " + title + " year >> " + year)
        }
    
    return {
        'statusCode': 200,
        'body': "Thanks"
    }
    