import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super().default(obj)

def lambda_handler(event, context):
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'], cls=DecimalEncoder),
        'headers': {'Content-Type': 'application/json'}
    }

