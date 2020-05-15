import boto3
import json

client = boto3.client("ebs")

def get_snapshot_block():
    response = client.get_snapshot_block(
        SnapshotId='',
        BlockIndex=0,
        BlockToken=''
    )
    print(response['BlockData'].read())

#------------------------------------------------

def list_snapshot_blocks():
    response = client.list_snapshot_blocks(
        SnapshotId=''
    )
    for item in response['Blocks']:
        for key,value in item.items():
            print('{} : {}'.format(key,value))
        print('\n')

#------------------------------------------------

def list_changed_blocks():
    response = client.list_changed_blocks(
        FirstSnapshotId='',
        SecondSnapshotId=''
    )
    for item in response['ChangedBlocks']:
        if('FirstBlockToken' in item.keys()):
            for key,value in item.items():
                print('{} : {}'.format(key,value))
            print('\n')
