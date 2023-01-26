# Authored by: Jonathan Gorczyca

import boto3
import re
import datetime

# This lambda vaildates the Record Sets and Hosted Zones to be deleted by ReaperRoute53 w/o actual deletion
def lambda_handler(event, context):
    client = boto3.client('route53')
    hosted_zones = get_hosted_zones(client)
    for zone in hosted_zones:
        print("Hosted Zone to be deleted:")
        print(zone)
        records = client.list_resource_record_sets(HostedZoneId=zone['Id'][12:])
        for record in records['ResourceRecordSets']:
            print("Deleting: " + record['Type'] + " record: " + record['Name'][:-1])
        print("Deleting hosted zone: " + zone['Name'])
        
# Returns list of Private hosted zones that are managed by Terraform, who's Names match the below regular expression, and are older than 2 weeks 
def get_hosted_zones(client):
    hosted_zones = client.list_hosted_zones()
    result = []
    for zone in hosted_zones['HostedZones']:
        nameResult = re.search("blah$", zone['Name'])
        commentResult = re.search("blah", zone['Config']['Comment'])
        privateZoneResult = zone['Config']['PrivateZone']
        if nameResult != None and commentResult != None and privateZoneResult:
            print("nameResult:")
            print(nameResult)
            print("commentResult:")
            print(commentResult)
            print("privateZoneResult:")
            print(privateZoneResult)
            callerReference = zone['CallerReference']
            creationYear = int(callerReference[10:14])
            creationMonth = int(callerReference[14:16].lstrip("0"))
            creationDay = int(callerReference[16:18].lstrip("0"))
            creationDate = datetime.datetime(creationYear, creationMonth, creationDay)
            age = datetime.datetime.now() - creationDate
            print("Age:")
            print(age.days)
            if age.days >= 14:
                result.append(zone)
    return result