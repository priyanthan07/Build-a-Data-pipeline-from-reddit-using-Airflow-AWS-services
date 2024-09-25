import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET_ID = parser.get(section='api_keys', option='reddit_secret_key')
CLIENT_ID = parser.get(section='api_keys', option='reddit_client_id')

DATABASE_HOST = parser.get(section='database', option='database_host')
DATABASE_NAME = parser.get(section='database', option='database_name')
DATABASE_PORT = parser.get(section='database', option='database_port')
DATABASE_USER = parser.get(section='database', option='database_username')
DATABASE_PASSWORD = parser.get(section='database', option='database_password')

INPUT_PATH = parser.get(section='file_paths', option='input_path')
OUTPUT_PATH = parser.get(section='file_paths', option='output_path')

AWS_ACCESS_KEY_ID = parser.get(section='aws', option='aws_access_key_id')
AWS_SECRET_ACCESS_KEY_ID = parser.get(section='aws', option='aws_secret_access_key')
AWS_REGION = parser.get(section='aws', option='aws_region')
AWS_BUCKET_NAME = parser.get(section='aws', option='aws_bucket_name')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)