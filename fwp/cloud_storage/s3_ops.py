import os 
import sys
from io import StringIO
from typing import List, Union
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3.service_resource import Bucket
from fwp.logger import logging


class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")
        
        
    def upload_file(
        self,
        from_filename: str,
        to_filename: str,
        bucket_name: str,
        remove: bool = True,
    ) -> None:
        
        """
        
        Method Name : upload_file
        
        Description : this method uploads the from_filename file to buscket_name bucket
        
        Output : folder is created in s3 bucket
        """
        logging.info("enter the upload_file metjpod of s3Operation class")
        
        try:
            logging.info(
                f"Uploading {from_filename} file to {to_filename} file in {bucket_name}
            )
            
            self.s3_resource.meta.client.upload_file(
                from_filename, bucket_name, to_filename
            )
            
            logging.info(
                f"Uploaded {from_filename} file to {to_filename} file in {bucket_name}
            )
            
            self.s3_resource.meta.client.upload_file(
                from_filename, bucket_name, to_filename
            )
            
            logging.info(
                f"Uploaded {from_filename} file to {to_filename} file in {bucket_name}
            )
            
            if remove is True:
                os.remove(from_filename)
                logging.info(f"Remove is det {remove}")
                
            else:
                logging.info(f"Remove is set to {remove}")
                
            logging.info("exited the upload_file method")
            
        except Exception as e:
            raise e