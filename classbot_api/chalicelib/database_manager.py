

'''
    Dynamodb database utils
'''
import boto3
dynamodb = boto3.resource('dynamodb')
database_table = {}

def get_table(table_name) :
    if (table_name not in database_table) : 
        database_table[table_name] = dynamodb.Table(table_name)
    return database_table[table_name]
    