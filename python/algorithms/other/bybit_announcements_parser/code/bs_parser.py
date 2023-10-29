import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from utils import save_new_data, start, ROOT_DIR

from typing import List, Tuple


session = HTMLSession()
fn = f'{ROOT_DIR}/data/bs_parser_data.csv'
base_url = 'https://announcements.bybit.com'
announce_url = 'https://announcements.bybit.com/en-US/?category=&page=1'


def get_new_data(url: str) -> Tuple[List[str], List[str]]:
    r = session.get(url)
    # r.html.render()  # render js работает и так
    soup = BeautifulSoup(r.text, 'html.parser')
    articles_soup = soup.find('div', attrs={'class': 'article-list'})

    titles = articles_soup.find_all('div', attrs={'class': 'ant-typography ant-typography-ellipsis article-item-title'})
    titles = [title.text for title in titles]

    articles = articles_soup.find_all('a', attrs={'class': 'no-style'})
    urls = [base_url + article['href'] for article in articles]
    return titles, urls


def update_data():
    current_time = datetime.now()
    titles, urls = get_new_data(announce_url)
    data = {'date' : [current_time for _ in range(len(titles))],  # NOQA
            'title': titles,  # NOQA
            'url'  : urls}  # NOQA
    new_df = pd.DataFrame(data)
    save_new_data(new_df, fn)


start(update_data, fn)
