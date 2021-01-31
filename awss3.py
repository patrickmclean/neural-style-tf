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
        localfilepath = imageRoot + location + filename
        #filename = filename.replace('.jpg','')
        print('Download ' + awsconfig['inputBucket']+" "+ localfilepath)
        s3.download_file(awsconfig['inputBucket'], filename, localfilepath)

class s3Upload:
    def __init__(self, localpath, filename, bucketname) :
        #Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")
        awsconfig = config_object["AWSS3"]
        imageRoot = config_object["LOCALFS"]['imageRoot']
        localpath = imageRoot + localpath
        bucketpath = awsconfig[bucketname]
        s3 = boto3.client('s3',
                        aws_access_key_id=awsconfig['accessKeyId'], 
                        aws_secret_access_key=awsconfig['secretAccessKey'],
                        region_name=awsconfig['region'])
        print('Upload ' + localpath + ' to ' + filename + '@' + bucketpath)
        with open(localpath, "rb") as f:
            s3.upload_fileobj(f,bucketpath ,filename)