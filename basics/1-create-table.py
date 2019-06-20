# Creation of Table in DynamoDB
# a SDK package for aws in python
# Note this code will pick up aws credentials automatically from the .aws/credentials and .aws/config folder
import boto3                                                  

# aws service resource and region are set.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 

# attributes included
# here Attribute 'year' is a partition key and it is of type hash which is derived using hash function, Partition key   
# here Attribute 'title' is a sort key and it is of type Range, Sort key
# N represents the datatype of attribute 'year' should be a number
# S represents the datatype of attribute 'title' should be a string
# throughput parameters
table = dynamodb.create_table(                                  
    TableName='MOVIES_DB',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'                 
                                                                
        },
        {
            'AttributeName': 'title',                         
            'KeyType': 'RANGE'  
        }
        ],
    AttributeDefinitions=[                                      
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',                         
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,                             
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)