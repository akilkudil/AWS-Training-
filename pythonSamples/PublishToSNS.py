import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    message = {"foo": "bar"}
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:814129119746:demoTester',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')