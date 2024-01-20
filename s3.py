from boto3.session import Session

ACCESS_KEY_ID = ''
SECRET_KEY = ''

session = Session(aws_access_key_id=ACCESS_KEY_ID, 
                  aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')
bucket = "ritesh1buck"
my_bucket = s3.Bucket(bucket)
print("++++++ Object before upload+++++++\n")

for s3_files in my_bucket.objects.all():
   print(s3_files.key)

file_upload = '/Users/Ritesh/Desktop/Ritesh parashar/aadhar_back.jpeg'
object_name = 'aadhar_back.jpeg'
my_bucket.upload_file(file_upload,object_name)
print ( "\n+++++++object after upload+++++++\n")

for s3_files in my_bucket.objects.all():
   print(s3_files.key)

