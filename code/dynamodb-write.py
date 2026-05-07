import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')

def lambda_handler(event, context):
    table.put_item(
        Item={
            'Artist': 'Bruce Springsteen',
            'SongTitle': 'Born in the USA',
            'Album': 'Born in the USA',
            'ReleaseYear': 1984
        }
    )
    return {'statusCode': 200, 'body': 'Item written to Music table'}
