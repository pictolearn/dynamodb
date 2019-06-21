# update an item in the table

# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
import json                                   
import decimal  

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
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')   
table = dynamodb.Table('MOVIES_DB')

title = "Pictolearn Movie"
year = 2019

# updation of items occur
response = table.update_item(                                       
    Key={
        'year': year,
        'title': title
    },
    UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
    ExpressionAttributeValues={
      
      # decimal, Converts a finite Decimal instance to a rational number, exactly.
        ':r': decimal.Decimal(5.5),                                  
        ':p': "Everything happens all at once.",
        ':a': ["Larry", "Moe", "Curly"]
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))