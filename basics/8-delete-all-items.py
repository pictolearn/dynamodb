                                                         #scan
# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
import json                                   

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError    

# This queries for all of the users whose particular key equals the value

from boto3.dynamodb.conditions import Key, Attr         

# Helper class to convert a DynamoDB item to JSON.

      
# resource request service and region are set

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')          


table = dynamodb.Table('MOVIES_DB')

pe = "#yr, title"
# Expression Attribute Names for Projection Expression only.
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html
ean = { "#yr": "year", }
 # table scan
response = table.scan(
    ProjectionExpression=pe,
    ExpressionAttributeNames=ean
    )

for item in response['Items']:
    # try block
    try:
        print ("Item with {} {} is being deleted".format(item['year'], item['title'])) 
        response = table.delete_item(
            Key={
                'year': item['year'],
                'title': item['title']
            }
        )
        
    # exception handling
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":               
            print(e.response['Error']['Message'])
        else:
            raise