import pandas as pd
import requests
from http import HTTPStatus
from urllib3 import Retry
from urllib3.util.retry import Retry

csv_url = '/usr/local/airflow/include/data/retail_sales.csv'
api_url = 'https://dummyjson.com/products'

def extract_csv():
    df = pd.read_csv(csv_url)
    return df

def extract_api():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[502, 503, 504]
        )
    session.mount('https://', requests.adapters.HTTPAdapter(max_retries=retries))
    headers = {
        'user_agent': 'MyApp/5.0'
        }
    response = session.get(api_url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return pd.DataFrame(data['products'])