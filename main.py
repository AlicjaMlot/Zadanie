import boto3
import re

s3 = boto3.resource('s3')
bucket_name = 'developer-task'
prefix = 'y-wing/'


def list_files():
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.all:
        print(obj.key)

def upload_file():
    s3.Bucket(bucket_name).upload_file("file", "folder/file")


def list_filtered_files(filter_regex='filter'):
    compiled_regex = re.compile(filter_regex)
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        if compiled_regex.search(obj.key):
            print(obj.key)

def delete_matching_files(delete_regex='y_wing'):
    compiled_regex = re.compile(delete_regex)
    bucket = s3.Bucket(bucket_name)
    objects_to_delete = []
    for obj in bucket.objects.filter(Prefix=prefix):
        if compiled_regex.search(obj.key):
            objects_to_delete.append({'Key': obj.key})

    if objects_to_delete:
        bucket.delete_objects(Delete={'Objects': objects_to_delete})
        print(f"Deleted {len(objects_to_delete)} files matching regex '{delete_regex}'.")

list_files()
