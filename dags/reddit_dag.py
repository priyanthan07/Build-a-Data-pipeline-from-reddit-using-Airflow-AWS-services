from airflow import DAG
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airflow.operators.python import PythonOperator
from pipelines.etl_pipeline_reddit import reddit_pipeline
from pipelines.etl_pipeline_aws import s3_pipeline



default_args = {
    'owner': 'priyanthan',
    'start_date': datetime(year=2024, month=9, day=24)
}

file_postfix = datetime.now().strftime("%y%m%d%H%M%S")

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['reddit','etl','pipeline']
)

#Data extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs = {
        'filename' : f'reddit_{file_postfix}',
        'subreddit' : 'MachineLearning',
        'time_filter' : 'day',
        'limit' : 100
    },
    dag=dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id = 'aws_s3_upload',
    python_callable = s3_pipeline,
    dag=dag
)

extract >> upload_s3