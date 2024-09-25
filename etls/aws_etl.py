import s3fs
from util.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY_ID

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY_ID)
        return s3
    
    except Exception as e:
        print(e)
        
        
def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f"Bucket '{bucket}' created successfully.")
        else:
            print(f"Bucket '{bucket}' already exists.")
            
    except Exception as e:
        print(e)
        

def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, object_name: str):
    try:
        s3.put(file_path, bucket+'/raw/'+object_name)
        print(f'{object_name} uploaded to s3 successfully')
        
    except Exception as e:
        print(e)
        