def handler(context, inputs):
    #Import functions
    import boto3
    import json

    AWS_ACCESS_KEY_ID = 'YourAccessID'
    AWS_SECRET_ACCESS_KEY = 'YourAccessKey'

    s3 = boto3.client('s3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    #Read file
    object = s3.get_object(Bucket='YourS3Bucket',Key='counter.json')
    serializedObject = object['Body'].read()
    myData = json.loads(serializedObject)

    #set count var and convert it to int
    count = int(myData['deployment']['count'])
    value = int(myData['deployment']['value'])
    
    #add +1 to count
    count = count +1
    
    #Update var
    myData['deployment']['count'] = count
    myData['deployment']['value'] = 20

    #save mydata
    serializedMyData = json.dumps(myData)


    #Save file
    s3.put_object(Bucket='YourS3Bucket',Key='counter.json',Body=serializedMyData)


    outputs = {
        "Deployments": count,
        "Value": value
    }

    return outputs
