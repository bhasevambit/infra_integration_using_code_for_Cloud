import boto3

client = boto3.client('ec2')
response = client.create_vpc(
    CidrBlock='10.0.0.0/16',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto3_example_vpc'
                },
                {
                    'Key': 'Managed',
                    'Value': 'boto3'
                }
            ]
        }
    ]
)

print(response)
