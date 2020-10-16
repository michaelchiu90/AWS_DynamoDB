import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key, Attr
from decimal import *

session = boto3.Session()
dynamodb = session.resource('dynamodb', region_name='us-east-1' )

def read_item(year, title):
    table = dynamodb.Table('Movies')
    response = table.get_item(Key={'year': year, 'title': title})
    movie = response['Item']
    pprint(movie)
read_item(2012, 'End of Watch')

def query_movies(year):
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    movies = response['Items']
    print(f"Movies from {year}")
    for movie in movies:
        print(movie['year'], ":", movie['title'])
query_movies(2012)

def query_and_project_movies(year):
    table = dynamodb.Table('Movies')
    # Expression attribute names can only reference items in the projection expression.
    response = table.query(ProjectionExpression="#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames={"#yr": "year"},
    KeyConditionExpression= Key('year').eq(year) & Key('title').between('D', 'H')
    )
    print(f"Get year, title, genres, and lead actor")
    movies = response['Items']
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")
    pprint(movie['info'])
    print(f"\nCount:{response['Count']}")
    print(f"\nScanCount:{response['ScannedCount']}")

query_and_project_movies(2012)

def table_scan1():
    table = dynamodb.Table('Movies')
    response = table.scan(
    ProjectionExpression="#yr, title, info.genres, info.actors[0]",
    ExpressionAttributeNames={"#yr": "year"},
    FilterExpression=Key('title').begins_with('K')
    )
    pprint(response['Items'])
    print(f"\nCount:{response['Count']}")
    print(f"\nScanCount:{response['ScannedCount']}")
table_scan1()

def table_scan2():
    table = dynamodb.Table('Movies')
    response = table.scan(
    ProjectionExpression="#yr, title, info.genres, info.actors[0], info.rating",
    ExpressionAttributeNames={"#yr": "year"},
    FilterExpression=Attr('info.rating').gte(Decimal(9))
    )
    pprint(response['Items'])
    print(f"\nCount:{response['Count']}")
    print(f"\nScanCount:{response['ScannedCount']}")
table_scan2()