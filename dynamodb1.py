import boto3 
import pprint 

session = boto3.Session() 
    
dynamodb = session.resource('dynamodb', region_name='us-east-1' ) 
table = dynamodb.Table('users') 

def table_scan(): 
    result = table.scan() 
    for i in result['Items']: 
        print(i) 
        
table_scan()

#table_scan() 
 
def insert_item_db(): 
    response = table.put_item( 
        Item={ 
            'username': 'janedoe', 
            'first_name': 'Jane', 
            'last_name': 'Doe', 
            'age': 25, 
            'hobbies':['badminton', 'foodball','singing'], 
            'account_type': 'standard_user' 
        } 
    ) 
    print(response) 
    
insert_item_db()

#insert_item_db() 

def get_db_item(): #retrieve an item using primary key 
    response = table.get_item( 
        Key={ 
            'username': 'janedoe' 
        } 
    ) 

    item = response['Item'] 
    print(item) 
    
get_db_item()