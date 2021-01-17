import boto3
from configparser import ConfigParser 

class s3Download:
    def __init__(self,location, filename) :
        #Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")
        awsconfig = config_object["AWSS3"]
        imageRoot = config_object["LOCALFS"]['imageRoot']
        s3 = boto3.client('s3',
                        aws_access_key_id=awsconfig['accessKeyId'], 
                        aws_secret_access_key=awsconfig['secretAccessKey'],
                        region_name=awsconfig['region'])
        localfilepath = imageRoot + '/' + filename
        filename = filename.replace('.jpg','')
        print('Download ' + awsconfig['inputBucket']+" "+ filename+" "+ localfilepath)
        s3.download_file(awsconfig['inputBucket'], filename, localfilepath)