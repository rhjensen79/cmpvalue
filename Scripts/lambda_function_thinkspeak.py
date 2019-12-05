import json
import boto3

def handler(context, inputs):
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

    totalminutes = int(count*value)
    totalhours = int(totalminutes/60)
    totaldays = int(totalhours/24)
    
    
    url = "https://api.thingspeak.com/update.json"
   
    apikey = "api_key=YourAPIkey"
    field1 = "&field1="
    field1value = str(count)
    field2 = "&field2="
    field2value = str(value)
    field3 = "&field3="
    field3value = str(totalminutes)
    field4 = "&field4="
    field4value = str(totalhours)
    field5 = "&field5="
    field5value = str(totaldays)

    pl = apikey+field1+field1value+field2+field2value+field3+field3value+field4+field4value+field5+field5value
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    }
    
    r = context.request(url, 'POST', pl, headers=headers)

    