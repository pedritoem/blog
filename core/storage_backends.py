from storages.backends.s3boton3 import S3Boto3Storage

class StaticStorage(S3BotoStorage):
    location = 'static'
    default_acl='private'

class MediaStore(S3Boto3Storage):
    location='media'
    file_overwrite=False