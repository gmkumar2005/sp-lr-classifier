import click
import numpy as np
import dill
from sklearn.linear_model import LogisticRegression
# from google.colab import files
from os import listdir
import pandas as pd
import boto3
import io
from google.colab import files
import numpy as np

@click.command()
@click.option('--s3_endpoint_url', envvar='S3_ENDPOINT_URL')
@click.option('--s3_access_key', envvar='S3_ACCESS_KEY')
@click.option('--s3_secret_key', envvar='S3_SECRET_KEY')
@click.option('--s3_bucket', envvar='S3_BUCKET')
@click.option('--max_keys', envvar='MAX_KEYS',type=int)
def run_pipeline(
        s3_endpoint_url, 
        s3_access_key,
        s3_secret_key, 
        s3_bucket,
        max_keys):

    click.echo('s3_endpoint_url: %s' % s3_endpoint_url)
    click.echo('s3_access_key: %s' % s3_access_key)
    click.echo('s3_secret_key: %s' % s3_secret_key)
    click.echo('s3_bucket: %s' % s3_bucket)
    click.echo('pandas version: %s' % pd.__version__)

    s3 = boto3.client(service_name='s3',aws_access_key_id = s3_access_key, aws_secret_access_key = s3_secret_key, endpoint_url=s3_endpoint_url)

    response = s3.list_objects(Bucket="frauddetection", Prefix="training_setA/", MaxKeys=max_keys)

    click.echo('File names found :')   
    for file in response["Contents"]:
        click.echo('File names found : %s ' %file["Key"])
        
    df_list = []

    for file in response["Contents"]:
        obj = s3.get_object(Bucket="frauddetection", Key=file["Key"])
        obj_df = pd.read_csv(obj["Body"], sep='|')
        df_list.append(obj_df)

    df = pd.concat(df_list)
    click.echo('Head records            :' )
    click.echo('%s' % df.head())
    

    train, validate, test = np.split(df.sample(frac=1), [int(.6*len(df)), int(.8*len(df))])
    click.echo('length of the all data  : %s' % len(df))
    click.echo('length of the train     : %s' % len(train))
    click.echo('length of the validate  : %s' % len(validate))
    click.echo('length of the test      : %s' % len(test))
  
if __name__ == "__main__":
    run_pipeline()

