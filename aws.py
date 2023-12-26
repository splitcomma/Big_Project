import boto3

# Replace 'your-access-key' and 'your-secret-key' with your AWS credentials
aws_access_key = 'your-access-key'
aws_secret_key = 'your-secret-key'

# Replace 'us-east-1' with your preferred AWS region
region = 'us-west-1b'

# Create an RDS client
rds = boto3.client('rds', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

# Specify RDS instance details
db_instance_identifier = 'your-db-instance-id'
db_instance_class = 'db.t3.micro'
engine = 'mysql'
master_username = 'Andras'
master_password = 'VgtyoiPvLfpdenTNpWbo'

# Create RDS instance
response = rds.create_db_instance(
    DBInstanceIdentifier=db_instance_identifier,
    AllocatedStorage=20,
    DBInstanceClass=db_instance_class,
    Engine=engine,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    PubliclyAccessible=True
)

print(response)