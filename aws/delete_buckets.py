# Authored by: Jonathan Gorczyca

import boto3
import re
import datetime
from boto3.session import Session
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = get_buckets(s3)
    session = Session()
    regions = session.get_available_regions('s3')
    clients = get_clients(regions)

    for bucket in buckets["Buckets"]:
        bucketName = bucket["Name"]
        currentLocation = s3.get_bucket_location(Bucket=bucketName)["LocationConstraint"]
        if currentLocation == None:
            currentLocation = "us-east-1"
        currentClient = clients[currentLocation]
        if not check_tags(s3, bucketName):
            delete_bucket_contents(currentClient, bucketName)
            delete_s3_bucket(currentClient, bucketName)

# Returns a dictionary containing a list of S3 Buckets whose names match the below regex and are more than 14 days old
def get_buckets(client):
    buckets = client.list_buckets()
    bucketsCopy = buckets

    for bucket in bucketsCopy["Buckets"]:
        bucketNameMatch = re.search("(blah)|(^blah)|(blah$)", bucket["Name"])
        bucketAge = datetime.datetime.now().astimezone() - bucket["CreationDate"]
        if bucketNameMatch == None or bucketAge.days >=14:
            buckets["Buckets"].remove(bucket)
    return buckets

# Returns a list with clients made for every available Region in S3
def get_clients(regions):
    clients = {}
    for region in regions:
        clients[region] = boto3.client('s3', region_name=region)
    return clients

# If a Bucket has the "reaperignore" and "donotdelete" tags, DO NOT mark them for deletion 
def check_tags(client, bucket):
    try:
        tags = client.get_bucket_tagging(Bucket=bucket)
        if tags:
            for tag in tags['TagSet']:
                if tag["Key"].lower() == "reaperignore" and tag["Value"].lower() == "donotdelete":
                   return True
        return False
    except ClientError:
        return False

# Deletes all objects, as well as any versions and delete markers (if the bucket is version-enabled) in the given S3 Bucket
def delete_bucket_contents(client, bucket):
    contents = client.list_objects(Bucket=bucket).get('Contents', [])

        # list_objects() can only return up to 1000 objects at a time
        while contents != []: 
            for content in contents:
                print("Deleting Object:", "[Key]:", content['Key'])
                client.delete_object(Bucket=bucket, Key=content['Key'])
            contents = client.list_objects(Bucket=bucket).get('Contents', [])

        versionsAndDMs = client.list_object_versions(Bucket=bucket)
        versions = []
        deleteMarkers = []

        # list_object_versions() can only return up to 1000 Objects at a time
        while ("Versions" in versionsAndDMs.keys()) and ("DeleteMarkers" in versionsAndDMs.keys()):
            versions = versionsAndDMs.get('Versions', [])
            for version in versions:
                print("Deleting Object Version:", "[Key]:", version['Key'], "[VersionId]:", version['VersionId'])
                client.delete_object(Bucket=bucket, Key=version['Key'], VersionId=version['VersionId'])
            deleteMarkers = versionsAndDMs.get('DeleteMarkers', [])
            for deleteMarker in deleteMarkers:
                print("Deleting Object Delete Marker:", "[Key]:", deleteMarker['Key'], "[VersionId]:", deleteMarker['VersionId'])
                client.delete_object(Bucket=bucket, Key=deleteMarker['Key'], VersionId=deleteMarker['VersionId'])
            versionsAndDMs = client.list_object_versions(Bucket=bucket)
                  
# Deletes the given S3 Bucket
def delete_s3_bucket(client, bucket):
    print("Deleting Bucket:", bucket)
    client.delete_bucket(Bucket=bucket)