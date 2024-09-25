import pandas as pd
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from util.constants import CLIENT_ID, SECRET_ID, OUTPUT_PATH


def reddit_pipeline(filename: str , subreddit : str , time_filter = 'day', limit = None):
    instance = connect_reddit(CLIENT_ID, SECRET_ID, 'Airscholar Agent')
    
    # Extraction
    extracted_data =extract_posts(instance, subreddit, time_filter, limit)
    extracted_df = pd.DataFrame(extracted_data)
    
    # Transformation
    transformed_df = transform_data(extracted_df)
    
    # Loading to csv
    file_path = f'{OUTPUT_PATH}/{filename}.csv'
    transformed_df.to_csv(file_path, index=False)
    
    # load_data_to_csv(transformed_df, file_path)
    
    return file_path