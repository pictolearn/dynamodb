# import data into the table 
# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
import json                                   
import decimal  

# service resource and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  

# table name in which you want to import data 
table = dynamodb.Table('MOVIES_DB')                              

# specify your JSON file name 
with open("./../data/moviedata.json") as json_file:                         
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)
 
 # put items into the table
        table.put_item(
           Item={                                                   
               'year': year,
               'title': title,
               'info': info,
            }
        )