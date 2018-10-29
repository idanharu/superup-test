from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com/")

table = dynamodb.Table('devops-challenge')

codeName = 'thedoctor'

try:
    response = table.get_item(
        Key={
            'code_name': codeName
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))

# Connect to Redis
#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/health")
def health():
     return json.dumps("{ status: healthy, container: https://hub.docker.com/r/idanharu/superup-test/ ,project: github.com/omerxx/ecscale }", indent=4, cls=DecimalEncoder)

@app.route("/secret")
def secret():
     return json.dumps(item, indent=4, cls=DecimalEncoder)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

