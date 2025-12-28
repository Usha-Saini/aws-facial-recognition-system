import boto3

# Initialize AWS clients
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition', region_name='ap-south-1')  # Change region if needed
dynamodbTableName = 'employeee'  # <-- Your DynamoDB table name
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
employeeTable = dynamodb.Table(dynamodbTableName)

def lambda_handler(event, context):
    print(event)

    # Get S3 bucket name and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # Index the employee image using Rekognition
        response = index_employee_image(bucket, key)
        print(response)

        # Check if the image indexing was successful
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            faceId = response['FaceRecords'][0]['Face']['FaceId']

            # Split filename to get first and last name (e.g., John_Doe.jpg)
            name = key.split('.')[0].split('_')
            firstName = name[0]
            lastName = name[1] if len(name) > 1 else ''

            # Register employee info into DynamoDB
            register_employee(faceId, firstName, lastName)

        return response

    except Exception as e:
        print(e)
        print(f"Error processing employee image {key} from bucket {bucket}")
        raise e


def index_employee_image(bucket, key):
    # Rekognition: index faces from the given S3 image
    response = rekognition.index_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        CollectionId='employees'  # <-- Your Rekognition collection name
    )
    return response


def register_employee(faceId, firstName, lastName):
    # Store employee record in DynamoDB
    employeeTable.put_item(
        Item={
            'rekoginitionid': faceId,
            'FirstName': firstName,
            'LastName': lastName
        }
    )
    print(f"Employee {firstName} {lastName} registered successfully.")
