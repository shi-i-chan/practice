import requests
import pandas as pd

from utils import save_new_data, start, ROOT_DIR

fn = f'{ROOT_DIR}/data/api_parser_data.csv'


def update_data():
    params = {
        'locale': 'en-US'
    }
    BASE_URL = 'https://api.bybit.com/'
    url = f'{BASE_URL}v5/announcements/index'
    new_df = pd.DataFrame(requests.get(url, params=params).json()['result']['list'])
    new_df = new_df[['dateTimestamp', 'title', 'url']]
    new_df['dateTimestamp'] = pd.to_datetime(new_df['dateTimestamp'], unit='ms')
    new_df = new_df.rename(columns={'dateTimestamp': 'date'})
    save_new_data(new_df, fn)


start(update_data, fn)
