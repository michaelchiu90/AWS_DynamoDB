import boto3
import json
from decimal import Decimal
session = boto3.Session() 
   

dynamodb = session.resource('dynamodb', region_name='us-east-1' )
def load_movies(movies):
    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)

with open("moviedata.json") as json_file:
    movie_list = json.load(json_file, parse_float=Decimal)
load_movies(movie_list)