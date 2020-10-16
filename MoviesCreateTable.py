import boto3
session = boto3.Session() 
   
   
dynamodb = session.resource('dynamodb', region_name='us-east-1' ) 

def create_movie_table(): 
    table = dynamodb.create_table( 
        TableName='Movies', 
        KeySchema=[ 
            { 
                'AttributeName': 'year', 
                'KeyType': 'HASH' # Partition key 
            }, 
            { 
                'AttributeName': 'title', 
                'KeyType': 'RANGE' # Sort key 
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
            'ReadCapacityUnits': 5, 
            'WriteCapacityUnits': 5 
        } 
    ) 
    return table 

movie_table = create_movie_table() 
print("Table status:", movie_table.table_status)