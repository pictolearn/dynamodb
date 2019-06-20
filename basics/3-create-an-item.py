# creating a new item in an existing table
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
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
 
# service from AWS and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')          

# Specify a table name
table = dynamodb.Table('MOVIES_DB')                                       

title ="Pictolearn Movie"
year = 2019

# putting items into the table
response = table.put_item(
   Item={
        'year': year,                                                     
        'title': title,
        'info': {
            'plot':"A nice theme",
            'rating': decimal.Decimal(0)
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))