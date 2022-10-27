import ibm_boto3
from ibm_botocore.client import Config, ClientError

def Connect():
    # Constants for IBM COS values
    COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"
    COS_API_KEY_ID = "pZ55JIFi18dEoWZ8xdnXl_cYlVdEqg4UZ6aZYpys66-P"
    COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/8e190478c4604e38861e8c727f3d0516:028a9be7-8ebf-4880-92d4-43c4ec6f9461::"

    # Create resource
    try:
        cos = ibm_boto3.resource("s3",
        ibm_api_key_id=COS_API_KEY_ID,
        ibm_service_instance_id=COS_INSTANCE_CRN,
        config=Config(signature_version="oauth"),
        endpoint_url=COS_ENDPOINT
        )
        print("Connected Successfully :-)")
        return cos

    except:
        print("Error while connecting !")
        return 0

#List the items in a bucket
def get_bucket_contents(bucket_name,cos):
    res = []
    try:
        files = cos.Bucket(bucket_name).objects.all()
        print(files)
        for file in files:
            File = "https://"+bucket_name+".s3.us-east.cloud-object-storage.appdomain.cloud/"+file.key
            if("css" not in file.key):
                res.append(File)
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
        return 0
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))
        return 0
    return res

# List the bucket 
# def get_buckets(cos):
#     print("Retrieving list of buckets")
#     try:
#         buckets = cos.buckets.all()
#         for bucket in buckets:
#             print("Bucket Name: {0}".format(bucket.name))
#     except ClientError as be:
#         print("CLIENT ERROR: {0}\n".format(be))
#     except Exception as e:
#         print("Unable to retrieve list buckets: {0}".format(e))